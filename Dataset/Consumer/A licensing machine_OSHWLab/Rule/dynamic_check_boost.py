import os
import subprocess
import re
import json
import datetime

# 1. Environment Configuration
LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_boost.json")
CIR_FILE  = os.path.join(BASE_DIR, "boost_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "boost_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "boost_audit_report.txt")

TEST_CRITERIA = {
    "v_in_steady":     {"name": "Input_Voltage_Steady",   "min": 7.4,   "max": 7.6,   "unit": "V"},
    "v_out_steady":    {"name": "Output_Voltage_Steady",  "min": 11.5,  "max": 12.5,  "unit": "V"},
    "v_fb_steady":     {"name": "Feedback_Voltage_Ref",   "min": 1.0,   "max": 1.15,  "unit": "V"},
    "v_sw_peak":       {"name": "SW_Node_Peak_Voltage",   "min": 12.0,  "max": 15.0,  "unit": "V"},
    "v_out_ripple":    {"name": "Output_Voltage_Ripple",  "min": 0.0,   "max": 0.2,   "unit": "V"}
}

def get_topology():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError("JSON File not found.")
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("High-Efficiency Inductive Transformation and Precision Regulation Module", [])
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

    n_in  = fetch("SX1308", "VIN")[0]
    n_sw  = fetch("SX1308", "SW")[0]
    n_fb  = fetch("SX1308", "FB")[0]
    n_gnd = fetch("SX1308", "GND")[0]
    n_out = fetch("SS54A", "K")[0]
    n_dio_a = fetch("SS54A", "A")[0]

    def sp(n): return "0" if n == n_gnd else n

    netlist = [
        "* SX1308 Boost Converter Behavioral Audit",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 10n 2m 0 uic",
        
        "* Testbench Power Supply (7.5V Input)",
        f"V_IN {sp(n_in)} 0 7.5V",
        
        "* Testbench External Components",
        f"L1 {sp(n_in)} {sp(n_sw)} 4.7uH",
        f"D2 {sp(n_dio_a)} {sp(n_out)} D_SS54A",
        f"C7 {sp(n_out)} 0 22uF IC=7.5V",
        f"R4 {sp(n_out)} {sp(n_fb)} 100K",
        f"R6 {sp(n_fb)} 0 10K",
        f"R_LOAD {sp(n_out)} 0 120",
        
        "* Schottky Diode Model",
        ".model D_SS54A D(Is=10u Rs=0.05 N=1.2 Cjo=200p tt=5n)",
        
        "* SX1308 Behavioral Macro Model",
        f"X_SX1308 {sp(n_sw)} 0 {sp(n_fb)} {sp(n_in)} {sp(n_in)} SX1308_MACRO",
        ".subckt SX1308_MACRO SW GND FB EN VIN",
        "Vosc osc 0 PULSE(0 1 0 10n 10n 400n 833n)",
        "B_ea ea 0 V=limit((1.09 - V(FB))*20, 0, 0.95)",
        "B_pwm pwm 0 V=V(osc)<V(ea) & V(EN)>1 ? 1 : 0",
        "S1 SW GND pwm 0 SW_MOD",
        ".model SW_MOD SW(Ron=0.1 Roff=1Meg Vt=0.5 Vh=-0.1)",
        ".ends",
        
        "* Automated Measurements",
        f".meas TRAN v_in_steady AVG V({sp(n_in)}) FROM 1.5m TO 2.0m",
        f".meas TRAN v_out_steady AVG V({sp(n_out)}) FROM 1.5m TO 2.0m",
        f".meas TRAN v_fb_steady AVG V({sp(n_fb)}) FROM 1.5m TO 2.0m",
        f".meas TRAN v_sw_peak MAX V({sp(n_sw)}) FROM 1.5m TO 2.0m",
        f".meas TRAN v_out_max MAX V({sp(n_out)}) FROM 1.5m TO 2.0m",
        f".meas TRAN v_out_min MIN V({sp(n_out)}) FROM 1.5m TO 2.0m",
        ".meas TRAN v_out_ripple PARAM v_out_max-v_out_min",
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
        report_lines.append(f"{'Audit Item':<30} | {'Value':<15} | {'Status'}")
        report_lines.append("---------------------------------------------------------")

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results.get(k)
            is_ok = spec["min"] <= val <= spec["max"] if val is not None else False
            if is_ok: 
                pass_count += 1
            status = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>11.3f} {spec['unit']}" if val is not None else "N/A"
            report_lines.append(f"{spec['name']:<30} | {val_str:<15} | {status}")

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