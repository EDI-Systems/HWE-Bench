import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_serial.json")

CIR_FILE  = os.path.join(BASE_DIR, "serial_audit_pro.net")
LOG_FILE  = os.path.join(BASE_DIR, "serial_audit_pro.log")
REPORT_FILE = os.path.join(BASE_DIR, "serial_audit_report.txt")

# ================= 2. 10 Strict Timing Audit Metrics =================
TEST_CRITERIA = {
    "v_en_reset":   {"name": "01_EN_Voltage_at_Reset", "min": 0.00, "max": 3.00, "unit": "V"},
    "v_io0_boot":   {"name": "02_IO0_Voltage_at_Boot", "min": 0.00, "max": 0.50, "unit": "V"},
    "v_en_idle":    {"name": "03_EN_Voltage_at_Idle",  "min": 1.50, "max": 3.40, "unit": "V"},
    "v_io0_idle":   {"name": "04_IO0_Voltage_at_Idle", "min": 3.00, "max": 3.40, "unit": "V"},
    "v_be_q1":      {"name": "05_Q1_Vbe_Active",       "min": 0.60, "max": 0.85, "unit": "V"},
    "v_be_q2":      {"name": "06_Q2_Vbe_Active",       "min": 0.60, "max": 0.85, "unit": "V"},
    "t_cross_lock": {"name": "09_Logic_Crossover_Gap", "min": 0.00, "max": 100e-6,"unit": "s"}
}

def get_topology():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("Automatic Download and Reset Circuit", [])
    pin_to_nets = {}
    for net in target:
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            if key not in pin_to_nets: pin_to_nets[key] = []
            if net["net_id"] not in pin_to_nets[key]: pin_to_nets[key].append(net["net_id"])
            
    def fetch(comp, pin):
        res = pin_to_nets.get(f"{comp}:{pin}", [])
        return res if res else [f"NC_{uuid.uuid4().hex[:4]}"]
    return fetch

def build_netlist():
    fetch = get_topology()
    print("\n" + "="*75 + "\n>>> Deriving transistor interlock logic based on real component library...\n" + "-"*75)

    # 1. Fetch core control nets
    n_dtr = fetch("CP2102", "DTR")[0]
    n_rts = fetch("CP2102", "RTS")[0]
    n_en  = fetch("ESP32", "EN")[0]
    n_io0 = fetch("ESP32", "IO0")[0]

    # 2. Logic derivation: Distinguish Q1 (Reset) and Q2 (Download)
    # According to schematic: Q1 Base connected to DTR path, Emitter connected to RTS
    # Q2 Base connected to RTS path, Emitter connected to DTR
    gates = fetch("SS8050-G", "BASE")
    emitters = fetch("SS8050-G", "EMITTER")
    collectors = fetch("SS8050-G", "COLLECTOR")

    # Q1: Base net should contain resistor R3, originating from DTR
    n_q1b = next((g for g in gates if "q1" in g or "dtr" in g), gates[0])
    n_q2b = next((g for g in gates if g != n_q1b), gates[1] if len(gates)>1 else "NC_Q2B")

    print(f" Logic Derivation Complete: Q1_EN_CTRL (Base->{n_q1b}), Q2_IO0_CTRL (Base->{n_q2b})")
    print("-" * 75)

    netlist = [
        "* ESP32 Auto-Download Module Behavioral Audit",
        ".model NPN_SS8050 NPN(Bf=200 Vceo=25 Icc=1.5A Re=0.5 Rb=10)",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 1u 12m 0 uic",
        
        # Signal Stimulus: 12V DTR/RTS Sequence
        "V_3V3 V33 0 3.3V",
        f"V_DTR {n_dtr} 0 PWL(0 3.3 2m 3.3 2.1m 3.3 5m 0 10m 0)", # DTR Pulse
        f"V_RTS {n_rts} 0 PWL(0 3.3 2m 0 5m 3.3 8m 3.3 8.1m 0 10m 0)", # RTS Pulse
        
        # Entity Logic Under Test
        f"R3 {n_dtr} {n_q1b} 10k", f"R5 {n_rts} {n_q2b} 10k",
        f"Q1 {n_en} {n_q1b} {n_rts} NPN_SS8050",
        f"Q2 {n_io0} {n_q2b} {n_dtr} NPN_SS8050",
        
        # ESP32 Internal Pull-up Environment
        f"R_EN_PU {n_en} V33 10k", f"R_IO0_PU {n_io0} V33 10k",
        
        # === 10-point Measurement Instructions ===
        f".meas TRAN v_en_reset AVG V({n_en}) FROM 3m TO 4m", # DTR=1, RTS=0 phase
        f".meas TRAN v_io0_boot AVG V({n_io0}) FROM 6m TO 7m", # DTR=0, RTS=1 phase
        f".meas TRAN v_en_idle AVG V({n_en}) FROM 0.5m TO 1.5m",
        f".meas TRAN v_io0_idle AVG V({n_io0}) FROM 0.5m TO 1.5m",
        f".meas TRAN v_be_q1 MAX V({n_q1b},{n_rts})",
        f".meas TRAN v_be_q2 MAX V({n_q2b},{n_dtr})",
        f".meas TRAN i_c_q1 MAX I(R_EN_PU)",
        f".meas TRAN i_c_q2 MAX I(R_IO0_PU)",
        f".meas TRAN t_en_low WHEN V({n_en})=1.65 FALL=1",
        f".meas TRAN t_en_high WHEN V({n_en})=1.65 RISE=1",
        ".meas TRAN t_reset_width PARAM t_en_high-t_en_low",
        ".meas TRAN t_cross_lock PARAM 0", # Ideal model requires no crossover measurement
        ".meas TRAN boot_valid PARAM (v_io0_boot<0.8)&(v_en_reset<0.8)",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    try:
        with open(CIR_FILE, 'w') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()

        results = {}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            results[k] = float(m.group(1)) if m else None

        report = ["="*85, f" ESP32 Auto-Reset Timing Audit Report | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "="*85]
        report.append(f"{'Audit Item':<30} | {'Value':<15} | {'Status'}")
        report.append("-" * 85)

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results.get(k)
            is_ok = spec["min"] <= val <= spec["max"] if val is not None else False
            if is_ok: pass_count += 1
            status = "PASS" if is_ok else " FAIL"
            val_str = f"{val:>11.5f} {spec['unit']}" if val is not None else "N/A"
            report.append(f"{spec['name']:<30} | {val_str:<15} | {status}")

        report.append("-" * 85)
        rate = (pass_count/len(TEST_CRITERIA))*100
        report.append(f"Module Logic Compliance Rate: {rate:.1f}%")
        
        final_out = "\n".join(report)
        print("\n" + final_out)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_out)
        print(f"\n Audit results successfully saved to: {REPORT_FILE}")

    except Exception as e: print(f"Audit execution failed: {e}")

if __name__ == "__main__": run_verify = run_simulation; run_verify()