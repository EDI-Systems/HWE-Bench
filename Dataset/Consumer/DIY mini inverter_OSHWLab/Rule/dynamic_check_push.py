import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_push.json")
CIR_FILE    = os.path.join(BASE_DIR, "push_pull_audit.net")
LOG_FILE    = os.path.join(BASE_DIR, "push_pull_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "push_pull_report_audit.txt")

# ================= 2. 10 Strict Audit Criteria =================
TEST_CRITERIA = {
    "v_hvdc":       {"name": "01_HVDC_Output",        "min": 250.0, "max": 360.0, "unit": "V"},
    "v_ripple":     {"name": "02_HVDC_Ripple",        "min": 0.0,   "max": 5.0,   "unit": "V"},
    "eff":          {"name": "03_Power_Efficiency",   "min": 0.70,  "max": 0.98,  "unit": "ratio"},
    "p_out":        {"name": "04_Output_Power",       "min": 200.0, "max": 400.0, "unit": "W"},
    "v_ds_peak":    {"name": "05_Drain_Voltage_Peak", "min": 24.0,  "max": 160.0, "unit": "V"},
    "v_gs_q6":      {"name": "06_Gate_Drive_Q6",      "min": 8.0,   "max": 12.0,  "unit": "V"},
    "v_gs_q8":      {"name": "07_Gate_Drive_Q8",      "min": 8.0,   "max": 12.0,  "unit": "V"},
    "i_peak_pri":   {"name": "08_Primary_Peak_Curr",  "min": 10.0,  "max": 60.0,  "unit": "A"},
    "i_batt_avg":   {"name": "09_Battery_Avg_Curr",   "min": 20.0,  "max": 40.0,  "unit": "A"},
    "v_sec_peak":   {"name": "10_Secondary_Peak_AC",  "min": 250.0, "max": 450.0, "unit": "V"}
}

def get_topology_map():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"JSON file not found: {JSON_FILE}")
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("High Voltage DC Generation (Push-Pull Converter)", [])
    pin_to_nets = {}
    for net in target:
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            if key not in pin_to_nets:
                pin_to_nets[key] = []
            pin_to_nets[key].append(net["net_id"])
            
    def fetch_nets(comp, pin, debug_name):
        result = []
        for k, nets in pin_to_nets.items():
            if comp in k and f":{pin}" in k:
                result.extend(nets)
                
        if not result:
            nc = f"NC_{uuid.uuid4().hex[:4]}"
            return [nc]
        return result
        
    return fetch_nets

