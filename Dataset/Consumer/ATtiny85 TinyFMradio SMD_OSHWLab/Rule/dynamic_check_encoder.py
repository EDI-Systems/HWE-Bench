import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = "D:/app/LTspice/LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct","dynamic_encoder.json")
CIR_FILE  = os.path.join(BASE_DIR, "encoder_connectivity_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "encoder_connectivity_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "encoder_connectivity_report.txt")

# --- Core Audit Metrics ---
TEST_CRITERIA = {
    "v_a_mcu":     {"name": "MCU_PB3_Receive_A",    "min": 3.00, "max": 3.40, "unit": "V"},
    "v_b_mcu":     {"name": "MCU_PB4_Receive_B",    "min": 3.00, "max": 3.40, "unit": "V"},
    "v_sw_mcu":    {"name": "MCU_PB1_Receive_SW",   "min": 3.00, "max": 3.40, "unit": "V"},
    "topo_score":  {"name": "Net_ID_Consistency",   "min": 1.0,  "max": 1.0,  "unit": "Score"}
}

def parse_dut_topology(json_path, module_name, dut_name):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except: return {}
    target_module = data.get(module_name, [])
    dut_nets = {}
    for net in target_module:
        for conn in net.get("Connections", []):
            if conn.get("ComponentID") == dut_name:
                dut_nets[conn.get("PinName")] = net.get("net_id", "")
    return dut_nets

def build_netlist():
    nets_enc = parse_dut_topology(JSON_FILE, "User Input & Control Module", "Rotary Encoder")
    nets_mcu = parse_dut_topology(JSON_FILE, "User Input & Control Module", "ATtiny85")

    # Stimulus side nets
    enc_a_net  = nets_enc.get("Phase A", "FLOAT_ENCA")
    enc_b_net  = nets_enc.get("Phase B", "FLOAT_ENCB")
    enc_sw_net = nets_enc.get("SW1",     "FLOAT_ENCSW")
    
    # Measurement side nets: If missing, force pointing to 'EMPTY_NODE' to ensure .meas command execution
    mcu_pb3_net = nets_mcu.get("PB3", "EMPTY_NODE_A")
    mcu_pb4_net = nets_mcu.get("PB4", "EMPTY_NODE_B")
    mcu_pb1_net = nets_mcu.get("PB1", "EMPTY_NODE_SW")
    
    vcc_net = nets_mcu.get("VCC", "net_vcc")
    
    # Topology consistency scoring logic
    topology_valid = 1 if (enc_a_net == mcu_pb3_net and enc_a_net != "FLOAT_ENCA") else 0

    netlist = [
        "* Connectivity-Sensitive Audit - Optimized",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 10m 0 uic",
        
        f"V_VCC {vcc_net} 0 3.3V",
        
        # Stimulus sources mounted only on encoder pin nets
        f"R7 {vcc_net} {enc_a_net} 10k",
        f"C14 {enc_a_net} 0 100n IC=3.3",
        f"V_STIM_A {enc_a_net}_stim 0 PULSE(0 3.3 1m 10u 10u 2m 5m)",
        f"S_MECH_A {enc_a_net} 0 {enc_a_net}_stim 0 SW_MOD",
        
        f"R8 {vcc_net} {enc_b_net} 10k",
        f"R9 {vcc_net} {enc_sw_net} 10k",
        
        # Fail-safe: prevent isolated nodes from causing singular matrix errors
        f"R_DUMMY_A EMPTY_NODE_A 0 1G",
        f"R_DUMMY_B EMPTY_NODE_B 0 1G",
        f"R_DUMMY_S EMPTY_NODE_SW 0 1G",
        
        ".model SW_MOD SW(Ron=1 Roff=10Meg Vt=1.65)",

        # Probe signals at MCU target pins
        f".meas TRAN v_a_mcu MAX V({mcu_pb3_net}) FROM 0 TO 10m",
        f".meas TRAN v_b_mcu MAX V({mcu_pb4_net}) FROM 0 TO 10m",
        f".meas TRAN v_sw_mcu MAX V({mcu_pb1_net}) FROM 0 TO 10m",
        f".meas TRAN topo_score PARAM {topology_valid}",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    print(f"--- Audit Task Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    
    # Force cleanup of old files
    for f in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(f): os.remove(f)
            
    try:
        # 1. Build Netlist
        with open(CIR_FILE, 'w', encoding='utf-8') as f: 
            f.write(build_netlist())
            
        # 2. Invoke LTspice
        print("Running simulation engine...")
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
        if not os.path.exists(LOG_FILE):
            print("Error: Log file not generated.")
            return

        # 3. Parse Log
        with open(LOG_FILE, 'r', errors='ignore') as f: 
            log = f.read()

        results = {k: None for k in TEST_CRITERIA}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            if m: results[k] = float(m.group(1))

        # 4. Format Report
        report = []
        report.append("="*65)
        report.append(f" ENCODER MODULE CONNECTIVITY AUDIT REPORT")
        report.append(f" Timestamp: {datetime.now().isoformat()}")
        report.append("="*65)
        report.append(f"{'Audit Item':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3f} {spec['unit']}" if val is not None else "N/A"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status}")

        report.append("-" * 65)
        rate = (pass_count / len(TEST_CRITERIA)) * 100
        report.append(f"TOTAL PASS RATE: {rate:.1f}%")
        report.append("="*65)
        
        final_out = "\n".join(report)
        
        # 5. Output to console and TXT file simultaneously
        print(final_out)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_out)
            f.flush()
            os.fsync(f.fileno()) 
            
        print(f"\n[Success] Audit report saved to: {os.path.abspath(REPORT_FILE)}")

    except Exception as e:
        print(f"Simulation Aborted: {e}")

if __name__ == "__main__":
    run_simulation()