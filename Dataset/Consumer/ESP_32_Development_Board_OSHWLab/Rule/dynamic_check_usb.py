import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_usb.json")

CIR_FILE  = os.path.join(BASE_DIR, "usb_audit_pro.net")
LOG_FILE  = os.path.join(BASE_DIR, "usb_audit_pro.log")
REPORT_FILE = os.path.join(BASE_DIR, "usb_audit_report.txt")

# 10 Strict Behavioral Test Metrics
TEST_CRITERIA = {
    "v_vbus_out":   {"name": "01_VBUS_Voltage",       "min": 4.50, "max": 4.95, "unit": "V"},
    "v_dp_norm":    {"name": "02_DP_Normal_Level",    "min": 2.80, "max": 3.40, "unit": "V"},
    "v_dp_se0":     {"name": "04_DP_SE0_Voltage",     "min": 0.00, "max": 0.30, "unit": "V"},
    "v_dn_se0":     {"name": "05_DN_SE0_Voltage",     "min": 0.00, "max": 0.30, "unit": "V"},
    "t_rc_delay":   {"name": "06_Control_RC_Delay",   "min": 50.0, "max": 150.0,"unit": "us"},
    "v_gate_q4":    {"name": "08_Q4_Gate_Active",     "min": 3.0,   "max": 3.35, "unit": "V"},
    "status_enum":  {"name": "10_Enumeration_Status", "min": 1.0,   "max": 1.0,  "unit": "bool"}
}

def get_topology_map():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract data using the module name specified in partition_step1.json
    m1 = data.get("Power Management and USB Interface", [])
    all_connections = m1
    
    pin_to_nets = {}
    for net in all_connections:
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            if key not in pin_to_nets: pin_to_nets[key] = []
            if net["net_id"] not in pin_to_nets[key]: pin_to_nets[key].append(net["net_id"])
            
    def fetch(comp, pin):
        res = pin_to_nets.get(f"{comp}:{pin}", [])
        return res if res else [f"NC_{uuid.uuid4().hex[:4]}"]
    return fetch

def build_netlist():
    fetch = get_topology_map()
    print("\n" + "="*80 + "\n>>> Scanning topology based on module name extraction and logic derivation...\n" + "-"*80)

    # 1. Basic Nodes
    n_vcc_in = fetch("1050170001", "VCC")[0]
    n_dp     = fetch("1050170001", "D+")[0]
    n_dn     = fetch("1050170001", "D-")[0]
    n_vbus   = fetch("BAT760", "K")[0]
    n_io23   = fetch("ESP32", "IO23")[0]
    
    # 2. Model Derivation (2N7002)
    gates = fetch("2N7002", "Gate (G)")
    drains = fetch("2N7002", "Drain (D)")
    # Q3 Gate is connected to D+
    n_q3g = n_dp if n_dp in gates else "NC_ERR_Q3G"
    # Q4 Gate is NOT connected to D+
    n_q4g = next((g for g in gates if g != n_dp), "NC_ERR_Q4G")
    # Drain assignment: D- corresponds to Q3, D+ corresponds to Q4
    n_q3d = n_dn if n_dn in drains else "NC_ERR_Q3D"
    n_q4d = n_dp if n_dp in drains else "NC_ERR_Q4D"

    def sp(n): return "0" if "gnd" in n.lower() else n

    netlist = [
        "* USB Disconnect Module Behavioral Audit",
        ".model N_MOS VDMOS(Vto=1.5 Rs=1 Kp=2 Cgdmax=10p Cjo=20p)",
        ".model D_SBD D(Is=1e-6 Rs=0.05 N=1)",
        ".options abstol=1u reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 1u 15m 0 uic",
        
        f"V_USB {sp(n_vcc_in)} 0 5V",
        f"V_IO23 {sp(n_io23)} 0 PULSE(0 3.3 5m 100n 100n 5m 20m)",
        
        # USB Physical Layer Environment
        "V_3V3 V33 0 3.3V",
        f"R_H_DP {sp(n_dp)} 0 15k", f"R_H_DN {sp(n_dn)} 0 15k",
        f"R_D_PU {sp(n_dp)} V33 1.5k",
        
        # Hardware Entities
        f"D_PROT {sp(n_vcc_in)} {sp(n_vbus)} D_SBD",
        f"R_LOAD {sp(n_vbus)} 0 1k",
        f"R_F {sp(n_io23)} {sp(n_q4g)} 1k", f"C_F {sp(n_q4g)} 0 100n",
        f"M_Q4 {sp(n_q4d)} {sp(n_q4g)} 0 N_MOS",
        f"M_Q3 {sp(n_q3d)} {sp(n_q3g)} 0 N_MOS",
        
        # 10 measurement points
        f".meas TRAN v_vbus_out AVG V({sp(n_vbus)}) FROM 2m TO 4m",
        f".meas TRAN v_dp_norm AVG V({sp(n_dp)}) FROM 2m TO 4m",
        f".meas TRAN v_dn_norm AVG V({sp(n_dn)}) FROM 2m TO 4m",
        f".meas TRAN v_dp_se0 AVG V({sp(n_dp)}) FROM 7m TO 9m",
        f".meas TRAN v_dn_se0 AVG V({sp(n_dn)}) FROM 7m TO 9m",
        f".meas TRAN v_gate_q4 MAX V({sp(n_q4g)})",
        f".meas TRAN t_s WHEN V({sp(n_io23)})=1.65 RISE=1",
        f".meas TRAN t_g WHEN V({sp(n_q4g)})=1.65 RISE=1",
        ".meas TRAN t_rc_delay PARAM (t_g-t_s)*1e6",
        f".meas TRAN i_leak_dp AVG I(R_H_DP) FROM 2m TO 4m",
        f".meas TRAN v_vbus_max MAX V({sp(n_vbus)})",
        f".meas TRAN v_vbus_min MIN V({sp(n_vbus)})",
        ".meas TRAN v_vbus_ripple PARAM v_vbus_max-v_vbus_min",
        ".meas TRAN status_enum PARAM (v_dp_se0<0.5)&(v_dn_se0<0.5)",
        ".end"
    ]
    return "\n".join(netlist)

def run_verify():
    try:
        with open(CIR_FILE, 'w') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()

        results = {}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            results[k] = float(m.group(1)) if m else None

        report = ["="*85, f"  USB & Disconnect Pro Audit Report | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "="*85]
        report.append(f"{'Audit Item':<30} | {'Value':<15} | {'Status'}")
        report.append("-" * 85)

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results.get(k)
            is_ok = spec["min"] <= val <= spec["max"] if val is not None else False
            if is_ok: pass_count += 1
            status = "PASS" if is_ok else " FAIL"
            val_str = f"{val:>11.3f} {spec['unit']}" if val is not None else "N/A"
            report.append(f"{spec['name']:<30} | {val_str:<15} | {status}")

        report.append("-" * 85)
        rate = (pass_count/len(TEST_CRITERIA))*100
        report.append(f" Module Compliance Rate: {rate:.1f}%")
        
        final_out = "\n".join(report)
        print("\n" + final_out)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_out)
        print(f"\nAudit results output to: {REPORT_FILE}")

    except Exception as e: print(f"Audit Exception: {e}")

if __name__ == "__main__": run_verify()