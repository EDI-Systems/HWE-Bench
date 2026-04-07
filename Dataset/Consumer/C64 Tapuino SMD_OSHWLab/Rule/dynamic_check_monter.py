import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_shifter.json")
CIR_FILE = os.path.join(BASE_DIR, "motor_opto_sim.net")
LOG_FILE = os.path.join(BASE_DIR, "motor_opto_sim.log")
REPORT_FILE = os.path.join(BASE_DIR, "motor_report.txt")

TEST_POINTS = [
    {"id": "V_MCU_HI",     "min": 4.8,   "max": 5.2,   "name": "MCU PD3 Drive High Level", "unit": "V"},
    {"id": "I_LED_DRV",    "min": 7.5e-3,"max": 8.5e-3,"name": "LED Drive Current (R2=470R)", "unit": "A"},
    {"id": "V_MCU_HI_OUT", "min": 4.5,   "max": 5.1,   "name": "MCU-side Cut-off High Level", "unit": "V"},
    {"id": "T_PROP_DELAY", "min": -1e-8, "max": 2e-5,  "name": "Optocoupler Propagation Delay", "unit": "s"},
    {"id": "P_R2_LOSS",    "min": 0.02,  "max": 0.04,  "name": "Resistor R2 Power Loss", "unit": "W"},
    {"id": "V_GND_REF",    "min": -0.1,  "max": 0.1,   "name": "System Ground Ref Potential", "unit": "V"}
]

def build_netlist():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("Motor Signal Converter with Optoisolation", [])
    pins = {f"{c['ComponentID']}:{c['PinName']}": n['net_id'] for n in target for c in n['Connections']}

    n_mcu   = pins.get("ATmega328p:PD3", "MCU_DRIVE_PD3")
    n_anode = pins.get("PC817:Anode", "OPTO_LED_ANODE")
    n_cath  = pins.get("PC817:Cathode", "GND")
    n_coll  = pins.get("PC817:Collector", "MCU_MOTOR_SENSE") 
    n_emit  = pins.get("PC817:Emitter", "GND")
    n_gnd   = pins.get("AMS1117:GND/ADJ", "GND")

    # --- Core Interceptor: Check if node is Ground ---
    def is_gnd(node_name):
        return node_name.upper() in ["GND", "0"]

    netlist = [
        "* Tapuino Motor Signal Converter Final Verify",
        ".subckt PC817_Exact 1 2 4 3",
        "D1 1 2 LED_Model",
        "G1 4 3 1 2 2.0", 
        ".model LED_Model D(Is=1e-14 N=1.5 Rs=0.1)",
        ".ends PC817_Exact",
        
        ".tran 0 50m 0 100u",
        
        f"V_MCU {n_mcu} 0 PULSE(0 5 1m 1n 1n 10m 20m)",
        f"R2 {n_mcu} {n_anode} 470",
        
        f"XU3 {n_anode} {n_cath} {n_coll} {n_emit} PC817_Exact",
        
        f"V_ISO VCC_ISO 0 5",
        f"R_PULLUP VCC_ISO {n_coll} 10k"
    ]

    # Safely bind reference points
    if not is_gnd(n_cath):
        netlist.append(f"V_CATH_TIE {n_cath} 0 0")
    if not is_gnd(n_gnd):
        netlist.append(f"V_GND_TIE {n_gnd} 0 0")

    # --- Smart Measurement Command Generation ---
    netlist.append(f".meas TRAN V_MCU_HI MAX V({n_mcu})")
    
    if is_gnd(n_cath):
        netlist.append(f".meas TRAN V_LED_DROP AVG V({n_anode}) FROM 5m TO 6m")
    else:
        netlist.append(f".meas TRAN V_LED_DROP AVG V({n_anode})-V({n_cath}) FROM 5m TO 6m")

    netlist.append(f".meas TRAN I_LED_DRV AVG I(R2) FROM 5m TO 6m")
    netlist.append(f".meas TRAN V_MCU_LO MIN V({n_coll}) FROM 5m TO 6m")
    netlist.append(f".meas TRAN V_MCU_HI_OUT MAX V({n_coll}) FROM 15m TO 16m")
    netlist.append(f".meas TRAN T_PROP_DELAY TRIG V({n_mcu})=2.5 RISE=1 TARG V({n_coll})=2.5 FALL=1")
    netlist.append(f".meas TRAN P_R2_LOSS AVG (V({n_mcu})-V({n_anode}))*I(R2) FROM 5m TO 6m")
    netlist.append(f".meas TRAN CTR_REAL PARAM abs(I(R_PULLUP)/I(R2))") 
    
    if is_gnd(n_gnd):
        netlist.append(f".meas TRAN V_GND_REF PARAM 0")
    else:
        netlist.append(f".meas TRAN V_GND_REF AVG V({n_gnd})")
        
    netlist.append(f".meas TRAN I_OUT_SAT AVG I(R_PULLUP) FROM 5m TO 6m")
    netlist.append(".end")

    return "\n".join(netlist)

def run_and_report():
    # Generate netlist and force simulation execution
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(build_netlist())
    
    print(f">>> Reading JSON topology and executing Tapuino simulation verification...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE):
        print("[Error] Simulation failed to generate log.")
        return

    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log = f.read()

    # Report generation logic
    report = [
        "=======================================================",
        f"Tapuino Motor Signal Converter Verification Report | {datetime.now().strftime('%Y-%m-%d')}",
        "-------------------------------------------------------",
        f"{'Test Item':<25} | {'Measured':<12} | {'Verdict'}"
    ]

    pass_count = 0
    for tp in TEST_POINTS:
        match = re.search(rf"{tp['id']}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
        val = float(match.group(1)) if match else float('nan')
        status = "PASS" if tp['min'] <= val <= tp['max'] else "FAIL"
        if status == "PASS": pass_count += 1
        unit = tp.get('unit', '')
        report.append(f"{tp['name']:<25} | {val:>10.4f} {unit:<2} | {status}")

    report.append("-------------------------------------------------------")
    report.append(f"Final Result: {pass_count} / {len(TEST_POINTS)} items passed")
    report.append(f"Pass Rate: {pass_count/len(TEST_POINTS)*100:.2f}%")
    report.append("=======================================================")

    final_report = "\n".join(report)
    print(final_report)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_report)

if __name__ == "__main__":
    try:
        run_and_report()
    except Exception as e:
        print(f"[Fatal Error] Simulation execution failed: {e}")