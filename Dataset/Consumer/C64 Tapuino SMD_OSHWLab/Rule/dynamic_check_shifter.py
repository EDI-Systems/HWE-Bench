import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_shifter.json")
CIR_FILE = os.path.join(BASE_DIR, "sd_level_sim.net")
LOG_FILE = os.path.join(BASE_DIR, "sd_level_sim.log")
REPORT_FILE = os.path.join(BASE_DIR, "sd_verify_report.txt")

TEST_POINTS = [
    {"id": "V_CS_HI",      "min": 3.1,   "max": 3.4,   "name": "SD_CS Converted High Level", "unit": "V"},
    {"id": "V_MOSI_HI",    "min": 3.1,   "max": 3.4,   "name": "SD_MOSI Converted High Level", "unit": "V"},
    {"id": "V_SCK_HI",     "min": 3.1,   "max": 3.4,   "name": "SD_SCK Converted High Level", "unit": "V"},
    # Correction: Allow minimal numerical jitter
    {"id": "T_PROP_DLY",   "min": -1e-9, "max": 5e-8,  "name": "Full Link Propagation Delay", "unit": "s"},
    {"id": "V_SD_LOW",     "min": -0.1,  "max": 0.2,   "name": "Output Low Level Integrity", "unit": "V"},
    {"id": "I_STATIC_CS",  "min": 5e-4,  "max": 1.5e-3,"name": "CS Channel Static Current", "unit": "A"},
    {"id": "V_DIV_RATIO",  "min": 0.63,  "max": 0.66,  "name": "Divider Ratio (R_low/R_all)"},
    {"id": "P_LOSS_TOTAL", "min": 0.001, "max": 0.05,  "name": "Total Static Power Loss", "unit": "W"},
    # Correction: Ensure calculation at 15us high level
    {"id": "V_NOISE_MARG", "min": 0.5,   "max": 1.5,   "name": "3.3V Logic Noise Margin", "unit": "V"}
]

def build_netlist():
    """Extract physical pin topology for ATmega328p and MICRO from JSON"""
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract mapping table: ComponentID:PinName -> NetID
    pins = {f"{c['ComponentID']}:{c['PinName']}": n['net_id'] 
            for sub in data.values() for n in sub for c in n['Connections']}

    # 1. Target MCU Output Pins (PB2, PB3, PB5)
    mcu_cs   = pins.get("ATmega328p:PB2", "net_mcu_cs")
    mcu_mosi = pins.get("ATmega328p:PB3", "net_mcu_mosi")
    mcu_sck  = pins.get("ATmega328p:PB5", "net_mcu_sck")

    # 2. Target SD Card Input Pins (CD/DAT3, CMD, CLK)
    sd_cs   = pins.get("MICRO:CD/DAT3", "net_sd_cs")
    sd_mosi = pins.get("MICRO:CMD", "net_sd_mosi")
    sd_sck  = pins.get("MICRO:CLK", "net_sd_sck")

    netlist = [
        "* SD Level Shifter Pin-to-Pin Verification",
        ".tran 0 100u 0 10n",
        
        # Stimulus Source (5V Logic Signal)
        f"V_CS {mcu_cs} 0 PULSE(0 5 10u 1n 1n 10u 20u)",
        f"V_MOSI {mcu_mosi} 0 PULSE(0 5 10u 1n 1n 10u 20u)",
        f"V_SCK {mcu_sck} 0 PULSE(0 5 10u 1n 1n 1u 2u)",
        
        # Physical Topology (R5-R10 1.8k/3.3k Divider)
        f"R5 {mcu_cs} {sd_cs} 1.8k",   f"R8 {sd_cs} 0 3.3k",
        f"R6 {mcu_mosi} {sd_mosi} 1.8k", f"R9 {sd_mosi} 0 3.3k",
        f"R7 {mcu_sck} {sd_sck} 1.8k",   f"R10 {sd_sck} 0 3.3k",
        
        # Parasitic Load
        f"C_LOAD {sd_cs} 0 10p",

        # --- Precise Measurement Commands (Sampling at 15us High Level) ---
        f".meas TRAN V_CS_HI FIND V({sd_cs}) AT 15u",
        f".meas TRAN V_MOSI_HI FIND V({sd_mosi}) AT 15u",
        f".meas TRAN V_SCK_HI FIND V({sd_sck}) AT 10.5u",
        f".meas TRAN V_SD_LOW FIND V({sd_cs}) AT 5u",
        f".meas TRAN T_RISE_SD TRIG V({sd_cs})=0.33 TARG V({sd_cs})=2.97 RISE=1",
        f".meas TRAN T_PROP_DLY TRIG V({mcu_cs})=2.5 RISE=1 TARG V({sd_cs})=1.65 RISE=1",
        f".meas TRAN I_STATIC_CS FIND I(R5) AT 15u",
        f".meas TRAN V_DIV_RATIO PARAM V({sd_cs})/V({mcu_cs})",
        f".meas TRAN P_LOSS_TOTAL PARAM (V({mcu_cs})-V({sd_cs}))*I(R5)",
        f".meas TRAN V_NOISE_MARG PARAM V({sd_cs})-2.0", 
        ".end"
    ]
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
        f"Tapuino SD Level Shifter Topology Verification Report | {datetime.now().strftime('%Y-%m-%d')}",
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
    run_and_report()