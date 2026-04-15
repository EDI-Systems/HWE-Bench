import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE  = os.path.join(BASE_DIR, "soft_latch_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "soft_latch_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "soft_latch_report.txt")

TARGET_MODULE = "Portable Power Management System"

# Audit Metrics: 10-channel spatial-temporal cross-verification matrix
TEST_CRITERIA = {
    "i_bat_sleep": {"name": "[01|Sleep] Bat Leakage Curr (<1uA)",    "min": -0.000001, "max": 0.000001, "unit": "A"},
    "v_sys_sleep": {"name": "[02|Sleep] Sys Bus Isolation (~0V)",    "min": -0.10, "max": 0.20, "unit": "V"},
    "i_btn_drive": {"name": "[03|Ignition] Btn Drive Curr (>100uA)", "min": 0.0001, "max": 0.005, "unit": "A"},
    "v_q1_base":   {"name": "[04|Ignition] NPN Base V (~0.7V)",      "min": 0.50,  "max": 0.90, "unit": "V"},
    "v_q2_gate_1": {"name": "[05|Ignition] PMOS Gate Pull-down (~0V)", "min": -0.10, "max": 0.50, "unit": "V"},
    "v_sys_ignit": {"name": "[06|Ignition] Bus Startup V (~3.8V)",   "min": 3.60,  "max": 3.90, "unit": "V"},
    "i_mcu_hold":  {"name": "[07|Latch] MCU Hold Current (>100uA)",  "min": 0.0001, "max": 0.005, "unit": "A"},
    "v_q2_gate_2": {"name": "[08|Latch] PMOS Gate Sustain (~0V)",    "min": -0.10, "max": 0.50, "unit": "V"},
    "v_sys_latch": {"name": "[09|Latch] Bus Latch Voltage (~3.8V)",  "min": 3.60,  "max": 3.90, "unit": "V"},
    "v_sys_dead":  {"name": "[10|Shutdown] Bus Power-down Drop (~0V)", "min": -0.10, "max": 0.20, "unit": "V"}
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception: return {}
    target_nets = {}
    for net in data.get(module_name, []):
        for conn in net.get("Connections", []):
            if component_id == str(conn.get("ComponentID", "")):
                target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def get_net_strict(nets_dict, exact_pin_name):
    return nets_dict.get(exact_pin_name, f"NC_{uuid.uuid4().hex[:5]}")

def build_netlist():
    print("="*65)
    print(f"Launching Strict Pin Version (BC817) - 10-Channel Timing Audit: {TARGET_MODULE}")
    
    nets_btn  = parse_module_topology(JSON_FILE, TARGET_MODULE, "Power_Button")
    nets_npn  = parse_module_topology(JSON_FILE, TARGET_MODULE, "BC817")     # Strict BC817 check
    nets_pmos = parse_module_topology(JSON_FILE, TARGET_MODULE, "IRLM") 
    nets_mcu  = parse_module_topology(JSON_FILE, TARGET_MODULE, "ESP32-WROVER")

    # Adhere strictly to the new library PinNames
    n_pmos_s = get_net_strict(nets_pmos, "S")    
    n_pmos_d = get_net_strict(nets_pmos, "D")    
    n_pmos_g = get_net_strict(nets_pmos, "G")    
    n_npn_e  = get_net_strict(nets_npn, "E")     
    n_npn_b  = get_net_strict(nets_npn, "B")     
    n_npn_c  = get_net_strict(nets_npn, "C")     
    n_btn_in = get_net_strict(nets_btn, "In")
    n_btn_out= get_net_strict(nets_btn, "Out")
    n_mcu_io33 = get_net_strict(nets_mcu, "IO33") 

    nodes = [n_pmos_s, n_pmos_d, n_pmos_g, n_npn_c, n_npn_b, n_npn_e, n_btn_out, n_mcu_io33]
    is_missing = any("NC_" in net for net in nodes)
    
    # Critical Cascade Lock: PMOS Gate must connect to NPN Collector; NPN Emitter must be grounded.
    is_q1_q2_linked = (n_pmos_g == n_npn_c)
    is_npn_grounded = (n_npn_e in ["0", "GND", "net_gnd"])

    inject_models = True
    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (Pins not connected per standard specs)"
        inject_models = False
    elif not is_q1_q2_linked:
        status_info = "CRITICAL FAIL: Cascade Fault! (IRLM Gate not connected to BC817 Collector)"
        inject_models = False
    elif not is_npn_grounded:
        status_info = "CRITICAL FAIL: BC817 Emitter (E-pin) must be grounded!"
        inject_models = False
    else:
        status_info = "TOPOLOGY PASS: Valid Latch Topology Found, Deploying 10-Probe Matrix"

    print(f"  [Judgment] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Strict Pin Soft-Power Matrix Audit (BC817)",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 50m 0",
        
        f"R_D1 {sp(n_pmos_s)} 0 1G", f"R_D2 {sp(n_pmos_d)} 0 1G",
        f"R_D3 {sp(n_npn_b)} 0 1G", f"R_D4 {sp(n_mcu_io33)} 0 1G",

        f"V_BAT {sp(n_pmos_s)} 0 3.8V",
        f"R_SYS_LOAD {sp(n_pmos_d)} 0 100",
        f"C_SYS_FILTER {sp(n_pmos_d)} 0 10u",

        f"V_BTN {sp(n_btn_in)} 0 PWL(0 0V 10m 0V 10.01m 3.8V 30m 3.8V 30.01m 0V 50m 0V)",
        f"R_BTN_CONTACT {sp(n_btn_in)} {sp(n_btn_out)} 0.1",
        f"V_MCU_HOLD {sp(n_mcu_io33)} 0 PWL(0 0V 20m 0V 20.01m 3.3V 40m 3.3V 40.01m 0V 50m 0V)"
    ]

    if inject_models:
        netlist.extend([
            f"M1 {sp(n_pmos_d)} {sp(n_pmos_g)} {sp(n_pmos_s)} {sp(n_pmos_s)} P_IRLM",
            f".model P_IRLM VDMOS(pchan Rg=5 Vto=-0.7 Rd=39m Rs=10m Cgdmax=740p)",
            f"R_PU_PMOS {sp(n_pmos_g)} {sp(n_pmos_s)} 100k",

            "* Injecting BC817 Physical Model",
            f"Q1 {sp(n_npn_c)} {sp(n_npn_b)} {sp(n_npn_e)} NPN_BC817",
            f".model NPN_BC817 NPN(Is=1e-13 Bf=250 Vaf=100 Ise=1e-14 Ne=1.5 Ikf=0.5)",

            f"R_BASE_BTN {sp(n_btn_out)} {sp(n_npn_b)} 10k",
            f"R_BASE_MCU {sp(n_mcu_io33)} {sp(n_npn_b)} 10k",
            f"R_PD_BASE {sp(n_npn_b)} 0 100k",
            f"C_BASE_DELAY {sp(n_npn_b)} 0 100n",

            f".meas TRAN i_bat_sleep AVG I(V_BAT) FROM 2m TO 8m",
            f".meas TRAN v_sys_sleep AVG V({sp(n_pmos_d)}) FROM 2m TO 8m",
            f".meas TRAN i_btn_drive MAX I(R_BASE_BTN) FROM 12m TO 18m",
            f".meas TRAN v_q1_base   AVG V({sp(n_npn_b)}) FROM 12m TO 18m",
            f".meas TRAN v_q2_gate_1 AVG V({sp(n_pmos_g)}) FROM 12m TO 18m",
            f".meas TRAN v_sys_ignit AVG V({sp(n_pmos_d)}) FROM 12m TO 18m",
            f".meas TRAN i_mcu_hold  MAX I(R_BASE_MCU) FROM 32m TO 38m",
            f".meas TRAN v_q2_gate_2 AVG V({sp(n_pmos_g)}) FROM 32m TO 38m",
            f".meas TRAN v_sys_latch AVG V({sp(n_pmos_d)}) FROM 32m TO 38m",
            f".meas TRAN v_sys_dead  AVG V({sp(n_pmos_d)}) FROM 45m TO 49m"
        ])
    else:
        netlist.extend([
            f".meas TRAN i_bat_sleep PARAM 999", f".meas TRAN v_sys_sleep PARAM 999",
            f".meas TRAN i_btn_drive PARAM 0",   f".meas TRAN v_q1_base   PARAM 0",
            f".meas TRAN v_q2_gate_1 PARAM 999", f".meas TRAN v_sys_ignit PARAM 0",
            f".meas TRAN i_mcu_hold  PARAM 0",   f".meas TRAN v_q2_gate_2 PARAM 999",
            f".meas TRAN v_sys_latch PARAM 0",   f".meas TRAN v_sys_dead  PARAM 999"
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
        
        report = ["="*65, " SOFT-POWER 10-POINT MATRIX AUDIT (BC817 STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<33} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            if k == "i_bat_sleep" and val is not None: is_ok = abs(val) <= 0.000001
            else: is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
                
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            
            if val is None: val_str = "N/A"
            elif k == "i_bat_sleep": val_str = f"{abs(val)*1e9:>8.1f} nA"
            elif "A" in spec["unit"]: val_str = f"{val*1e6:>8.1f} uA"
            else: val_str = f"{val:>8.3g} {spec['unit']}"
                
            report.append(f"{spec['name']:<33} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_report_str)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()