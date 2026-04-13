import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_bridge.json")

CIR_FILE  = os.path.join(BASE_DIR, "bridge_strict_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "bridge_strict_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "bridge_strict_report.txt")

TARGET_MODULE = "Wired Diagnostic & Programming Bridge"

# Audit Criteria: Verify cross-timing logic of EN and IO0 under various flow control combinations
TEST_CRITERIA = {
    "v_idle_en":  {"name": "[1] EN_Idle_State (3.3V)",    "min": 3.00, "max": 3.50, "unit": "V"},
    "v_prep_io0": {"name": "[2] IO0_Prep_Boot (0V)",      "min": -0.10, "max": 0.50, "unit": "V"},
    "v_rst_en":   {"name": "[3] EN_Hardware_Reset (0V)",  "min": -0.10, "max": 0.50, "unit": "V"},
    "v_safe_io0": {"name": "[4] IO0_Safe_Isolate (3.3V)", "min": 3.00, "max": 3.50, "unit": "V"} 
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
    print(f"Performing Auto-Download Logic Timing Audit: {TARGET_MODULE}")
    
    nets_uart = parse_module_topology(JSON_FILE, TARGET_MODULE, "CP2102") 
    nets_mcu  = parse_module_topology(JSON_FILE, TARGET_MODULE, "ESP32")

    def get_net(nets_dict, pin_aliases):
        for alias in pin_aliases:
            for key in nets_dict.keys():
                if alias in key: return nets_dict[key]
        return f"NC_{uuid.uuid4().hex[:5]}"

    # Extract core flow control pins
    n_dtr = get_net(nets_uart, ["DTR", "28"])
    n_rts = get_net(nets_uart, ["RTS", "24"])
    n_en  = get_net(nets_mcu,  ["EN", "CHIP_PU"])
    n_io0 = get_net(nets_mcu,  ["IO0", "GPIO0"])

    # --- Physical Correction: Strict Four-Zone Topology Isolation Check ---
    nodes = [n_dtr, n_rts, n_en, n_io0]
    is_missing = any("NC_" in net for net in nodes)
    is_shorted = len(set(nodes)) != len(nodes) # Any identical net IDs are considered violations

    inject_models = True
    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (DTR/RTS/EN/IO0 signals not fully connected)"
        inject_models = False
    elif is_shorted:
        status_info = "CRITICAL FAIL: Direct Short Violation! (DTR/EN or RTS/IO0 cannot be directly shorted)"
        inject_models = False
    else:
        status_info = "TOPOLOGY PASS: Control lines isolated, preparing to inject dual-transistor cross-logic"

    print(f"  [JUDGMENT] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Auto-Download Logic Timing Audit - Physics Tuned",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 40m 0",
        
        f"R_D1 {sp(n_dtr)} 0 1G", f"R_D2 {sp(n_rts)} 0 1G",
        f"R_D3 {sp(n_en)} 0 1G", f"R_D4 {sp(n_io0)} 0 1G",

        "* ESP32 Internal/External Pull-up Resistor and Capacitor Models",
        f"V_VDD net_vdd 0 3.3V",
        f"R_PU_EN {sp(n_en)} net_vdd 10k",
        f"C_EN    {sp(n_en)} 0 1u",
        f"R_PU_IO0 {sp(n_io0)} net_vdd 10k",

        "* Simulating four-phase flow control timing from Serial chip",
        "* 0-10ms (Standby): DTR=3.3, RTS=3.3",
        "* 10-20ms (IO0 Assert): DTR=3.3, RTS=0",
        "* 20-30ms (EN Reset): DTR=0, RTS=3.3",
        "* 30-40ms (Release): DTR=3.3, RTS=0",
        f"V_DTR {sp(n_dtr)} 0 PWL(0 3.3 10m 3.3 10.1m 3.3 20m 3.3 20.1m 0 30m 0 30.1m 3.3 40m 3.3)",
        f"V_RTS {sp(n_rts)} 0 PWL(0 3.3 10m 3.3 10.1m 0 20m 0 20.1m 3.3 30m 3.3 30.1m 0 40m 0)"
    ]

    # [CORE FIX]: Inject gold-standard transistor logic only if topology is valid
    if inject_models:
        netlist.extend([
            "* Injecting Gold-Standard Dual-Transistor Network (Simulating SS8050)",
            f"Q1 {sp(n_en)} net_q1_b {sp(n_dtr)} NPN_SS8050",
            f"R_Q1_B {sp(n_rts)} net_q1_b 10k",
            
            f"Q2 {sp(n_io0)} net_q2_b {sp(n_rts)} NPN_SS8050",
            f"R_Q2_B {sp(n_dtr)} net_q2_b 10k",
            
            ".model NPN_SS8050 NPN(Is=1e-14 Bf=300 Vaf=100)",

            f".meas TRAN v_idle_en  AVG V({sp(n_en)})  FROM 2m TO 8m",
            f".meas TRAN v_prep_io0 MIN V({sp(n_io0)}) FROM 12m TO 18m",
            f".meas TRAN v_rst_en   MIN V({sp(n_en)})  FROM 22m TO 28m",
            f".meas TRAN v_safe_io0 MAX V({sp(n_io0)}) FROM 22m TO 28m"
        ])
    else:
        # Prevent "parallel universe" scoring if topology is bypassed
        netlist.extend([
            f".meas TRAN v_idle_en  PARAM 0",
            f".meas TRAN v_prep_io0 PARAM 0",
            f".meas TRAN v_rst_en   PARAM 0",
            f".meas TRAN v_safe_io0 PARAM 0"
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
        
        report = ["="*65, " AUTO-DOWNLOAD LOGIC TIMING AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3g} {spec['unit']}" if val is not None else "0.0 V"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: 
            f.write(final_report_str)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()