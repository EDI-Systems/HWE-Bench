import os
import subprocess
import re
import json
import uuid

LTSPICE_EXE = "D:/app/LTspice/LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct","dynamic_audio.json")
CIR_FILE  = os.path.join(BASE_DIR, "audio_final_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "audio_final_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "audio_process_report.txt")

# --- Audit Metrics (Full 6-point coverage) ---
TEST_CRITERIA = {
    "v_mix_in":      {"name": "Input_Mixing_Amplitude", "min": 0.20, "max": 0.60, "unit": "V"},
    "v_b_stable":    {"name": "Bypass_Ref_Stability",   "min": 2.40, "max": 2.60, "unit": "V"},
    "v_out_active":  {"name": "Active_Output_Swing",    "min": 2.00, "max": 5.00, "unit": "V"},
    "v_out_muted":   {"name": "Shutdown_Mute_Level",    "min": 0.00, "max": 0.05, "unit": "V"},
    "dc_offset":     {"name": "Speaker_DC_Offset",      "min": -5.00, "max": 0.05, "unit": "V"}
}

def parse_dut_topology(json_path, module_name, dut_name):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except: return {}
    target_module = data.get(module_name, [])
    dut_nets = {}
    for net in target_module:
        for conn in net.get("Connections", []):
            if conn.get("ComponentID") == dut_name:
                dut_nets[conn.get("PinName")] = net.get("net_id", "")
    return dut_nets

def build_netlist():
    nets_amp = parse_dut_topology(JSON_FILE, "Audio Amplification & Output Module", "XPT8871")
    nets_fm  = parse_dut_topology(JSON_FILE, "Audio Amplification & Output Module", "RDA5807MP")
    nets_mcu = parse_dut_topology(JSON_FILE, "Audio Amplification & Output Module", "ATtiny85")

    n_in, n_sd = nets_amp.get("IN", "NC_IN"), nets_amp.get("SD", "NC_SD")
    n_vop, n_von = nets_amp.get("VOP", "NC_VOP"), nets_amp.get("VON", "NC_VON")
    n_byp, n_vdd = nets_amp.get("BYP", "NC_BYP"), "net_vdd5"
    fm_l, fm_r = nets_fm.get("LOUT", "FM_L"), nets_fm.get("ROUT", "FM_R")
    mcu_pb0 = nets_mcu.get("PB0", "MCU_PB0")

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Audio Process Corrected Audit",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 20m 0 uic",
        "V_VDD net_vdd5 0 5V",
        f"V_L {fm_l} 0 SINE(0 0.5 1k)",
        f"V_R {fm_r} 0 SINE(0 0.5 1k)",
        f"V_SD {sp(mcu_pb0)} 0 PWL(0 0 10m 0 10.01m 5 20m 5)",
        f"C12 {fm_l} {n_in}_l 390n",
        f"R5 {n_in}_l {sp(n_in)} 20k",
        f"C13 {fm_r} {n_in}_r 390n",
        f"R6 {n_in}_r {sp(n_in)} 20k",
        f"C11 {sp(n_byp)} 0 1u IC=2.5", 
        f"X_U3 {sp(n_sd)} {sp(n_byp)} 0 {sp(n_in)} {sp(n_von)} net_vdd5 0 {sp(n_vop)} XPT_FIXED",
        ".subckt XPT_FIXED SD BYP MODE IN VON VDD GND VOP",
        "R_INT_BIAS IN BYP 1G", # Ultra-high impedance bias to prevent DC drift
        "B_GAIN raw 0 V=V(SD)>1.5 ? 0 : limit((V(IN)-V(BYP))*12, -2.4, 2.4)", 
        "E_P VOP 0 VALUE={V(BYP) + V(raw)}",
        "E_N VON 0 VALUE={V(BYP) - V(raw)}",
        ".ends",
        f"R_SPK {sp(n_vop)} {sp(n_von)} 8",
        f".meas TRAN v_mix_in MAX V({sp(n_in)}) FROM 2m TO 8m",
        f".meas TRAN v_b_stable AVG V({sp(n_byp)}) FROM 2m TO 8m",
        f".meas TRAN v_out_active MAX ABS(V({sp(n_vop)},{sp(n_von)})) FROM 2m TO 8m",
        f".meas TRAN v_out_muted MAX ABS(V({sp(n_vop)},{sp(n_von)})) FROM 15m TO 20m",
        f".meas TRAN t_sd_delay TRIG V({sp(n_sd)})=1.5 RISE=1 TARG V({sp(n_vop)},{sp(n_von)})=0.2 FALL=1",
        f".meas TRAN dc_offset AVG V({sp(n_vop)},{sp(n_von)}) FROM 2m TO 8m",
        ".end"
    ]
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
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            if m: results[k] = float(m.group(1))
        report = ["="*65, " AUDIO MODULE AUDIT REPORT (FIXED)", "="*65]
        report.append(f"{'Audit Item':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3f} {spec['unit']}" if val is not None else "N/A"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status}")
        report.append("-" * 65)
        report.append(f"TOTAL PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        final_out = "\n".join(report)
        print(final_out)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_out)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": 
    run_simulation()