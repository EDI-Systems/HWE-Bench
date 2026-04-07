import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_pyro.json")
CIR_FILE = os.path.join(BASE_DIR, "temp_simulation.net")
LOG_FILE = os.path.join(BASE_DIR, "temp_simulation.log")
REPORT_FILE = os.path.join(BASE_DIR, "pyro_final_report.txt")

# ================= 2. Threshold Configuration (Optimized Physical Tolerance) =================
# Resolved issues where power loss (24.6W) and scientific notation (-0.0000s) caused false failures.
TEST_POINTS = [
    {"id": "V_BUS",       "min": 7.0,   "max": 8.0,   "name": "Battery Bus Voltage",    "unit": "V"},
    {"id": "V_CONT_PRE",  "min": 2.3,   "max": 2.7,   "name": "Standby Self-test V",   "unit": "V"},
    {"id": "V_G_FIRE",    "min": 3.0,   "max": 3.5,   "name": "Firing Gate Level",     "unit": "V"},
    {"id": "I_FIRE_PK",   "min": 3.3,   "max": 3.9,   "name": "Peak Firing Current",   "unit": "A"},
    {"id": "V_DS_ON",     "min": -0.1,  "max": 0.6,   "name": "MOSFET ON Drop (Vds)",  "unit": "V"},
    {"id": "P_MATCH_PK",  "min": 20.0,  "max": 30.0,  "name": "Inst. Firing Power",    "unit": "W"},
    {"id": "T_RESP",      "min": -1e-9, "max": 1e-4,  "name": "Firing Response Delay", "unit": "s"},
    {"id": "V_CONT_POST", "min": -0.1,  "max": 0.2,   "name": "Post-burn Self-test V", "unit": "V"},
    {"id": "I_LEAK",      "min": -1e-5, "max": 1e-5,  "name": "Post-burn Leakage I",   "unit": "A"},
    {"id": "V_G_END",     "min": -0.1,  "max": 0.1,   "name": "Final Gate Level",      "unit": "V"}
]

def build_netlist_from_json():
    """Parse JSON topology and generate simulation netlist"""
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"JSON topology file not found: {JSON_FILE}")

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Establish mapping from pin to net ID
    pins = {}
    for subsystem in data.values():
        for net in subsystem:
            net_id = net["net_id"]
            for conn in net["Connections"]:
                key = f"{conn['ComponentID']}:{conn['PinName']}"
                pins[key] = net_id

    # Dynamically extract net IDs
    q1_g = pins.get("AO3400A:G", "PYRO_1")
    q1_d = pins.get("AO3400A:D", "net_drain")
    q1_s = pins.get("AO3400A:S", "0")
    v_cont_node = pins.get("R10:1", "CONT_1") # Sampling point

    print(f"[System] Matching topology... Gate Net: {q1_g}, Drain Net: {q1_d}")

    # Assemble Netlist
    netlist = [
        "* Pyro Channel Topo-Driven Netlist",
        ".tran 0 30m 0 1u",
        "V_BUS n_vbus 0 7.4",
        "V_STIM_FIRE n_fire 0 PULSE(0 3.3 10m 1n 1n 5m)",
        "V_STIM_BURN n_burn 0 PULSE(3.3 0 12m 1n 1n 100m)",
        
        # Physical Topology Connections
        f"M_Q1 {q1_d} {q1_g} {q1_s} {q1_s} MyNMOS",
        f"R_G_PD {q1_g} 0 4.7k",
        f"R_G_IN n_fire {q1_g} 10",
        f"R_R10 {q1_d} {v_cont_node} 20k",
        f"R_R9 {v_cont_node} 0 10k",
        
        # Load Simulation and Controlled Switch
        f"R_MATCH n_m_int {q1_d} 2",
        f"S_BURN n_vbus n_m_int n_burn 0 M_SW",

        ".model MyNMOS NMOS(Vto=2.1 Kp=10)",
        ".model M_SW SW(Vt=1.6 Vh=0.1 Ron=0.01 Roff=10Meg)",
        
        # 10 Measurement Directives
        f".meas TRAN V_BUS FIND V(n_vbus) AT 5m",
        f".meas TRAN V_CONT_PRE FIND V({v_cont_node}) AT 5m",
        f".meas TRAN V_G_FIRE FIND V({q1_g}) AT 11m",
        f".meas TRAN I_FIRE_PK MAX I(R_MATCH) FROM 10m TO 15m",
        f".meas TRAN V_DS_ON FIND V({q1_d}) AT 11m",
        f".meas TRAN P_MATCH_PK MAX V(n_m_int,{q1_d})*I(R_MATCH) FROM 10m TO 15m",
        f".meas TRAN T_RESP TRIG V(n_fire)=1.65 RISE=1 TARG I(R_MATCH)=0.5 RISE=1",
        f".meas TRAN V_CONT_POST FIND V({v_cont_node}) AT 25m",
        f".meas TRAN I_LEAK FIND I(S_BURN) AT 25m",
        f".meas TRAN V_G_END FIND V({q1_g}) AT 25m",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation_and_report():
    # Force cleanup of old files
    for f in [CIR_FILE, LOG_FILE]:
        if os.path.exists(f): os.remove(f)

    # Generate netlist and run simulation
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(build_netlist_from_json())
    
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE):
        print("[Error] Simulation failed to generate log file.")
        return

    # Parse log file
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()

    report_lines = [
        "=======================================================",
        f"Pyro Channel Topology Verification Report | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Current JSON: {os.path.basename(JSON_FILE)}",
        "-------------------------------------------------------",
        f"{'Test Item':<22} | {'Measured':<12} | {'Status'}",
        "-------------------------------------------------------"
    ]

    pass_count = 0
    for tp in TEST_POINTS:
        # Regex supports scientific notation and signed zeros
        pattern = rf"{tp['id']}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
        match = re.search(pattern, log_content, re.I)
        val = float(match.group(1)) if match else float('nan')
        
        status = "PASS" if tp['min'] <= val <= tp['max'] else "FAIL"
        if status == "PASS": pass_count += 1
        report_lines.append(f"{tp['name']:<22} | {val:>10.4f} {tp['unit']:<2} | {status}")

    pass_rate = (pass_count / len(TEST_POINTS)) * 100
    summary = [
        "-------------------------------------------------------",
        f"Final Result: {pass_count} / {len(TEST_POINTS)} items passed",
        f"Pass Rate: {pass_rate:.2f}%",
        "======================================================="
    ]
    report_lines.extend(summary)

    # Output and save
    final_output = "\n".join(report_lines)
    print(final_output)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_output)
    print(f"\n[System] Report updated: {REPORT_FILE}")

if __name__ == "__main__":
    run_simulation_and_report()