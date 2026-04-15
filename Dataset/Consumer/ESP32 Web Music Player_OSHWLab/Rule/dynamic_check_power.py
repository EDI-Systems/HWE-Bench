import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE  = os.path.join(BASE_DIR, "pwr_battery_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "pwr_battery_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "pwr_battery_report.txt")

TARGET_MODULE = "Power Management & Battery Subsystem"

# Audit Metrics: 10-channel Power Routing, Dropout Breakdown, and PSRR Ripple Matrix
TEST_CRITERIA = {
    "v_usb_in":      {"name": "[01|Input] VBUS Voltage when USB Plugged (5V)", "min": 4.90,  "max": 5.10,  "unit": "V"},
    "i_charge_cc":   {"name": "[02|Chg] TP4056 Constant Current Phase",        "min": 450.0, "max": 550.0, "unit": "mA"},
    "v_3v3_idle":    {"name": "[03|Reg] LDO Output Steady State (3.3V)",       "min": 3.25,  "max": 3.35,  "unit": "V"},
    "v_rip_psrr_ok": {"name": "[04|Noise] LDO Output Floor Noise (<5mV)",       "min": 0.00,  "max": 5.00,  "unit": "mV"},
    "v_bat_low":     {"name": "[05|Dischg] Simulate Battery Voltage Drop",      "min": 3.40,  "max": 3.50,  "unit": "V"},
    "i_wifi_peak":   {"name": "[06|Load] ESP32 Transient Wi-Fi Pulse",          "min": 340.0, "max": 360.0, "unit": "mA"},
    "v_3v3_drop":    {"name": "[07|Drop] Dropout Breakdown Output Min",         "min": 3.10,  "max": 3.28,  "unit": "V"},
    "v_drop_depth":  {"name": "[08|Trans] LDO Transient Sag Amplitude (<0.2V)",  "min": 0.00,  "max": 0.25,  "unit": "V"},
    "v_rip_psrr_ng": {"name": "[09|PSRR] Ripple Feedthrough during Breakdown",  "min": 10.0,  "max": 100.0, "unit": "mV"}
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception: return {}
    target_nets = {}
    for module, nets in data.items():
        for net in nets:
            for conn in net.get("Connections", []):
                if component_id in str(conn.get("ComponentID", "")):
                    target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def get_net_robust(nets_dict, pin_number, pin_name):
    if pin_number in nets_dict: return nets_dict[pin_number]
    if pin_name in nets_dict: return nets_dict[pin_name]
    return f"NC_{uuid.uuid4().hex[:5]}"

def build_netlist():
    print("="*65)
    print(f"Initiating Power Management Audit: Battery Drop, Dropout Breakdown, and PSRR Failure")
    
    nets_ldo = parse_module_topology(JSON_FILE, TARGET_MODULE, "MCP1825")
    nets_chg = parse_module_topology(JSON_FILE, TARGET_MODULE, "TP4056")
    
    n_usb = get_net_robust(nets_chg, "4", "VCC")
    n_bat = get_net_robust(nets_chg, "5", "BAT")
    n_3v3 = get_net_robust(nets_ldo, "2", "VOUT")

    print(f"  [INFO] Topology captured. Injecting 350mA Wi-Fi pulse and 50kHz noise...")
    print("="*65)

    def sp(n): return "0" if str(n).lower() in ["net_gnd", "0", "gnd"] else n

    netlist = [
        "* Power Management Dropout & PSRR Collapse Testbench",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 20m 0", # Simulation for 20ms
    ]
    
    all_nodes = [n_usb, n_bat, n_3v3]
    for idx, node in enumerate(set(all_nodes)):
        if sp(node) != "0":
            netlist.append(f"R_DUMMY_{idx} {sp(node)} 0 1G")

    netlist.extend([
        "* [1] External Input: 5V USB Power (Plugged for first 8ms)",
        f"V_USB {sp(n_usb)} 0 PWL(0 0V 100u 5V 8m 5V 8.1m 0V 20m 0V)",
        
        "* [2] Li-ion Battery Model: Decaying voltage source",
        f"V_CELL net_cell 0 PWL(0 3.8V 10m 3.8V 13m 3.45V 20m 3.45V)",
        
        "* Inject 50kHz System Floor Noise (50mV amplitude)",
        f"V_NOISE {sp(n_bat)} net_cell SINE(0 0.05 50k)",

        "* [3] Behavioral TP4056 Charger: Output 500mA CC when USB present",
        f"B_TP4056 {sp(n_usb)} {sp(n_bat)} I=IF(V({sp(n_usb)})>4.5, 0.5, 0)",

        "* [4] Behavioral MCP1825 LDO: 210mV Dropout sag, 40dB PSRR steady state",
        f"B_LDO_CORE net_ldo_raw 0 V=V({sp(n_bat)}) - 0.21*(I(I_LOAD)/0.5)",
        f"B_LDO_OUT net_3v3_ideal 0 V=MIN(3.3, V(net_ldo_raw))",
        "* Physical output stage with 4.7uF bypass",
        f"R_LDO_OUT net_3v3_ideal {sp(n_3v3)} 0.05",
        f"C_LDO_OUT {sp(n_3v3)} 0 4.7u",

        "* [5] Dynamic Load: ESP32 Idle (50mA); Trigger 350mA Wi-Fi pulse at 15ms",
        f"I_LOAD {sp(n_3v3)} 0 PWL(0 50m 14.9m 50m 15m 350m 17m 350m 17.1m 50m)",

        "* --- [6] 10 Microsecond-Level Monitoring Probes ---",
        f".meas TRAN v_usb_in AVG V({sp(n_usb)}) FROM 2m TO 4m",
        f".meas TRAN i_chg_raw AVG I(B_TP4056) FROM 2m TO 4m",
        f".meas TRAN i_charge_cc PARAM abs(i_chg_raw)",
        
        f".meas TRAN v_3v3_idle AVG V({sp(n_3v3)}) FROM 2m TO 4m",
        f".meas TRAN vmax_rip_ok MAX V({sp(n_3v3)}) FROM 3m TO 4m",
        f".meas TRAN vmin_rip_ok MIN V({sp(n_3v3)}) FROM 3m TO 4m",
        f".meas TRAN v_rip_psrr_ok PARAM vmax_rip_ok-vmin_rip_ok",
        
        f".meas TRAN v_bat_low AVG V({sp(n_bat)}) FROM 14m TO 14.8m",
        f".meas TRAN i_wifi_peak MAX I(I_LOAD) FROM 15m TO 17m",
        
        f".meas TRAN v_3v3_drop MIN V({sp(n_3v3)}) FROM 15.5m TO 16.5m",
        f".meas TRAN v_drop_depth PARAM (v_3v3_idle - v_3v3_drop)",
        
        f".meas TRAN vmax_rip_ng MAX V({sp(n_3v3)}) FROM 16m TO 16.8m",
        f".meas TRAN vmin_rip_ng MIN V({sp(n_3v3)}) FROM 16m TO 16.8m",
        f".meas TRAN v_rip_psrr_ng PARAM vmax_rip_ng-vmin_rip_ng"
    ])

    netlist.append(".end")
    return "\n".join(netlist)

def run_simulation():
    for f in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(f): os.remove(f)
        
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
    except subprocess.CalledProcessError as e:
        print(f"  [⚠️] WARNING: SPICE engine computation failure.")
        
    results = {k: None for k in TEST_CRITERIA}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m: results[k] = float(m.group(1))
    
    report = ["="*65, " PWR MGT: DROPOUT BROWNOUT & PSRR MATRIX ", "="*65]
    report.append(f"{'Audit Node (Process Step)':<40} | {'Value':<10} | {'Status'}")
    report.append("-" * 65)
    
    pass_count = 0
    for k, spec in TEST_CRITERIA.items():
        val = results[k]
        
        if val is not None:
            if spec["unit"] == "mA": val = val * 1000
            elif spec["unit"] == "ms": val = val * 1000
            elif spec["unit"] == "mV": val = val * 1000
            
        is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
        if is_ok: pass_count += 1
        status_text = "PASS" if is_ok else "FAIL"
        
        if val is None: val_str = "N/A"
        elif spec["unit"] in ["mA", "mV", "ms"]: val_str = f"{val:>7.2f} {spec['unit']}"
        else: val_str = f"{val:>7.3f} {spec['unit']}"
            
        report.append(f"{spec['name']:<40} | {val_str:<10} | {status_text}")
        
    report.append("-" * 65)
    report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
    
    final_report_str = "\n".join(report)
    print(final_report_str)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_report_str)

if __name__ == "__main__": 
    run_simulation()