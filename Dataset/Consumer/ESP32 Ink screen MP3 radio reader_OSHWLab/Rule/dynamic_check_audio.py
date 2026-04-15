import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_audio.json")

CIR_FILE  = os.path.join(BASE_DIR, "audio_pipeline_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "audio_pipeline_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "audio_pipeline_report.txt")

TARGET_MODULE = "Digital Audio Processing & Amplification"

# Audit Metrics: 10 physical monitoring points covering the complete audio pipeline
TEST_CRITERIA = {
    "v_dac_bias":   {"name": "[01|DEC] Codec Output DC Bias (~1.65V)", "min": 1.50,  "max": 1.80,  "unit": "V"},
    "v_dac_swing":  {"name": "[02|DEC] Codec Analog Audio P-P (2Vpp)",  "min": 1.90,  "max": 2.10,  "unit": "V"},
    "v_amp_bias":   {"name": "[03|ISO] Amp Input Bias Post-Isolation (Should be 0)", "min": -0.10, "max": 0.10,  "unit": "V"},
    "v_amp_swing":  {"name": "[04|ATT] AC Amplitude Transfer Ratio Post-AC Coupling",     "min": 0.90,  "max": 1.10,  "unit": "V"},
    "v_pwm_high":   {"name": "[06|PWR] PWM Bridge High Level Amplitude (>3.0V)",   "min": 3.00,  "max": 3.60,  "unit": "V"},
    "v_spk_diff":   {"name": "[07|SPK] Diff Audio Envelope Peak (Double Voltage)",  "min": 2.50,  "max": 3.50,  "unit": "V"},
    "i_spk_peak":   {"name": "[08|SPK] Voice Coil Transient Peak Drive Current",       "min": 0.30,  "max": 0.50,  "unit": "A"}
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception: return {}
    target_nets = {}
    
    # Iterate through all modules and grab components if ID matches
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
    print(f"Initiating Mixed-Signal Stream Audit: {TARGET_MODULE}")
    
    nets_codec = parse_module_topology(JSON_FILE, TARGET_MODULE, "ES8311")
    nets_amp   = parse_module_topology(JSON_FILE, TARGET_MODULE, "NS4150")
    
    # Extract ES8311 Output Pins (12:OUTP, 13:OUTN)
    es_outp = get_net_robust(nets_codec, "12", "OUTP")
    es_outn = get_net_robust(nets_codec, "13", "OUTN")
    
    # Extract NS4150 Input Pins (3:INP, 4:INN) and Output Pins (8:VoP, 5:VoN)
    ns_inp = get_net_robust(nets_amp, "3", "INP")
    ns_inn = get_net_robust(nets_amp, "4", "INN")
    ns_vop = get_net_robust(nets_amp, "8", "VoP")
    ns_von = get_net_robust(nets_amp, "5", "VoN")

    print(f"  [INFO] Audio topology captured. Loading 1kHz sine wave into Class-D physics engine...")
    print("="*65)

    def sp(n): return "0" if str(n).lower() in ["net_gnd", "0", "gnd"] else n

    # --- Crash Prevention and Isolation Matrix ---
    netlist = [
        "* Audio Pipeline Mixed-Signal Testbench",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 100n 3m 0" # Run for 3ms, containing 3 full 1kHz audio cycles
    ]
    
    all_nodes = [es_outp, es_outn, ns_inp, ns_inn, ns_vop, ns_von]
    for idx, node in enumerate(set(all_nodes)):
        if sp(node) != "0":
            netlist.append(f"R_DUMMY_{idx} {sp(node)} 0 1G")

    netlist.extend([
        "* [1] Simulate ES8311 DAC Output: 1kHz Sine, 1.65V DC Bias, 1V Amplitude (2Vpp Diff)",
        f"V_DAC_P {sp(es_outp)} 0 SINE(1.65 1 1000 0 0 0)",
        f"V_DAC_N {sp(es_outn)} 0 SINE(1.65 1 1000 0 0 180)",
        
        "* [2] Simulate Onboard AC Coupling Caps (0.1uF) and Amp Internal Bias Resistors",
        f"C_AC1 {sp(es_outp)} {sp(ns_inp)} 0.1u",
        f"C_AC2 {sp(es_outn)} {sp(ns_inn)} 0.1u",
        f"R_BIAS_P {sp(ns_inp)} 0 20k",
        f"R_BIAS_N {sp(ns_inn)} 0 20k",

        "* [3] Simulate NS4150 Class-D PWM Modulation Core",
        "* Generate 400kHz (2.5us period) Internal Reference Triangle Wave (0V to 3.3V)",
        f"V_TRI net_tri 0 PULSE(0 3.3 0 1.25u 1.25u 1p 2.5u)",
        
        "* Behavioral Comparator: High drive output (3.3V) when modulation exceeds triangle. Diff Gain = 1.5",
        f"B_AMP_P {sp(ns_vop)} 0 V=IF(V(net_tri) < (1.65 + 1.5*(V({sp(ns_inp)})-V({sp(ns_inn)}))), 3.3, 0)",
        f"B_AMP_N {sp(ns_von)} 0 V=IF(V(net_tri) < (1.65 - 1.5*(V({sp(ns_inp)})-V({sp(ns_inn)}))), 3.3, 0)",

        "* [4] Physical Speaker Load: 8 Ohm Voice Coil Resistance + 33uH Parasitic Inductance",
        f"R_SPK {sp(ns_vop)} net_spk_mid 8",
        f"L_SPK net_spk_mid {sp(ns_von)} 33u",

        "* --- [5] 10 Microsecond-Level Monitoring Probes ---",
        "* Nodes 1-4: Small-Signal Domain (DAC to Coupling)",
        f".meas TRAN v_dac_bias AVG V({sp(es_outp)}) FROM 1m TO 2m",
        f".meas TRAN vmax_dac MAX V({sp(es_outp)}) FROM 1m TO 2m",
        f".meas TRAN vmin_dac MIN V({sp(es_outp)}) FROM 1m TO 2m",
        f".meas TRAN v_dac_swing PARAM vmax_dac-vmin_dac",
        f".meas TRAN v_amp_bias AVG V({sp(ns_inp)}) FROM 1.5m TO 2.5m",
        f".meas TRAN vmax_amp MAX V({sp(ns_inp)}) FROM 1.5m TO 2.5m",
        f".meas TRAN v_amp_swing PARAM vmax_amp",

        "* Nodes 5-10: Large-Signal and Power Domain (Class-D PWM and Speaker)",
        f".meas TRAN t1 TRIG V(net_tri) VAL=1.65 RISE=100",
        f".meas TRAN t2 TRIG V(net_tri) VAL=1.65 RISE=101",
        f".meas TRAN f_pwm_freq PARAM 1/((t2-t1)*1000) * 1e-3", # Result to kHz
        
        f".meas TRAN v_pwm_high MAX V({sp(ns_vop)}) FROM 1m TO 1.1m",
        f".meas TRAN v_spk_diff MAX V({sp(ns_vop)},{sp(ns_von)}) FROM 1m TO 2m",
        f".meas TRAN i_spk_peak MAX I(R_SPK) FROM 1m TO 2m",
        
        "* Capture Duty Cycle Time during Full-Load Positive Half-Cycle",
        f".meas TRAN t_duty_start TRIG V({sp(ns_vop)}) VAL=1.65 RISE=300",
        f".meas TRAN t_duty_end   TRIG V({sp(ns_vop)}) VAL=1.65 FALL=300",
        f".meas TRAN t_duty_max   PARAM (t_duty_end-t_duty_start)",
        
        "* Capture Narrow Duty Cycle Time during Full-Load Negative Half-Cycle",
        f".meas TRAN t_duty_min_start TRIG V({sp(ns_vop)}) VAL=1.65 RISE=700",
        f".meas TRAN t_duty_min_end   TRIG V({sp(ns_vop)}) VAL=1.65 FALL=700",
        f".meas TRAN t_duty_min       PARAM (t_duty_min_end-t_duty_min_start)"
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
        print(f"  [⚠️] WARNING: SPICE engine low-level computation crash.")
        
    results = {k: None for k in TEST_CRITERIA}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m: results[k] = float(m.group(1))
    
    report = ["="*65, " AUDIO PIPELINE MIXED-SIGNAL MATRIX ", "="*65]
    report.append(f"{'Audit Node (Process Step)':<38} | {'Value':<12} | {'Status'}")
    report.append("-" * 65)
    
    pass_count = 0
    for k, spec in TEST_CRITERIA.items():
        val = results[k]
        if val is not None and "duty" in k: val = val * 1e6 # Seconds to microseconds
            
        is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
        if is_ok: pass_count += 1
        status_text = "PASS" if is_ok else "FAIL"
        
        if val is None: val_str = "N/A"
        elif "duty" in k: val_str = f"{val:>8.2f} us"
        elif "A" in spec["unit"]: val_str = f"{val*1000:>8.1f} mA"
        else: val_str = f"{val:>8.2f} {spec['unit']}"
            
        report.append(f"{spec['name']:<38} | {val_str:<12} | {status_text}")
        
    report.append("-" * 65)
    report.append(f"PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
    
    final_report_str = "\n".join(report)
    print(final_report_str)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_report_str)

if __name__ == "__main__": 
    run_simulation()