def build_netlist():
    print("\n" + "-"*65)
    print(">>> Scanning JSON pin topology, building 10-point depth audit netlist...")
    fetch_nets = get_topology_map()

    # Extract nets
    pwm_a = fetch_nets("SG3525A", "Output A", "Control_PWM_A")
    pwm_b = fetch_nets("SG3525A", "Output B", "Control_PWM_B")
    batt  = fetch_nets("MR30PB", "Pin 3", "Battery_Pos_12V")
    hvdc  = fetch_nets("ES3GF", "K", "Rectifier_Output_HVDC")
    
    gnd_nets = fetch_nets("78L05", "GND", "System_Common_GND") + fetch_nets("SG3525A", "Ground", "Controller_GND")
    
    mos_g = fetch_nets("NCEP60T12A", "G", "MOSFET_Gate")
    n_g1 = pwm_a[0] if pwm_a[0] in mos_g else f"NC_{uuid.uuid4().hex[:4]}"
    n_g2 = pwm_b[0] if pwm_b[0] in mos_g else f"NC_{uuid.uuid4().hex[:4]}"
    
    mos_d = fetch_nets("NCEP60T12A", "D", "MOSFET_Drain")
    n_d1 = mos_d[0] if len(mos_d) > 0 else f"NC_{uuid.uuid4().hex[:4]}"
    n_d2 = mos_d[1] if len(mos_d) > 1 else f"NC_{uuid.uuid4().hex[:4]}"

    mos_s = fetch_nets("NCEP60T12A", "S", "MOSFET_Source")
    n_s1 = mos_s[0] if len(mos_s) > 0 else f"NC_{uuid.uuid4().hex[:4]}"
    n_s2 = mos_s[1] if len(mos_s) > 1 else n_s1
    
    print("✅ JSON topology extracted. Constructing netlist...")
    print("-" * 65 + "\n")

    def sp(name): return "0" if name in gnd_nets else name

    netlist = [
        "* Ultimate 10-Point Push-Pull Topology Audit",
        
        ".model N_PWR VDMOS(Vto=3.5 Rs=0.012 Kp=20 Cgdmax=2n Cjo=3n BV=150 mtriodes=1)",
        ".model D_FAST D(Is=1e-12 Rs=0.05 N=1.2)",
        ".options abstol=1u reltol=0.01 vntol=1m plotwinsize=0 cshunt=10p method=gear",
        
        # Capture steady-state data to accelerate simulation
        ".tran 1u 40m 35m uic",
        
        f"V_BATT {sp(batt[0])} 0 12V",
        f"V_PWM_A {sp(pwm_a[0])} 0 PULSE(0 9.5 0 100n 100n 8u 20u)",
        f"V_PWM_B {sp(pwm_b[0])} 0 PULSE(0 9.5 10u 100n 100n 8u 20u)",
        
        f"M_Q6 {sp(n_d1)} {sp(n_g1)} {sp(n_s1)} N_PWR",
        f"M_Q8 {sp(n_d2)} {sp(n_g2)} {sp(n_s2)} N_PWR",
        
        # RC Snubber Circuits
        f"R_SN1 {sp(n_d1)} N_SN1 100", f"C_SN1 N_SN1 {sp(n_s1)} 1n",
        f"R_SN2 {sp(n_d2)} N_SN2 100", f"C_SN2 N_SN2 {sp(n_s2)} 1n",
        
        # Transformer
        f"L_P1 {sp(batt[0])} {sp(n_d1)} 50uH Rser=0.01",
        f"L_P2 {sp(n_d2)} {sp(batt[0])} 50uH Rser=0.01", 
        "L_S1 HV_1 0 45mH Rser=0.1",
        "L_S2 0 HV_2 45mH Rser=0.1",
        "K_ALL L_P1 L_P2 L_S1 L_S2 0.996",
        
        # Output and Load
        f"D2 HV_1 {sp(hvdc[0])} D_FAST",
        f"D3 HV_2 {sp(hvdc[0])} D_FAST",
        f"C_FILTER {sp(hvdc[0])} 0 22uF",
        f"R_LOAD {sp(hvdc[0])} 0 300", 
        
        # ================= 10 Strict Measurement Instructions =================
        f".meas TRAN v_hvdc AVG V({sp(hvdc[0])})",
        f".meas TRAN v_hvdc_max MAX V({sp(hvdc[0])})",
        f".meas TRAN v_hvdc_min MIN V({sp(hvdc[0])})",
        f".meas TRAN p_out AVG V({sp(hvdc[0])})*I(R_LOAD)",
        f".meas TRAN p_in AVG -V({sp(batt[0])})*I(V_BATT)",
        f".meas TRAN v_ds_peak MAX V({sp(n_d1)})",
        f".meas TRAN v_gs_q6 MAX V({sp(n_g1)})",
        f".meas TRAN v_gs_q8 MAX V({sp(n_g2)})",
        f".meas TRAN i_peak_pri MAX I(L_P1)",
        f".meas TRAN i_batt_avg AVG -I(V_BATT)",
        f".meas TRAN v_sec_peak MAX V(HV_1)",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
        
        print(">>> Executing Push-Pull 10-point topology audit simulation...")
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=45)
        
        if not os.path.exists(LOG_FILE): return
        with open(LOG_FILE, 'r', errors='ignore') as f: log_raw = f.read()

        # Extract all base data
        vals = {}
        extract_keys = ["v_hvdc", "v_hvdc_max", "v_hvdc_min", "p_out", "p_in", 
                        "v_ds_peak", "v_gs_q6", "v_gs_q8", "i_peak_pri", "i_batt_avg", "v_sec_peak"]
        
        for key in extract_keys:
            match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log_raw, re.I)
            vals[key] = float(match.group(1)) if match else None
            
        # Safe calculation of efficiency and ripple
        if vals.get("v_hvdc_max") is not None and vals.get("v_hvdc_min") is not None:
            vals["v_ripple"] = vals["v_hvdc_max"] - vals["v_hvdc_min"]
        else:
            vals["v_ripple"] = None

        if vals.get("p_in") and vals["p_in"] > 0 and vals.get("p_out"):
            vals["eff"] = vals["p_out"] / vals["p_in"]
        else:
            vals["eff"] = None

        # Build report content
        report_lines = []
        report_lines.append("="*80)
        report_lines.append(f" 🚀 Push-Pull 10-Point Topology Audit Report | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("="*80)
        report_lines.append(f"{'Audit Item':<25} | {'Measured Value':<15} | {'Status'}")
        report_lines.append("-" * 80)

        pass_count = 0
        for key, spec in TEST_CRITERIA.items():
            val = vals.get(key)
            if val is not None:
                is_ok = spec["min"] <= val <= spec["max"]
                status = "✅ PASS" if is_ok else "❌ FAIL"
                if is_ok: pass_count += 1
                val_str = f"{val:>10.3f} {spec['unit']}"
            else:
                status = "❌ FAIL (Simulation Abort)"; val_str = "0.000"
            
            report_lines.append(f"{spec['name']:<25} | {val_str:<15} | {status}")
        
        report_lines.append("-" * 80)
        compliance_rate = (pass_count/len(TEST_CRITERIA))*100
        report_lines.append(f"📊 Audit Conclusion: JSON physical compliance rate is {compliance_rate:.1f}%")
        report_lines.append("="*80)
        
        final_report = "\n".join(report_lines)
        
        # Print to terminal
        print("\n" + final_report)
        
        # Save to TXT file
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_report)
        print(f"\n✅ Test results successfully saved to: {REPORT_FILE}")

        if vals.get("v_hvdc") is None:
            print("⚠️ Diagnosis: LTspice produced no data. If JSON is aligned, please check engine status.")

    except Exception as e:
        print(f"\nSimulation Exception: {e}")

if __name__ == "__main__":
    run_simulation()