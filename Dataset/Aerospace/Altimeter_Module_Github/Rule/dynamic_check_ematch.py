import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_ematch.json")
CIR_FILE = os.path.join(BASE_DIR, "ematch_pro_bench.net")
LOG_FILE = os.path.join(BASE_DIR, "ematch_pro_bench.log")
REPORT_FILE = os.path.join(BASE_DIR, "ematch_report.txt")

# Configuration for 15 key test points
TEST_POINTS_CONFIG = [
    {"id": "V_BATT_IN",    "min": 7.0,   "max": 8.0,   "name": "Battery Input Voltage"},
    {"id": "V_MCU_IN",     "min": 3.2,   "max": 3.4,   "name": "Logic Supply Voltage"},
    {"id": "V_G1_READY",   "min": 2.0,   "max": 7.5,   "name": "Q1 Gate Pre-on Voltage"},
    {"id": "V_OUT_READY",  "min": -0.1,  "max": 0.5,   "name": "Standby Output Low Level"},
    {"id": "V_PWM_FIRE",   "min": 3.0,   "max": 3.5,   "name": "Ignition Pulse Level"},
    {"id": "I_MATCH_PK",   "min": 3.4,   "max": 3.8,   "name": "Peak Ignition Current"},
    {"id": "V_Q2_VDS_ON",  "min": -0.1,  "max": 0.8,   "name": "Q2 Saturation Voltage Drop"},
    {"id": "P_MATCH_PK",   "min": 20.0,  "max": 30.0,  "name": "Peak Ignition Power (W)"},
    {"id": "V_G1_BURNED",  "min": -0.1,  "max": 0.6,   "name": "Q1 Gate Voltage Post-burn"},
    {"id": "V_OUT_BURNED", "min": 3.1,   "max": 3.4,   "name": "Burnout Alarm High Level"},
    {"id": "I_LEAK_POST",  "min": -1e-6, "max": 1e-5,  "name": "Post-off Quiescent Leakage"},
    {"id": "V_OUT_END",    "min": 3.2,   "max": 3.4,   "name": "Final Steady State Voltage"}
]

