import os
import subprocess
import re
import json
import datetime
import uuid
# 1. Environment Configuration
LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_rev.json")

CIR_FILE  = os.path.join(BASE_DIR, "rev_prot_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "rev_prot_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "rev_prot_audit_report.txt")

TEST_CRITERIA = {
    "v_out_normal":   {"name": "V_OUT_Normal_24V",   "min": 23.0,  "max": 24.5,  "unit": "V"},
    "v_gs_normal":    {"name": "V_GS_Clamped_Normal","min": -11.0, "max": -8.0,  "unit": "V"},
    "v_out_reverse":  {"name": "V_OUT_Reverse_Block","min": -1.5,  "max": 0.5,   "unit": "V"},
    "v_gs_reverse":   {"name": "V_GS_Reverse_Safe",  "min": -0.5,  "max": 1.0,   "unit": "V"}
}

def get_topology():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError("JSON File not found.")
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("Reverse Polarity Protection & Power Input", [])
    pin_to_nets = {}
    for net in target:
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            if key not in pin_to_nets: pin_to_nets[key] = []
            if net["net_id"] not in pin_to_nets[key]: pin_to_nets[key].append(net["net_id"])
            
    def fetch(comp, pin):
        res = pin_to_nets.get(f"{comp}:{pin}", [])
        if not res:
            return [f"NC_{uuid.uuid4().hex[:4]}"]
        return res
    return fetch

def build_netlist():
    fetch = get_topology()

    n_vlipo = fetch("3401", "D")[0]
    n_vmain = fetch("3401", "S")[0]
    n_gate  = fetch("3401", "G")[0]
    
    n_zener_k = fetch("MM3Z10VT1G", "K")[0]
    n_zener_a = fetch("MM3Z10VT1G", "A")[0]

    netlist = [
        "* Reverse Polarity Protection Behavioral Audit",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 10u 10m 0 uic",
        
        "* Testbench: Bipolar Power Supply to simulate Normal and Reverse Connection",
        "* 0-5ms: +24V (Normal Connection), 5-10ms: -24V (Reverse Connection)",
        f"V_LIPO {n_vlipo} 0 PWL(0 0 0.5m 24 4.5m 24 5m 0 5.5m -24 9.5m -24 10m 0)",
        
        "* Testbench: External Bias and Load",
        f"R_GATE {n_gate} 0 100k",
        f"R_LOAD {n_vmain} 0 1k",
        f"C_LOAD {n_vmain} 0 10uF",
        
        "* DUT: P-Channel MOSFET (3401)",
        f"M_Q1 {n_vlipo} {n_gate} {n_vmain} {n_vmain} P_3401",
        ".model P_3401 VDMOS(pchan Vto=-0.8 Rs=0.044 Kp=15 Cgdmax=600p Cjo=600p Vds=-30 mtriodes=1)",
        
        "* DUT: 10V Zener Diode (MM3Z10VT1G)",
        f"D_Z1 {n_zener_a} {n_zener_k} D_10V",
        ".model D_10V D(Is=1e-11 Rs=5 N=1.5 Bv=10 Ibv=5m Cjo=50p)",
        
        "* Automated Measurements",
        f".meas TRAN v_out_normal AVG V({n_vmain}) FROM 3m TO 4m",
        f".meas TRAN v_gate_normal AVG V({n_gate}) FROM 3m TO 4m",
        ".meas TRAN v_gs_normal PARAM v_gate_normal-v_out_normal",
        
        f".meas TRAN v_out_reverse AVG V({n_vmain}) FROM 8m TO 9m",
        f".meas TRAN v_gate_reverse AVG V({n_gate}) FROM 8m TO 9m",
        ".meas TRAN v_gs_reverse PARAM v_gate_reverse-v_out_reverse",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: 
            f.write(build_netlist())
            
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
        with open(LOG_FILE, 'r', errors='ignore') as f: 
            log = f.read()

        results = {}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m:
                results[k] = float(m.group(1))
            else:
                results[k] = None

        report_lines = []
        report_lines.append("---------------------------------------------------------")
        report_lines.append(f"{'Audit Item':<25} | {'Value':<12} | {'Status'}")
        report_lines.append("---------------------------------------------------------")

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results.get(k)
            is_ok = spec["min"] <= val <= spec["max"] if val is not None else False
            if is_ok: 
                pass_count += 1
            status = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3f} {spec['unit']}" if val is not None else "N/A"
            report_lines.append(f"{spec['name']:<25} | {val_str:<12} | {status}")

        report_lines.append("---------------------------------------------------------")
        rate = (pass_count / len(TEST_CRITERIA)) * 100
        report_lines.append(f"passrate: {rate:.1f}%")
        
        final_report = "\n".join(report_lines)
        print(final_report)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_report)

    except Exception as e: 
        print(f"Simulation Error: {e}")

if __name__ == "__main__": 
    run_simulation()