import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_power.json")

CIR_FILE  = os.path.join(BASE_DIR, "power_ecosystem_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "power_ecosystem_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "power_ecosystem_report.txt")

TARGET_MODULE = "Power Management Ecosystem"

# Audit Criteria: Covers charging/discharging, RF noise immunity, and high-load boost dynamic flows
TEST_CRITERIA = {
    "i_charge_cc":    {"name": "[1] IP2312_Fast_Charge (1.35A)",  "min": 1.25, "max": 1.45, "unit": "A"},
    "v_buck_wifi":    {"name": "[2] TPS62088_3V3_Wi-Fi_Drop",     "min": 3.10, "max": 3.40, "unit": "V"},
    "v_boost_sleep":  {"name": "[3] TPS61236_5V_DeepSleep_Leak",  "min": -0.10, "max": 0.20, "unit": "V"},
    "v_boost_eink":   {"name": "[4] TPS61236_5V_E-Ink_Refresh",   "min": 4.70, "max": 5.10, "unit": "V"} 
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
    print(f"Performing Full-Flow Power Dynamic Audit: {TARGET_MODULE}")
    
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

    # --- Physical Correction: Strict Five-Zone Topology Isolation Check ---
    nodes = [n_usb, n_bat, n_3v3, n_5v]
    is_missing = any("NC_" in net for net in nodes + [n_en])
    is_shorted = len(set(nodes)) != len(nodes)

    inject_models = True
    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (Key power converters not fully connected)"
        inject_models = False
    elif is_shorted:
        status_info = "CRITICAL FAIL: Fatal Power Short! (Converter found bypassed/shorted)"
        inject_models = False
    else:
        status_info = "TOPOLOGY PASS: Solid power tree isolation found, preparing to inject dynamic loads"

    print(f"  [JUDGMENT] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Power Ecosystem Dynamic Transient Audit - Physics Tuned",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 30m 0",
        
        f"R_D1 {sp(n_usb)} 0 1G", f"R_D2 {sp(n_bat)} 0 1G",
        f"R_D3 {sp(n_3v3)} 0 1G", f"R_D4 {sp(n_5v)} 0 1G", f"R_D5 {sp(n_en)} 0 1G",

        f"V_CELL net_cell 0 3.8V",
        f"R_ESR net_cell {sp(n_bat)} 0.1",
        f"V_USB {sp(n_usb)} 0 PWL(0 5V 10m 5V 10.1m 0V 30m 0V)",
    ]

    # Construct physical models and real measurements only if topology is valid
    if inject_models:
        netlist.extend([
            f"B_CHG {sp(n_usb)} {sp(n_bat)} I=(V({sp(n_usb)})>4.5 ? 1.35 : 0)",
            f".meas TRAN i_charge_cc AVG I(B_CHG) FROM 2m TO 8m",

            f"B_BUCK net_3v3_ideal 0 V=(V({sp(n_bat)})>3.0 ? 3.3 : 0)",
            f"R_BUCK_OUT net_3v3_ideal {sp(n_3v3)} 0.05",
            f"C_BUCK_OUT {sp(n_3v3)} 0 22u",
            f"I_WIFI_LOAD {sp(n_3v3)} 0 PWL(0 10m 11m 10m 11.1m 400m 15m 400m 15.1m 10m 30m 10m)",
            f".meas TRAN v_buck_wifi MIN V({sp(n_3v3)}) FROM 12m TO 15m",

            f"V_MCU_EN {sp(n_en)} 0 PWL(0 0V 21m 0V 21.1m 3.3V 30m 3.3V)",
            f"B_BOOST net_5v_ideal 0 V=(V({sp(n_en)})>1.5 & V({sp(n_bat)})>3.0 ? 5.0 : 0)",
            f"R_BOOST_OUT net_5v_ideal {sp(n_5v)} 0.1",
            f"C_BOOST_OUT {sp(n_5v)} 0 44u",
            f"I_EINK_LOAD {sp(n_5v)} 0 PWL(0 0A 23m 0A 23.1m 1A 28m 1A 28.1m 0A 30m 0A)",
            f".meas TRAN v_boost_sleep MAX V({sp(n_5v)}) FROM 2m TO 18m",
            f".meas TRAN v_boost_eink MIN V({sp(n_5v)}) FROM 24m TO 27m",
        ])
    else:
        # If topology violation detected, force parameters to 0 to prevent scoring
        netlist.extend([
            f".meas TRAN i_charge_cc PARAM 0",
            f".meas TRAN v_buck_wifi PARAM 0",
            f".meas TRAN v_boost_sleep PARAM 0",
            f".meas TRAN v_boost_eink PARAM 0"
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
        
        report = ["="*65, " POWER ECOSYSTEM TRANSIENT AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3g} {spec['unit']}" if val is not None else "0.0 V/A"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: 
            f.write(final_report_str)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()