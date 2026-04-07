import os
import subprocess
import re
import json

LTSPICE_EXE = "D:/app/LTspice/LTspice.exe"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE = os.path.join(BASE_DIR, "tc_amp_auto.net")
LOG_FILE = os.path.join(BASE_DIR, "tc_amp_auto.log")

TEST_POINTS_CONFIG = [
    {"id": "V_OUT_MAX",  "unit": "V", "min": 3.95,  "max": 4.10,  "name": "Full Scale Detection", "desc": "20mV input corresponds to 4.02V"},
    {"id": "V_OUT_MID",  "unit": "V", "min": 1.95,  "max": 2.05,  "name": "Linear Midpoint",      "desc": "10mV input corresponds to 2.01V"},
    {"id": "V_ADC_LINK", "unit": "V", "min": 3.95,  "max": 4.10,  "name": "ADC Link Connectivity", "desc": "Verify if MCU:PC0 pin receives signal"},
    {"id": "V_FB_SHORT", "unit": "V", "min": -1e-3, "max": 1e-3,  "name": "Op-amp Virtual Short", "desc": "Verify if differential voltage is near 0V"},
    {"id": "V_NON_INV",  "unit": "V", "min": 0.019, "max": 0.021, "name": "Input Pin Potential",  "desc": "Verify if stimulus successfully enters the chip"},
    {"id": "V_VCC_LMV",  "unit": "V", "min": 4.80,  "max": 5.20,  "name": "IC Power Detection",   "desc": "Verify if LMV358 power pin is energized"},
    {"id": "V_GND_LMV",  "unit": "V", "min": -0.01, "max": 0.01,  "name": "IC Grounding Detection", "desc": "Verify LMV358 GND pin potential"},
    {"id": "V_LIN_75",   "unit": "V", "min": 2.95,  "max": 3.10,  "name": "High-range Linearity",  "desc": "Gain performance at 15mV input"}
]

def build_netlist():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    module_data = data.get("Precision Thermocouple Signal Conditioner", [])
    pins = {f"{c['ComponentID']}:{c['PinName']}": net['net_id'] for net in module_data for c in net['Connections']}

    n_out = pins.get("LMV358:OUT2", "NC_O")
    n_inv = pins.get("LMV358:-IN2", "NC_I")
    n_ni  = pins.get("LMV358:+IN2", "NC_NI")
    n_vcc = pins.get("LMV358:VCC+", "NC_V")
    n_gnd = pins.get("LMV358:GND", "NC_G")
    n_adc = pins.get("ATmega328P:PC0", "NC_A")

    netlist = f"""* TC Amp Test Bench (No Auto-Fix)
.tran 100m startup
.options plotwinsize=0 numdgt=7
V_V1 net_tc_src 0 PWL(0 0 100m 20m)
V_V2 net_vcc_src 0 5
R_R3 net_tc_src {n_ni} 10k
R_R1 {n_out} {n_inv} 200k
R_R2 {n_inv} {n_gnd} 1k
V_B_VCC {n_vcc} net_vcc_src 0
V_B_GND {n_gnd} 0 0
XU1 {n_out} {n_inv} {n_ni} {n_vcc} {n_gnd} MyOpAmp
.subckt MyOpAmp out inv non vcc vee
B1 out_int vee V=limit(1e6*(V(non)-V(inv)), V(vee), V(vcc))
R_out out_int out 1
.ends
.meas TRAN V_OUT_MAX AVG V({n_out}) FROM 99m TO 100m
.meas TRAN V_OUT_MID AVG V({n_out}) FROM 49m TO 51m
.meas TRAN V_ADC_LINK AVG V({n_adc}) FROM 99m TO 100m
.meas TRAN V_FB_SHORT AVG V({n_ni})-V({n_inv}) FROM 50m TO 60m
.meas TRAN V_NON_INV AVG V({n_ni}) FROM 99m TO 100m
.meas TRAN V_VCC_LMV AVG V({n_vcc})
.meas TRAN V_GND_LMV AVG V({n_gnd})
.meas TRAN I_STATIC AVG ABS(I(V_V2)) FROM 10m TO 90m
.meas TRAN V_LIN_75  AVG V({n_out}) FROM 74m TO 76m
.meas TRAN T_SETTLE TRIG V({n_out})=0.1 TARG V({n_out})=3.9 RISE=1
.end
"""
    return netlist

def run_benchmark():
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f:
            f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], timeout=15, check=True)
    except Exception:
        return

    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()

    pass_cnt = 0
    for tp in TEST_POINTS_CONFIG:
        pattern = rf"{tp['id']}[^=]*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
        match = re.search(pattern, log_content, re.IGNORECASE)
        val = float(match.group(1)) if match else -99.0
        
        status = "PASS" if tp['min'] <= val <= tp['max'] else "FAIL"
        if status == "PASS": pass_cnt += 1

if __name__ == "__main__":
    run_benchmark()