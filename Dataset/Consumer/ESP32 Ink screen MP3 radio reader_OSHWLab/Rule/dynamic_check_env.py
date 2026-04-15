import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_env.json")

CIR_FILE  = os.path.join(BASE_DIR, "env_rtc_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "env_rtc_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "env_rtc_report.txt")

TARGET_MODULE = "Environmental Sensing & Timekeeping"

# Audit Metrics: 10-channel dual-power hot-swap and bus leakage voltage measurement matrix
TEST_CRITERIA = {
    "v_3v3_on":    {"name": "[01|MAIN] Normal 3.3V Steady State",        "min": 3.20,  "max": 3.40,  "unit": "V"},
    "v_rtc_main":  {"name": "[02|DIODE] RTC Voltage during Main Supply",  "min": 2.40,  "max": 3.80,  "unit": "V"},
    "i_bat_stby":  {"name": "[03|ISO] Battery Reverse Leakage during Main (~0)", "min": -0.05, "max": 0.05,  "unit": "uA"},
    "v_scl_high":  {"name": "[04|BUS] I2C High Level during Normal Operation",        "min": 3.00,  "max": 3.40,  "unit": "V"},
    "v_rtc_bat":   {"name": "[06|TAKEOVER] Actual RTC Voltage after Power Loss", "min": 2.20,  "max": 3.00,  "unit": "V"},
    "i_bat_active":{"name": "[07|CONS] Battery Sustain Current after Power Loss",      "min": 0.10,  "max": 2.00,  "unit": "uA"},
    "v_scl_dead":  {"name": "[08|BUS] I2C Bus Zeroing Voltage after Power Loss",      "min": -0.10, "max": 0.30,  "unit": "V"},
    "i_leak_scl":  {"name": "[09|LEAK] Reverse Leakage from RTC to I2C Bus",   "min": -0.10, "max": 0.10,  "unit": "uA"},
    "v_osc_alive": {"name": "[10|OSC] Osc Operating Voltage after Power Loss (>2V)",  "min": 2.00,  "max": 3.00,  "unit": "V"}
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
    print(f"Initiating Dual-Power Hot-Swap and Leakage Audit: Environment & RTC Module")
    
    nets_mcu = parse_module_topology(JSON_FILE, TARGET_MODULE, "ESP32")
    nets_rtc = parse_module_topology(JSON_FILE, TARGET_MODULE, "RX8010SJ")
    
    n_scl = get_net_robust(nets_mcu, "36", "IO22")
    n_sda = get_net_robust(nets_mcu, "33", "IO21")
    rtc_scl = get_net_robust(nets_rtc, "3", "SCL")
    rtc_vdd = get_net_robust(nets_rtc, "2", "VDD")

    print(f"  [INFO] Topology captured. Loading power loss simulator into physics engine...")
    print("="*65)

    def sp(n): return "0" if str(n).lower() in ["net_gnd", "0", "gnd"] else n

    netlist = [
        "* RTC Power Switchover & Bus Backpowering Audit",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 4m 0", # Run for 4ms, trigger power loss at 2ms
        
        "* Import real 1N4148 fast recovery diode model",
        ".model D1N4148 D(Is=2.52n Rs=.568 N=1.752 Cjo=4p M=.4 tt=20n IKF=8 Eg=1.11)",
        ".model SW_I2C SW(Vt=1.65 Ron=50 Roff=1G)"
    ]
    
    all_nodes = [n_scl, n_sda, rtc_scl, rtc_vdd]
    for idx, node in enumerate(set(all_nodes)):
        if sp(node) != "0":
            netlist.append(f"R_DUMMY_{idx} {sp(node)} 0 1G")

    netlist.extend([
        "* [1] Disaster Simulator: 3.3V Main Power drops to 0V at 2ms",
        f"V_3V3 net_3v3 0 PWL(0 0V 10u 3.3V 2m 3.3V 2.1m 0V 4m 0V)",
        
        "* [2] Coin Cell: Rock-solid 3.0V Backup Energy Source",
        f"V_BAT net_vbat 0 DC 3.0",
        
        "* [3] Diode OR-ing power path in schematic",
        f"D9 net_3v3 {sp(rtc_vdd)} D1N4148",
        f"D10 net_vbat {sp(rtc_vdd)} D1N4148",
        
        "* [4] Simulate RX8010SJ Internal Load (~1uA Crystal Sustain Consumption)",
        f"R_RTC_CORE {sp(rtc_vdd)} 0 2.5Meg",
        
        "* [5] Injecting Backpowering Vulnerability: Simulate ESD protection diode of RTC internal SCL pin",
        "* (If design is flawed, battery current flows through this diode to I2C pull-up during power loss)",
        f"D_ESD_SCL {sp(rtc_scl)} {sp(rtc_vdd)} D1N4148",
        
        "* [6] I2C Physical Environment (Pull-up resistor connected to 3.3V Main rail)",
        f"R_PU_SCL net_3v3 {sp(rtc_scl)} 4.7k",
        
        "* [7] Simulate ESP32 issuing I2C Clock (Active for first 2ms, then dead with power)",
        f"V_SCL_GATE net_scl_gate 0 PULSE(0 3.3 0 50n 50n 5u 10u 200)",
        f"S1 {sp(rtc_scl)} 0 net_scl_gate 0 SW_I2C",

        "* --- [8] 10 Microsecond-Level Monitoring Probes ---",
        "* Phase 1: Main Power Normal Operation period (1.0ms - 1.5ms)",
        f".meas TRAN v_3v3_on    AVG V(net_3v3) FROM 1.0m TO 1.5m",
        f".meas TRAN v_rtc_main  AVG V({sp(rtc_vdd)}) FROM 1.0m TO 1.5m",
        f".meas TRAN i_bat_stby  AVG I(V_BAT) FROM 1.0m TO 1.5m",
        f".meas TRAN v_scl_high  MAX V({sp(rtc_scl)}) FROM 1.0m TO 1.5m",
        
        "* Phase 2: Disaster Drop period (2.0ms Trigger)",
        f".meas TRAN t_drop_start TRIG V(net_3v3) VAL=3.0 FALL=1",
        f".meas TRAN t_drop_end   TRIG V(net_3v3) VAL=0.3 FALL=1",
        f".meas TRAN t_power_drop PARAM (t_drop_end-t_drop_start)",
        
        "* Phase 3: Battery Sustain period (3.0ms - 3.5ms)",
        f".meas TRAN v_rtc_bat   AVG V({sp(rtc_vdd)}) FROM 3.0m TO 3.5m",
        "* I(V_BAT) is negative when supplying; absolute value used for output current",
        f".meas TRAN i_bat_raw   AVG I(V_BAT) FROM 3.0m TO 3.5m",
        f".meas TRAN i_bat_active PARAM abs(i_bat_raw)", 
        
        f".meas TRAN v_scl_dead  MAX V({sp(rtc_scl)}) FROM 3.0m TO 3.5m",
        f".meas TRAN i_leak_raw  AVG I(D_ESD_SCL) FROM 3.0m TO 3.5m",
        f".meas TRAN i_leak_scl  PARAM abs(i_leak_raw)",
        
        "* Final Verification: Is RTC voltage sufficient to support crystal operation?",
        f".meas TRAN v_osc_alive AVG V({sp(rtc_vdd)}) FROM 3.0m TO 3.5m"
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
    
    report = ["="*65, " RTC POWER SWITCHOVER & BACKPOWERING MATRIX ", "="*65]
    report.append(f"{'Audit Node (Process Step)':<38} | {'Value':<12} | {'Status'}")
    report.append("-" * 65)
    
    pass_count = 0
    for k, spec in TEST_CRITERIA.items():
        val = results[k]
        
        if val is not None:
            if spec["unit"] == "uA": val = val * 1e6 
            elif spec["unit"] == "us": val = val * 1e6 
            
        is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
        if is_ok: pass_count += 1
        status_text = "PASS" if is_ok else "FAIL"
        
        if val is None: val_str = "N/A"
        elif "uA" in spec["unit"]: val_str = f"{val:>8.3f} uA"
        elif "us" in spec["unit"]: val_str = f"{val:>8.1f} us"
        else: val_str = f"{val:>8.2f} {spec['unit']}"
            
        report.append(f"{spec['name']:<38} | {val_str:<12} | {status_text}")
        
    report.append("-" * 65)
    report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
    
    final_report_str = "\n".join(report)
    print(final_report_str)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_report_str)

if __name__ == "__main__": 
    run_simulation()