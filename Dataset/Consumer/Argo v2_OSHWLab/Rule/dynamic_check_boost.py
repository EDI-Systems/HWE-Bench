import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_boost.json")
CIR_FILE  = os.path.join(BASE_DIR, "tps61022_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "tps61022_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "tps61022_audit_report.txt")

TEST_CRITERIA = {
    "v_in_steady":     {"name": "VSYS_Input_Voltage",     "min": 3.20, "max": 3.40, "unit": "V"},
    "v_out_steady":    {"name": "5V_Boost_Output",        "min": 4.90, "max": 5.20, "unit": "V"},
    "v_fb_steady":     {"name": "Feedback_Reference",     "min": 0.58, "max": 0.62, "unit": "V"},
    "v_sw_peak":       {"name": "SW_Node_Peak_Voltage",   "min": 5.00, "max": 6.00, "unit": "V"},
    "v_out_ripple":    {"name": "Output_Voltage_Ripple",  "min": 0.00, "max": 0.25, "unit": "V"}
}

def parse_dut_topology(json_path, module_name, dut_name):
    if not os.path.exists(json_path):
        return {}
        
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return {}
            
    target_module = data.get(module_name, [])
    dut_nets = {}
    
    # Dynamic capture: if JSON is incorrect, an empty dictionary will be returned.
    for net in target_module:
        net_id = net.get("net_id", "")
        for conn in net.get("Connections", []):
            if conn.get("ComponentID") == dut_name:
                dut_nets[conn.get("PinName")] = net_id
                
    return dut_nets

def build_netlist():
    dut_nets = parse_dut_topology(JSON_FILE, "TSP61022 5V Boost Circuit", "TPS61022")

    # When no connection is found, assign random floating nodes to isolate the DUT.
    dut_vin  = dut_nets.get("VIN", f"NC_VIN_{uuid.uuid4().hex[:4]}")
    dut_en   = dut_nets.get("EN", f"NC_EN_{uuid.uuid4().hex[:4]}")
    dut_sw   = dut_nets.get("SW", f"NC_SW_{uuid.uuid4().hex[:4]}")
    dut_vout = dut_nets.get("VOUT", f"NC_VOUT_{uuid.uuid4().hex[:4]}")
    dut_fb   = dut_nets.get("FB", f"NC_FB_{uuid.uuid4().hex[:4]}")
    dut_gnd  = dut_nets.get("GND", f"NC_GND_{uuid.uuid4().hex[:4]}")

    def sp(n): return "0" if n in ["net_gnd", "0"] else n

    netlist = [
        "* TPS61022 5V Synchronous Boost Behavioral Audit (Strictly Hardened)",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 10n 2m 0 uic",
        
        "* ==========================================",
        "* TESTBENCH: Fixed External Testbed Network",
        "* ==========================================",
        "V_VSYS net_vsys 0 3.3V",
        "R50 net_vsys net_en 0.001",
        "L21 net_vsys net_sw 1uH",
        "* Ultimate Defense: 1GΩ dummy resistor to prevent Singular Matrix collapse if chip is missing",
        "R_DUMMY_SW net_sw 0 1G",
        "C75 net_vout 0 47uF IC=3.3",
        "C76 net_vout 0 47uF IC=3.3",
        "C66 net_vout 0 22uF IC=3.3",
        "R52 net_vout net_fb 750k",
        "R38 net_fb 0 100k",
        "R_LOAD net_vout 0 5",
        
        "* ==========================================",
        "* DUT: Connection points dynamically injected by JSON",
        "* ==========================================",
        f"X_U20 {sp(dut_vin)} {sp(dut_sw)} {sp(dut_gnd)} {sp(dut_vout)} {sp(dut_fb)} {sp(dut_en)} {sp(dut_vin)} TPS61022_MACRO",
        
        ".subckt TPS61022_MACRO VIN SW GND VOUT FB EN MODE",
        "Vosc osc 0 PULSE(0 1 0 5n 5n 240n 500n)",
        "B_ea ea 0 V=limit((0.6 - V(FB))*50, 0, 0.95)",
        "B_pwm pwm 0 V=V(osc)<V(ea) & V(EN)>1.2 ? 1 : 0",
        "S_LS SW GND pwm 0 SW_MOD",
        "S_HS SW VOUT n_pwm 0 SW_MOD",
        "B_npwm n_pwm 0 V=V(EN)>1.2 & V(pwm)<0.5 ? 1 : 0",
        ".model SW_MOD SW(Ron=0.06 Roff=1Meg Vt=0.5 Vh=-0.1)",
        ".ends",
        
        "* ==========================================",
        "* Automatic Measurement Probes",
        "* ==========================================",
        ".meas TRAN v_in_steady AVG V(net_vsys) FROM 1.5m TO 2.0m",
        ".meas TRAN v_out_steady AVG V(net_vout) FROM 1.5m TO 2.0m",
        ".meas TRAN v_fb_steady AVG V(net_fb) FROM 1.5m TO 2.0m",
        ".meas TRAN v_sw_peak MAX V(net_sw) FROM 1.5m TO 2.0m",
        ".meas TRAN v_out_max MAX V(net_vout) FROM 1.5m TO 2.0m",
        ".meas TRAN v_out_min MIN V(net_vout) FROM 1.5m TO 2.0m",
        ".meas TRAN v_out_ripple PARAM v_out_max-v_out_min",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    # Fix 1: Force cleanup of all old simulation logs and reports before execution!
    for file in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(file):
            os.remove(file)
            
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: 
            f.write(build_netlist())
            
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
        # Fix 2: If the engine crashes and no log is generated, directly judge as failure.
        if not os.path.exists(LOG_FILE):
            print("FATAL ERROR: Simulation engine crashed and aborted, no log file generated. Potential serious open circuit in topology.")
            return

        with open(LOG_FILE, 'r', errors='ignore') as f: 
            log = f.read()

        results = {}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            if m:
                results[k] = float(m.group(1))
            else:
                results[k] = None

        report_lines = []
        report_lines.append("---------------------------------------------------------")
        report_lines.append(f"{'Audit Item':<28} | {'Value':<12} | {'Status'}")
        report_lines.append("---------------------------------------------------------")

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results.get(k)
            is_ok = spec["min"] <= val <= spec["max"] if val is not None else False
            if is_ok: 
                pass_count += 1
            status = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3f} {spec['unit']}" if val is not None else "N/A"
            report_lines.append(f"{spec['name']:<28} | {val_str:<12} | {status}")

        report_lines.append("---------------------------------------------------------")
        rate = (pass_count / len(TEST_CRITERIA)) * 100
        report_lines.append(f"Pass Rate: {rate:.1f}%")
        
        final_report = "\n".join(report_lines)
        print(final_report)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_report)

    except Exception as e: 
        print(f"Simulation execution failed: {e}")

if __name__ == "__main__": 
    run_simulation()