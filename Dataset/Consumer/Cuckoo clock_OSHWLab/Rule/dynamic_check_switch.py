import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE = os.path.join(BASE_DIR, "motor_switch_strict.net")
LOG_FILE = os.path.join(BASE_DIR, "motor_switch_strict.log")
REPORT_FILE = os.path.join(BASE_DIR, "motor_switch_report.txt")

TEST_CRITERIA = {
    # Standby Phase (Gate=5V, PMOS OFF)
    "v_motor_off":  {"name": "01_Motor_V_OFF",        "min": -0.1, "max": 0.1,  "unit": "V"},
    "i_leak_off":   {"name": "02_Leakage_Current_OFF", "min": -1e-6,"max": 1e-6, "unit": "A"},
    
    # Active Phase (Gate=0V, PMOS ON)
    "v_motor_on":   {"name": "03_Motor_V_ON",         "min": 4.5,  "max": 5.0,  "unit": "V"},
    "i_motor_run":  {"name": "04_Motor_Steady_Curr",   "min": 0.8,  "max": 1.2,  "unit": "A"},
    "v_drop_pmos":  {"name": "05_PMOS_Voltage_Drop",  "min": 0.0,  "max": 0.5,  "unit": "V"},
    
    # Transient Phase
    "t_switch_on":  {"name": "06_Motor_V_Rise_Time",   "min": 0.0,  "max": 1e-3, "unit": "s"}, 
    "v_spike_neg":  {"name": "07_Turn_OFF_Neg_Spike",  "min": -20000.0,"max": -10.0,  "unit": "V"}  
}

def build_pmos_netlist():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"JSON file not found: {JSON_FILE}")

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Extract mapping
    pins = {}
    for net in data.get("Motor Load Switch & Inrush Buffer", []):
        for conn in net["Connections"]:
            pins[f"{conn['ComponentID']}:{conn['PinName']}"] = net["net_id"]

    # 2. Bind JSON component pins
    n_pwr  = pins.get("Arduino:TOP_4", "NC_PWR")
    n_gnd  = pins.get("Arduino:TOP_5", "NC_GND")
    n_ctrl = pins.get("Arduino:LEFT_10", "NC_CTRL")
    
    # PMOS IRLM
    m_g = pins.get("IRLM:1", "NC_MG")
    m_d = pins.get("IRLM:2", "NC_MD")
    m_s = pins.get("IRLM:3", "NC_MS")
    
    # Motor ES9251II
    mot_vcc = pins.get("ES9251II:2", "NC_MOT_V")
    mot_gnd = pins.get("ES9251II:3", "NC_MOT_G")

    def n(name): return "0" if name in [n_gnd, mot_gnd] else name

    # 3. Construct High-Side PMOS Netlist
    netlist = [
        "* PMOS High-Side Motor Switch Strict Validation",
        ".model P_MOS VDMOS(pchan Vto=-1.5 Rs=0.05 Kp=5.0)", 
        ".tran 0 50m 0 1u", 
        
        # --- Power Supply ---
        f"V_BAT {n(n_pwr)} 0 5",
        
        # --- Control Logic ---
        # Starts 5V (OFF), drops to 0V at 10ms (ON), back to 5V at 30ms (OFF)
        f"V_CTRL {n(n_ctrl)} 0 PULSE(5 0 10m 1u 1u 20m 50m)",
        
        # --- Physical Components from JSON ---
        f"M1 {n(m_d)} {n(m_g)} {n(m_s)} {n(m_s)} P_MOS",
        
        # Equivalent Motor Model
        f"R_MOTOR {n(mot_vcc)} N_MID 5",
        f"L_MOTOR N_MID {n(mot_gnd)} 1mH",
        
        # --- Measurement Instructions ---
        f".meas TRAN v_motor_off AVG V({n(mot_vcc)}) FROM 2m TO 8m",
        f".meas TRAN i_leak_off AVG I(V_BAT) FROM 2m TO 8m",
        
        f".meas TRAN v_motor_on AVG V({n(mot_vcc)}) FROM 20m TO 28m",
        f".meas TRAN i_motor_run AVG I(L_MOTOR) FROM 20m TO 28m",
        f".meas TRAN v_drop_pmos AVG (V({n(n_pwr)})-V({n(m_d)})) FROM 20m TO 28m",
        
        # Rise time from 0.5V to 4.5V
        f".meas TRAN t_switch_on TRIG V({n(mot_vcc)}) VAL=0.5 RISE=1 TARG V({n(mot_vcc)}) VAL=4.5 RISE=1",
        
        # Negative spike validation
        f".meas TRAN v_spike_neg MIN V({n(mot_vcc)}) FROM 29m TO 35m",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    content = build_pmos_netlist()
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_raw = f.read()

    print("\n" + "="*85)
    print(f" PMOS High-Side Motor Switch Validation Report | Pure Topology")
    print("="*85)
    print(f"{'Test Item':<22} | {'Measured Value':<15} | {'Criteria':<15} | {'Status'}")
    print("-" * 85)

    pass_count = 0
    for key, spec in TEST_CRITERIA.items():
        match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log_raw, re.I)
        val = float(match.group(1)) if match else None
        
        if val is not None:
            is_ok = spec["min"] <= val <= spec["max"]
            status = "✅ PASS" if is_ok else "❌ FAIL"
            if is_ok: pass_count += 1
            
            if spec['unit'] == 's' and val < 0.1:
                val_str = f"{val*1000:>10.4f} ms"
            else:
                val_str = f"{val:>11.4f} {spec['unit']}"
        else:
            status = "⚠️ MISSING"
            val_str = "N/A"
            
        print(f"{spec['name']:<22} | {val_str:<15} | {spec['min']}~{spec['max']:<10} | {status}")

    print("-" * 85)
    print(f"📊 Module Overall Pass Rate: {(pass_count / len(TEST_CRITERIA)) * 100:.2f}%")
    print("="*85)

if __name__ == "__main__":
    run_simulation()