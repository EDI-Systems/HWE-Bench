import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_drive.json")

CIR_FILE  = os.path.join(BASE_DIR, "drive_channel_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "drive_channel_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "drive_channel_report.txt")

TARGET_MODULE = "High-Current Drive Channels"

# Audit Metrics: Full-workflow voltage/current matrix tracking.
TEST_CRITERIA = {
    "v_drain_idle": {"name": "[1] Idle: V_Drain_Idle (~5V)",        "min": 4.80,  "max": 5.20, "unit": "V"},
    "i_motor_idle": {"name": "[2] Idle: I_Motor_Idle (0A)",         "min": -0.01, "max": 0.05, "unit": "A"},
    "i_motor_run":  {"name": "[4] Full Load: I_Motor_Run (>1A)",    "min": 1.00,  "max": 6.00, "unit": "A"},
    "v_spike_max":  {"name": "[5] Turn-off: V_Spike_Clamp (<6V)",   "min": -1.00, "max": 6.50, "unit": "V"},
    "i_diode_pk":   {"name": "[6] Turn-off: I_Diode_Catch (>1A)",   "min": 1.00,  "max": 6.00, "unit": "A"},
    "i_motor_dec":  {"name": "[7] Decay: I_Motor_Decay (->0A)",     "min": -0.10, "max": 0.20, "unit": "A"} 
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path):
        print(f"  [FATAL ERROR] JSON file not found!: {json_path}")
        return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception as e: return {}
    module_nets = data.get(module_name, [])
    target_nets = {}
    for net in module_nets:
        for conn in net.get("Connections", []):
            if component_id in str(conn.get("ComponentID", "")):
                target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def build_netlist():
    print("="*65)
    print(f"Performing High-Current Motor Full-Workflow Dynamic Audit: {TARGET_MODULE}")
    
    nets_mcu   = parse_module_topology(JSON_FILE, TARGET_MODULE, "MCU") 
    nets_mos   = parse_module_topology(JSON_FILE, TARGET_MODULE, "SM4410PRL")
    nets_diode = parse_module_topology(JSON_FILE, TARGET_MODULE, "SS34")
    nets_motor = parse_module_topology(JSON_FILE, TARGET_MODULE, "Motor_Connector")

    def get_net(nets_dict, pin_aliases):
        for alias in pin_aliases:
            for key in nets_dict.keys():
                if alias in key: return nets_dict[key]
        return f"NC_{uuid.uuid4().hex[:5]}"

    n_pwm   = get_net(nets_mcu, ["IO14", "IO12", "PWM"])
    n_gate  = get_net(nets_mos, ["G", "Gate", "1"])
    n_drain = get_net(nets_mos, ["D", "Drain", "2", "3", "4"])
    n_d_cat = get_net(nets_diode, ["K", "Cathode", "2"])
    n_d_ano = get_net(nets_diode, ["A", "Anode", "1"])
    n_m_pos = get_net(nets_motor, ["+", "VCC", "1"])
    n_m_neg = get_net(nets_motor, ["-", "GND", "2"])

    # Physical Isolation and Anti-cheat verification
    is_missing = any("NC_" in net for net in [n_pwm, n_gate, n_drain, n_d_cat, n_d_ano, n_m_pos, n_m_neg])
    is_shorted = (n_gate == n_drain) or (n_d_cat == n_d_ano)

    inject_models = True
    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (Critical control nets not fully connected)"
        inject_models = False
    elif is_shorted:
        status_info = "CRITICAL FAIL: Fatal Short Circuit Violation!"
        inject_models = False
    else:
        status_info = "TOPOLOGY PASS: Found complete freewheeling topology. Injecting inductive motor lifecycle load."

    print(f"  [Judgment Result] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Motor Drive Full Lifecycle Audit - Physics Tuned",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 1u 30m 0",
        
        f"R_D1 {sp(n_pwm)} 0 1G", f"R_D2 {sp(n_drain)} 0 1G",
        f"R_D3 {sp(n_d_cat)} 0 1G", f"R_D4 {sp(n_m_pos)} 0 1G",

        f"V_PWR {sp(n_m_pos)} 0 5V",
        f"V_PWM {sp(n_pwm)} 0 PWL(0 0V 10m 0V 10.01m 3.3V 20m 3.3V 20.01m 0V 30m 0V)"
    ]

    if inject_models:
        netlist.extend([
            f"M1 {sp(n_drain)} {sp(n_gate)} 0 0 N_SM4410",
            f".model N_SM4410 VDMOS(Rg=2 Vto=1.5 Rd=10m Rs=5m Cgdmax=2n Cgdmin=1n Cgs=3n)",
            f"R_GATE {sp(n_pwm)} {sp(n_gate)} 100",

            f"L_MOTOR net_motor_mid {sp(n_m_neg)} 1mH",
            f"R_MOTOR {sp(n_m_pos)} net_motor_mid 1",
            
            f"D_FLYBACK {sp(n_d_ano)} {sp(n_d_cat)} D_SS34",
            f".model D_SS34 D(Is=2e-5 Rs=0.05 N=1.05 Eg=0.69)",

            # 1. Idle Phase (0-10ms) Measurement
            f".meas TRAN v_drain_idle AVG V({sp(n_drain)}) FROM 2m TO 8m",
            f".meas TRAN i_motor_idle AVG I(L_MOTOR) FROM 2m TO 8m",
            
            # 2. Full Load Phase (10-20ms) Measurement
            f".meas TRAN v_drain_run  AVG V({sp(n_drain)}) FROM 15m TO 19m",
            f".meas TRAN i_motor_run  MAX I(L_MOTOR) FROM 15m TO 19m",
            
            # 3. Turn-off Moment (20ms-21ms) Measurement of kickback
            f".meas TRAN v_spike_max  MAX V({sp(n_drain)}) FROM 19.5m TO 22m",
            f".meas TRAN i_diode_pk   MAX I(D_FLYBACK) FROM 19.5m TO 21m",
            
            # 4. Decay Phase (21ms-30ms) Measurement of energy release
            f".meas TRAN i_motor_dec  AVG I(L_MOTOR) FROM 26m TO 29m"
        ])
    else:
        netlist.extend([
            f".meas TRAN v_drain_idle PARAM 0", f".meas TRAN i_motor_idle PARAM 999",
            f".meas TRAN v_drain_run  PARAM 0", f".meas TRAN i_motor_run  PARAM 0",
            f".meas TRAN v_spike_max  PARAM 999", f".meas TRAN i_diode_pk PARAM 0",
            f".meas TRAN i_motor_dec  PARAM 999"
        ])

    netlist.append(".end")
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
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m: results[k] = float(m.group(1))
        
        report = ["="*65, " MOTOR DRIVE FULL LIFECYCLE AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3g} {spec['unit']}" if val is not None else "N/A"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: 
            f.write(final_report_str)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()