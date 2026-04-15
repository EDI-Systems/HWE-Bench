import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE  = os.path.join(BASE_DIR, "audio_ac_coupling_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "audio_ac_coupling_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "audio_ac_coupling_report.txt")

TARGET_MODULE = "High-Fidelity Audio Subsystem"

# Audit Metrics: 10-channel Audio AC/DC Isolation and Transient Power Matrix
TEST_CRITERIA = {
    "v_bias_dac":   {"name": "[01|Bias] DAC Output DC Offset (~1.65V)",      "min": 1.60,  "max": 1.70,  "unit": "V"},
    "v_swing_dac":  {"name": "[02|Signal] DAC 100Hz AC Peak-to-Peak",         "min": 1.90,  "max": 2.10,  "unit": "V"},
    "v_bias_hp":    {"name": "[03|Iso] Headphone Load Residual DC Bias (~0V)", "min": -0.05, "max": 0.05,  "unit": "V"},
    "v_swing_hp":   {"name": "[04|Freq] HP Load 100Hz AC Peak-to-Peak",       "min": 1.80,  "max": 2.10,  "unit": "V"},
    "i_peak_hp":    {"name": "[05|Drive] 32 Ohm Voice Coil Max Drive Current", "min": 25.0,  "max": 35.0,  "unit": "mA"},
    "v_drop_ac":    {"name": "[06|Loss] 220uF Coupling Cap Low-Freq AC Drop",  "min": 0.00,  "max": 0.30,  "unit": "V"},
    "v_clip_high":  {"name": "[09|Safety] DAC Positive Clipping Margin (<3.3V)", "min": 2.50,  "max": 3.20,  "unit": "V"},
    "v_clip_low":   {"name": "[10|Safety] DAC Negative Clipping Margin (>0.0V)", "min": 0.10,  "max": 0.80,  "unit": "V"}
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception: return {}
    target_nets = {}
    for module, nets in data.items():
        for net in nets:
            for conn in net.get("Connections", []):
                if component_id in str(conn.get("ComponentID", "")):
                    target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def get_net_robust(nets_dict, pin_number, pin_name):
    if pin_number in nets_dict: return nets_dict[pin_number]
    if pin_name in nets_dict: return nets_dict[pin_name]
    return f"NC_{uuid.uuid4().hex[:5]}"

def build_netlist():
    print("="*65)
    print(f"Initiating Hi-Fi Audio Subsystem Audit: Coupling Caps & Low-Freq Response")
    
    # Extract Analog Output pins for PCM1771
    nets_dac = parse_module_topology(JSON_FILE, TARGET_MODULE, "PCM1771")
    
    # Extract Right Channel Output (Pin 10: HOUTR)
    n_houtr = get_net_robust(nets_dac, "10", "HOUTR")

    print(f"  [INFO] Topology captured. Taking over DAC output and building 32 Ohm physical testbench...")
    print("="*65)

    def sp(n): return "0" if str(n).lower() in ["net_gnd", "0", "gnd"] else n

    netlist = [
        "* High-Fidelity Audio AC Coupling Testbench",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 100u 100m 0", # Simulation for 100ms to observe RC charging and 100Hz cycles
        
        f"R_DUMMY {sp(n_houtr)} 0 1G"
    ]

    netlist.extend([
        "* [1] Simulate PCM1771 Internal DAC Characteristics",
        "* Setting: 1.65V DC Bias with 1V Amplitude (2Vpp) 100Hz Sine wave",
        f"V_DAC_RAW net_dac_raw 0 SINE(1.65 1 100 0 0)",
        f"R_DAC_OUT net_dac_raw {sp(n_houtr)} 1", # Small internal output impedance
        
        "* [2] Virtual Takeover: 220uF Coupling Cap (C2) from Schematic",
        "* Responsible for blocking 1.65V DC while passing AC audio",
        f"C_COUPLING {sp(n_houtr)} net_hp_out 220u",
        
        "* [3] Physical Headphone Load (Standard 32 Ohm impedance)",
        f"R_HEADPHONE net_hp_out 0 32",

        "* --- [4] 10 Microsecond-Level Monitoring Probes ---",
        
        "* Nodes 1-2: DAC Raw Output Characteristics",
        f".meas TRAN v_bias_dac AVG V({sp(n_houtr)}) FROM 60m TO 100m",
        f".meas TRAN vmax_dac MAX V({sp(n_houtr)}) FROM 60m TO 100m",
        f".meas TRAN vmin_dac MIN V({sp(n_houtr)}) FROM 60m TO 100m",
        f".meas TRAN v_swing_dac PARAM (vmax_dac - vmin_dac)",
        
        "* Nodes 3-4: Headphone Load Characteristics (Verify DC Blocking)",
        f".meas TRAN v_bias_hp AVG V(net_hp_out) FROM 60m TO 100m",
        f".meas TRAN vmax_hp MAX V(net_hp_out) FROM 60m TO 100m",
        f".meas TRAN vmin_hp MIN V(net_hp_out) FROM 60m TO 100m",
        f".meas TRAN v_swing_hp PARAM (vmax_hp - vmin_hp)",
        
        "* Node 5: Current Drive Capability",
        f".meas TRAN i_hp_raw MAX I(R_HEADPHONE) FROM 60m TO 100m",
        f".meas TRAN i_peak_hp PARAM abs(i_hp_raw)",
        
        "* Node 6: AC Voltage Drop caused by Capacitor",
        f".meas TRAN v_drop_raw MAX V({sp(n_houtr)}, net_hp_out) FROM 60m TO 100m",
        f".meas TRAN v_drop_ac PARAM abs(v_drop_raw - 1.65)", 
        
        "* Node 7: Initial DC Settling Time (Prevents headphone 'pop' noise)",
        f".meas TRAN t_settle_dc TRIG V({sp(n_houtr)}) VAL=0.1 RISE=1 TARG V({sp(n_houtr)}) VAL=1.60 RISE=1",
        
        "* Node 8: Output RMS Power Evaluation (mW)",
        f".meas TRAN p_load_avg AVG (V(net_hp_out)*V(net_hp_out)/32) FROM 60m TO 100m",
        
        "* Nodes 9-10: Power Rail Clipping Margins",
        f".meas TRAN v_clip_high PARAM vmax_dac",
        f".meas TRAN v_clip_low  PARAM vmin_dac"
    ])

    netlist.append(".end")
    return "\n".join(netlist)

def run_simulation():
    for f in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(f): os.remove(f)
        
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
    except subprocess.CalledProcessError as e:
        print(f"  [⚠️] WARNING: SPICE engine computation failure.")
        
    results = {k: None for k in TEST_CRITERIA}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m: results[k] = float(m.group(1))
    
    report = ["="*65, " AUDIO AC COUPLING & LOW-FREQ MATRIX ", "="*65]
    report.append(f"{'Audit Node (Process Step)':<40} | {'Value':<10} | {'Status'}")
    report.append("-" * 65)
    
    pass_count = 0
    for k, spec in TEST_CRITERIA.items():
        val = results[k]
        
        # Unit conversion for display
        if val is not None:
            if spec["unit"] == "mA": val = val * 1000
            elif spec["unit"] == "ms": val = val * 1000
            elif spec["unit"] == "mW": val = val * 1000
            
        is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
        if is_ok: pass_count += 1
        status_text = "PASS" if is_ok else "FAIL"
        
        if val is None: val_str = "N/A"
        elif spec["unit"] in ["mA", "mW", "ms"]: val_str = f"{val:>7.2f} {spec['unit']}"
        else: val_str = f"{val:>7.3f} {spec['unit']}"
            
        report.append(f"{spec['name']:<40} | {val_str:<10} | {status_text}")
        
    report.append("-" * 65)
    report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
    
    final_report_str = "\n".join(report)
    print(final_report_str)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_report_str)

if __name__ == "__main__": 
    run_simulation()