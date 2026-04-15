import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_bridge.json")

CIR_FILE  = os.path.join(BASE_DIR, "bridge_rc_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "bridge_rc_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "bridge_rc_report.txt")

TARGET_MODULE = "Automated Wired Diagnostic Bridge"

# Audit Metrics: Focuses on RC timing competition and synchronization during MCU wake-up.
TEST_CRITERIA = {
    "v_en_idle":   {"name": "[1] Idle: EN_Idle_State (~3.3V)",     "min": 3.00,    "max": 3.50, "unit": "V"},
    "v_en_rst":    {"name": "[2] Reset: EN_Hardware_Reset (~0V)",  "min": -0.10,   "max": 0.50, "unit": "V"},
    "t_rc_delay":  {"name": "[3] Rise: EN_RC_Rise_Time (>0.5ms)",  "min": 0.0005,  "max": 0.005,"unit": "S"},
    # Core Anti-cheat: When EN crosses the 2.0V wake-up threshold, IO0 must be held at a low level.
    "v_sync_io0":  {"name": "[4] Critical: IO0_at_Wake_Threshold", "min": -0.10,   "max": 0.80, "unit": "V"} 
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
    print(f"Performing Auto-Download RC Timing Competition Audit: {TARGET_MODULE}")
    
    nets_uart = parse_module_topology(JSON_FILE, TARGET_MODULE, "CH340") 
    nets_mcu  = parse_module_topology(JSON_FILE, TARGET_MODULE, "MCU")

    def get_net(nets_dict, pin_aliases):
        for alias in pin_aliases:
            for key in nets_dict.keys():
                if alias in key: return nets_dict[key]
        return f"NC_{uuid.uuid4().hex[:5]}"

    # Extract the four primary flow control pins
    n_dtr = get_net(nets_uart, ["DTR", "13"])
    n_rts = get_net(nets_uart, ["RTS", "14"])
    n_en  = get_net(nets_mcu,  ["EN", "RST"])
    n_io0 = get_net(nets_mcu,  ["IO0"])

    # Physical Anti-cheat: Check for short circuits to prevent perfect square waves from bypassing RC testing.
    nodes = [n_dtr, n_rts, n_en, n_io0]
    is_missing = any("NC_" in net for net in nodes)
    is_shorted = len(set(nodes)) != len(nodes)

    inject_models = True
    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (Flow control/Reset pins not fully connected)"
        inject_models = False
    elif is_shorted:
        status_info = "CRITICAL FAIL: Direct Connection Violation! (Direct drive detected bypassing transistors)"
        inject_models = False
    else:
        status_info = "TOPOLOGY PASS: Control line isolation normal. Preparing to inject critical crossover logic."

    print(f"  [Judgment Result] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Auto-Download RC Timing Competition Audit",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 1u 30m 0",
        
        f"R_D1 {sp(n_dtr)} 0 1G", f"R_D2 {sp(n_rts)} 0 1G",
        f"R_D3 {sp(n_en)} 0 1G", f"R_D4 {sp(n_io0)} 0 1G",

        f"V_VDD net_vdd 0 3.3V",
        
        "* Strict physical environment injection: Mount 100nF capacitor on EN to force RC delay",
        f"R_PU_EN {sp(n_en)} net_vdd 10k",
        f"C_EN_DELAY {sp(n_en)} 0 100n",
        f"R_PU_IO0 {sp(n_io0)} net_vdd 10k",

        "* UART chip issues programming sequence (generating competition/conflict segments)",
        "* 0-5ms: Idle",
        "* 5-15ms: Pull EN low to reset MCU (DTR=0, RTS=3.3)",
        "* After 15ms: Release EN for slow charging while pulling IO0 low (DTR=3.3, RTS=0)",
        f"V_DTR {sp(n_dtr)} 0 PWL(0 3.3V 5m 3.3V 5.01m 0V 15m 0V 15.01m 3.3V 30m 3.3V)",
        f"V_RTS {sp(n_rts)} 0 PWL(0 3.3V 5m 3.3V 5.01m 3.3V 15m 3.3V 15.01m 0V 30m 0V)"
    ]

    if inject_models:
        netlist.extend([
            "* Inject standard dual-transistor cross-mapping circuit",
            f"Q1 {sp(n_en)} net_q1_b {sp(n_dtr)} NPN_SS8050",
            f"R_Q1_B {sp(n_rts)} net_q1_b 10k",
            
            f"Q2 {sp(n_io0)} net_q2_b {sp(n_rts)} NPN_SS8050",
            f"R_Q2_B {sp(n_dtr)} net_q2_b 10k",
            
            ".model NPN_SS8050 NPN(Is=1e-14 Bf=300 Vaf=100)",

            "* --- Timing Measurement (Wake-up Moment Capture) ---",
            f".meas TRAN v_en_idle AVG V({sp(n_en)}) FROM 1m TO 4m",
            f".meas TRAN v_en_rst  MIN V({sp(n_en)}) FROM 8m TO 12m",
            
            "* Calculate RC rise time (from 0.5V to 2.0V)",
            f".meas TRAN t_en_start FIND time WHEN V({sp(n_en)})=0.5 RISE=1",
            f".meas TRAN t_en_wake  FIND time WHEN V({sp(n_en)})=2.0 RISE=1",
            f".meas TRAN t_rc_delay PARAM t_en_wake - t_en_start",
            
            "* Ultimate Test: Capture IO0 voltage at the instant EN crosses 2.0V!",
            f".meas TRAN v_sync_io0 FIND V({sp(n_io0)}) WHEN V({sp(n_en)})=2.0 RISE=1"
        ])
    else:
        netlist.extend([
            f".meas TRAN v_en_idle  PARAM 0",
            f".meas TRAN v_en_rst   PARAM 0",
            f".meas TRAN t_rc_delay PARAM 0",
            f".meas TRAN v_sync_io0 PARAM 99"
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
        
        report = ["="*65, " AUTO-DOWNLOAD RC TIMING AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            
            # Format unit output (handling microseconds/milliseconds)
            if val is None:
                val_str = "N/A"
            elif "S" in spec["unit"] and val < 0.01:
                val_str = f"{val*1000:>8.3g} ms"
            else:
                val_str = f"{val:>8.3g} {spec['unit']}"
                
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: 
            f.write(final_report_str)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()