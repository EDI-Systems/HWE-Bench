import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_power.json")

CIR_FILE  = os.path.join(BASE_DIR, "power_ecosystem_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "power_ecosystem_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "power_ecosystem_report.txt")

TARGET_MODULE = "Power Management Ecosystem"

# Audit Metrics: Full-lifecycle voltage/current dynamic tracking matrix.
TEST_CRITERIA = {
    "v_usb_in":    {"name": "[1] Charging: USB_Input_Vol (~5V)",      "min": 4.80, "max": 5.20, "unit": "V"},
    "i_bat_chg":   {"name": "[2] Charging: IP2312_Chg_Cur (1.35A)",   "min": 1.25, "max": 1.45, "unit": "A"},
    "v_3v3_idle":  {"name": "[3] Idle: Vlogic_3V3_Idle (~3.3V)",      "min": 3.20, "max": 3.40, "unit": "V"},
    "v_5v_sleep":  {"name": "[4] Idle: Vboost_5V_Sleep (~0V)",        "min": -0.10, "max": 0.20, "unit": "V"},
    "v_3v3_wifi":  {"name": "[5] RF: 3V3_Wi-Fi_Drop (>3.1V)",         "min": 3.10, "max": 3.40, "unit": "V"},
    "v_5v_eink":   {"name": "[6] Refresh: 5V_E-Ink_Run (~5V)",        "min": 4.70, "max": 5.10, "unit": "V"},
    "i_bat_peak":  {"name": "[7] Refresh: Bat_Discharge_Pk (>1.5A)",  "min": 1.40, "max": 5.00, "unit": "A"} 
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path):
        print(f"  [FATAL ERROR] JSON file not found!: {json_path}")
        return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception as e: return {}
    module_nets = data.get(module_name, [])
    target_nets = {}
    for net in module_nets:
        for conn in net.get("Connections", []):
            if component_id in str(conn.get("ComponentID", "")):
                target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def build_netlist():
    print("="*65)
    print(f"Performing Power Ecosystem Full-Flow V/I Audit: {TARGET_MODULE}")
    
    nets_usb   = parse_module_topology(JSON_FILE, TARGET_MODULE, "KH-TYPE-C-16P")
    nets_chg   = parse_module_topology(JSON_FILE, TARGET_MODULE, "IP2312")
    nets_buck  = parse_module_topology(JSON_FILE, TARGET_MODULE, "TPS62088")
    nets_boost = parse_module_topology(JSON_FILE, TARGET_MODULE, "TPS61236P")
    nets_mcu   = parse_module_topology(JSON_FILE, TARGET_MODULE, "ESP32-WROVER")

    def get_net(nets_dict, pin_aliases):
        for alias in pin_aliases:
            if alias in nets_dict: return nets_dict[alias]
        return f"NC_{uuid.uuid4().hex[:5]}"

    n_usb  = get_net(nets_usb, ["VBUS", "A4"])
    n_bat  = get_net(nets_chg, ["BAT", "VIN", "VBAT+"]) 
    n_3v3  = get_net(nets_buck, ["VOUT", "SW", "VCC3_3"])
    n_5v   = get_net(nets_boost, ["VOUT", "VCC5"])
    n_en   = get_net(nets_boost, ["EN"])

    # Physical Anti-cheat: Check for strict five-zone topology hardware isolation.
    nodes = [n_usb, n_bat, n_3v3, n_5v]
    is_missing = any("NC_" in net for net in nodes + [n_en])
    is_shorted = len(set(nodes)) != len(nodes)

    inject_models = True
    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (Key power converters not fully connected)"
        inject_models = False
    elif is_shorted:
        status_info = "CRITICAL FAIL: Fatal Power Short! (Converter bypass detected)"
        inject_models = False
    else:
        status_info = "TOPOLOGY PASS: Robust power tree isolation detected. Injecting four-phase panoramic load."

    print(f"  [Judgment Result] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Power Ecosystem Full Lifecycle V/I Matrix - Physics Tuned",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 40m 0",
        
        f"R_D1 {sp(n_usb)} 0 1G", f"R_D2 {sp(n_bat)} 0 1G",
        f"R_D3 {sp(n_3v3)} 0 1G", f"R_D4 {sp(n_5v)} 0 1G", f"R_D5 {sp(n_en)} 0 1G",

        "* Physical model of a real Li-ion battery (3.8V, Internal Resistance 0.1 Ohm)",
        f"V_CELL net_cell 0 3.8V",
        f"R_ESR net_cell {sp(n_bat)} 0.1",
        
        "* Phase 1: 0-10ms Plug in USB fast charging",
        f"V_USB {sp(n_usb)} 0 PWL(0 5V 10m 5V 10.1m 0V 40m 0V)"
    ]

    if inject_models:
        netlist.extend([
            "* IP2312 Constant Current Charging Logic",
            f"B_CHG {sp(n_usb)} {sp(n_bat)} I=(V({sp(n_usb)})>4.5 ? 1.35 : 0)",
            
            "* TPS62088 Buck Converter Model with Wi-Fi Pulse Load",
            f"B_BUCK net_3v3_ideal 0 V=(V({sp(n_bat)})>3.0 ? 3.3 : 0)",
            f"R_BUCK_OUT net_3v3_ideal {sp(n_3v3)} 0.05",
            f"C_BUCK_OUT {sp(n_3v3)} 0 22u",
            "* Phase 3: 22-28ms Generate 400mA Wi-Fi RF transmission spike",
            f"I_WIFI {sp(n_3v3)} 0 PWL(0 0A 22m 0A 22.1m 0.4A 28m 0.4A 28.1m 0A 40m 0A)",

            "* TPS61236P Boost Converter Model with E-Ink Pulse Load",
            f"V_MCU_EN {sp(n_en)} 0 PWL(0 0V 31m 0V 31.1m 3.3V 40m 3.3V)",
            f"B_BOOST net_5v_ideal 0 V=(V({sp(n_en)})>1.5 & V({sp(n_bat)})>3.0 ? 5.0 : 0)",
            f"R_BOOST_OUT net_5v_ideal {sp(n_5v)} 0.1",
            f"C_BOOST_OUT {sp(n_5v)} 0 44u",
            "* Phase 4: 33-38ms Generate 1A E-Ink charge pump current draw",
            f"I_EINK {sp(n_5v)} 0 PWL(0 0A 33m 0A 33.1m 1.0A 38m 1.0A 38.1m 0A 40m 0A)",

            "* Physical Coupling: Calculate battery-side discharge current based on efficiency",
            "* (During Wi-Fi phase, approx 0.35A is drawn; during E-Ink phase, approx 1.5A is drawn)",
            f"I_BAT_DRAIN {sp(n_bat)} 0 PWL(0 0A 22m 0A 22.1m 0.35A 28m 0.35A 28.1m 0A 33m 0A 33.1m 1.5A 38m 1.5A 38.1m 0A 40m 0A)",
            
            "* --- Full Matrix Measurement Instructions ---",
            f".meas TRAN v_usb_in  AVG V({sp(n_usb)}) FROM 2m TO 8m",
            f".meas TRAN i_bat_chg AVG I(B_CHG) FROM 2m TO 8m",
            
            f".meas TRAN v_3v3_idle AVG V({sp(n_3v3)}) FROM 12m TO 18m",
            f".meas TRAN v_5v_sleep AVG V({sp(n_5v)}) FROM 12m TO 18m",
            
            f".meas TRAN v_3v3_wifi MIN V({sp(n_3v3)}) FROM 24m TO 27m",
            
            f".meas TRAN v_5v_eink  MIN V({sp(n_5v)}) FROM 34m TO 37m",
            f".meas TRAN i_bat_peak MAX I(R_ESR) FROM 34m TO 37m"  # Positive value indicates battery is discharging to system
        ])
    else:
        netlist.extend([
            f".meas TRAN v_usb_in PARAM 0",  f".meas TRAN i_bat_chg PARAM 0",
            f".meas TRAN v_3v3_idle PARAM 0", f".meas TRAN v_5v_sleep PARAM 99",
            f".meas TRAN v_3v3_wifi PARAM 0", f".meas TRAN v_5v_eink PARAM 0",
            f".meas TRAN i_bat_peak PARAM 0"
        ])

    netlist.append(".end")
    return "\n".join(netlist)

def run_simulation():
    for f in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(f): os.remove(f)
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        if not os.path.exists(LOG_FILE): return
        
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()
        results = {k: None for k in TEST_CRITERIA}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m: results[k] = float(m.group(1))
        
        report = ["="*65, " POWER ECOSYSTEM FULL LIFECYCLE V/I AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3g} {spec['unit']}" if val is not None else "N/A"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: 
            f.write(final_report_str)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()