def build_netlist():
    if not os.path.exists(JSON_FILE): raise FileNotFoundError(f"Missing: {JSON_FILE}")
    with open(JSON_FILE, 'r', encoding='utf-8') as f: data = json.load(f)
    
    # --- 1. Map pins to Net IDs from JSON ---
    pins = {}
    for subsystem in data.values():
        for net in subsystem:
            net_id = net["net_id"]
            for conn in net["Connections"]:
                comp, pin = conn["ComponentID"], conn["PinName"]
                pins[f"{comp}:{pin}"] = net_id

    # Helper function: Handle pin naming variations (G/1, D/8, S/1-3, etc.)
    def get_net(comp, pin_list, default):
        for p in pin_list:
            if f"{comp}:{p}" in pins: return pins[f"{comp}:{p}"]
        return default

    # --- 2. Extract Key Net IDs ---
    net_q2_g = get_net("AO4406AL", ["G", "1"], "n_q2_g")
    net_q2_s = get_net("AO4406AL", ["S", "2", "3", "S"], "0") # Typically connected to GND
    net_sw   = "n_match_sw_node" # Acts as a bridge between e-match and MOSFET

    net_q1_g = get_net("AO3400", ["G", "1", "G"], "n_q1_g")
    net_q1_d = get_net("AO3400", ["D", "3", "D"], "n_continuity_out")
    net_q1_s = get_net("AO3400", ["S", "2", "S"], "0")

    # --- 3. Inject Netlist Template ---
    netlist = [
        "* Topo-Driven E-Match Deep Verification",
        ".tran 0 30m 0 1u",
        ".options numdgt=7",
        "V_BATT n_v_batt 0 7.4",
        "V_MCU  n_v_mcu  0 3.3",
        "V_FIRE net_fire_stim 0 PULSE(0 3.3 10m 1n 1n 5m)",
        "V_BURN net_burn_stim 0 PULSE(3.3 0 12m 1n 1n 100m)",

        # --- Power Stage Topology (Q2) ---
        f"M_Q2 {net_sw} {net_q2_g} {net_q2_s} {net_q2_s} MyNMOS",
        f"R_G2 net_fire_stim {net_q2_g} 510", # Gate resistor
        f"R_PD2 {net_q2_g} 0 10k",             # Pull-down resistor
        
        # --- Detection Stage Topology (Q1) ---
        f"M_Q1 {net_q1_d} {net_q1_g} {net_q1_s} {net_q1_s} MyNMOS",
        f"R_G1 {net_sw} {net_q1_g} 510",       # Sampling resistor
        f"R_PD1 {net_q1_g} 0 100k",            # Pull-down resistor
        f"R_PU n_v_mcu {net_q1_d} 100k",       # Pull-up resistor

        # --- Load and Burnout Simulation ---
        f"R_MATCH n_match_int {net_sw} 2",
        f"S_BURN n_v_batt n_match_int net_burn_stim 0 M_BURN",
        
        # --- Indicator Branch ---
        f"D_FIRE {net_sw} net_led_node MyDiode",
        f"R_LED net_led_node 0 510",

        ".model MyNMOS NMOS(Vto=2.1 Kp=10)",
        ".model MyDiode D(Vd=1.8)",
        ".model M_BURN SW(Vt=1.6 Vh=0.1 Ron=0.01 Roff=10Meg)",
        
        # --- 15 Measurement Commands ---
        ".meas TRAN V_BATT_IN FIND V(n_v_batt) AT 5m",
        ".meas TRAN V_MCU_IN  FIND V(n_v_mcu) AT 5m",
        f".meas TRAN V_G1_READY FIND V({net_q1_g}) AT 5m",
        f".meas TRAN V_OUT_READY FIND V({net_q1_d}) AT 5m",
        ".meas TRAN V_PWM_FIRE MAX V(net_fire_stim)",
        ".meas TRAN I_MATCH_PK MAX I(R_MATCH) FROM 10m TO 15m",
        f".meas TRAN V_Q2_VDS_ON FIND V({net_sw}) AT 11m",
        ".meas TRAN I_LED_FIRE MAX I(D_FIRE) FROM 10m TO 15m",
        f".meas TRAN P_MATCH_PK MAX V(n_match_int,{net_sw})*I(R_MATCH) FROM 10m TO 15m",
        ".meas TRAN T_IGNIT_DLY TRIG V(net_fire_stim)=1.65 RISE=1 TARG I(R_MATCH)=1.0 RISE=1",
        f".meas TRAN V_G1_BURNED FIND V({net_q1_g}) AT 25m",
        f".meas TRAN V_OUT_BURNED FIND V({net_q1_d}) AT 25m",
        f".meas TRAN T_SENSE_DLY TRIG V(net_burn_stim)=1.65 FALL=1 TARG V({net_q1_d})=1.65 RISE=1",
        ".meas TRAN I_LEAK_POST FIND I(S_BURN) AT 28m",
        f".meas TRAN V_OUT_END FIND V({net_q1_d}) AT 29m",
        ".end"
    ]
    return "\n".join(netlist)

def run_and_report():
    # 1. Run Simulation
    with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f: log = f.read()

    # 2. Parse results and generate report text
    report_lines = []
    report_lines.append("="*50)
    report_lines.append(f"E-Match Automated Simulation Report")
    report_lines.append(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"Topology Source: {os.path.basename(JSON_FILE)}")
    report_lines.append("-" * 50)
    report_lines.append(f"{'Test Item':<25} | {'Value':<12} | {'Result'}")
    report_lines.append("-" * 50)

    pass_count = 0
    for tp in TEST_POINTS_CONFIG:
        match = re.search(rf"{tp['id']}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
        val = float(match.group(1)) if match else float('nan')
        is_pass = tp['min'] <= val <= tp['max']
        if is_pass: pass_count += 1
        
        line = f"{tp['name']:<25} | {val:>12.4f} | {'PASS' if is_pass else 'FAIL'}"
        report_lines.append(line)
        print(line) # Output to console

    pass_rate = (pass_count / len(TEST_POINTS_CONFIG)) * 100
    footer = [
        "-" * 50,
        f"Summary: {pass_count}/{len(TEST_POINTS_CONFIG)} items passed",
        f"Pass Rate: {pass_rate:.2f}%",
        "="*50
    ]
    report_lines.extend(footer)
    for f_line in footer: print(f_line)

    # 3. Save to TXT file
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))
    print(f"\n[System] Report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    run_and_report()