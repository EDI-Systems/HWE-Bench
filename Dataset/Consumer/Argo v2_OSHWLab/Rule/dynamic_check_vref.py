import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_vref.json")
CIR_FILE  = os.path.join(BASE_DIR, "tlv_vref_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "tlv_vref_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "tlv_vref_audit_report.txt")

TEST_CRITERIA = {
    "v_in_usb":   {"name": "LDO_IN_Voltage_USB_Mode", "min": 4.50, "max": 5.00, "unit": "V"},
    "v_in_bat":   {"name": "LDO_IN_Voltage_BAT_Mode", "min": 3.40, "max": 5.00, "unit": "V"},
    "v_out_usb":  {"name": "VREF_Output_USB_Mode",    "min": 3.25, "max": 3.35, "unit": "V"},
    "v_out_bat":  {"name": "VREF_Output_BAT_Mode",    "min": 3.25, "max": 3.35, "unit": "V"},
    "v_out_sag":  {"name": "VREF_Transient_Sag",      "min": 3.10, "max": 3.35, "unit": "V"}
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
    
    for net in target_module:
        net_id = net.get("net_id", "")
        for conn in net.get("Connections", []):
            if conn.get("ComponentID") == dut_name:
                dut_nets[conn.get("PinName")] = net_id
                
    return dut_nets

def build_netlist():
    # Independently extract the topology mapping of the two key chips
    nets_bat54c = parse_dut_topology(JSON_FILE, "3.3V VREF Circuit", "BAT54C")
    nets_tlv    = parse_dut_topology(JSON_FILE, "3.3V VREF Circuit", "TLV70430")

    # BAT54C dynamic pin allocation (if undefined, assign random floating nodes)
    dut_bat_a1 = nets_bat54c.get("A1", f"NC_A1_{uuid.uuid4().hex[:4]}")
    dut_bat_a2 = nets_bat54c.get("A2", f"NC_A2_{uuid.uuid4().hex[:4]}")
    dut_bat_k  = nets_bat54c.get("K",  f"NC_K_{uuid.uuid4().hex[:4]}")

    # TLV70430 dynamic pin allocation
    dut_tlv_in  = nets_tlv.get("IN",  f"NC_IN_{uuid.uuid4().hex[:4]}")
    dut_tlv_out = nets_tlv.get("OUT", f"NC_OUT_{uuid.uuid4().hex[:4]}")
    dut_tlv_gnd = nets_tlv.get("GND", f"NC_GND_{uuid.uuid4().hex[:4]}")

    def sp(n): return "0" if n in ["net_gnd", "0"] else n

    netlist = [
        "* TLV70430 3.3V VREF OR-ing Full Process Transient Audit (Strictly Hardened)",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 10u 6m 0 uic",
        
        "* ==========================================",
        "* TESTBENCH: Fixed External Testbed and Stimulus Network",
        "* ==========================================",
        "* VBUS USB Hot-swap Event Simulation (5V -> 0V -> 5V)",
        "V_VBUS net_vbus 0 PWL(0 5 2m 5 2.01m 0 4m 0 4.01m 5 6m 5)",
        "* VBAT Battery Steady-state Power Supply",
        "V_VBAT net_vbat 0 4.0V",
        
        "* Schematic peripheral bypass capacitors and system load",
        "C58 net_ldo_in 0 1uF IC=4.7",
        "C59 net_vref 0 4.7uF IC=3.3",
        "R_LOAD net_vref 0 330",
        
        "* Ultimate Defense: 1GΩ dummy resistor to prevent Singular Matrix error if DUT is missing",
        "R_DUM_IN net_ldo_in 0 1G",
        "R_DUM_OUT net_vref 0 1G",
        
        "* ==========================================",
        "* DUT: Connection points dynamically injected by JSON",
        "* ==========================================",
        "* DUT 1: BAT54C Schottky OR gate",
        f"D1 {sp(dut_bat_a1)} {sp(dut_bat_k)} D_BAT54",
        f"D2 {sp(dut_bat_a2)} {sp(dut_bat_k)} D_BAT54",
        ".model D_BAT54 D(Is=1u Rs=0.5 N=1.05 Cjo=10p)",
        
        "* DUT 2: TLV70430 3.3V Voltage Regulator",
        f"X_LDO {sp(dut_tlv_in)} {sp(dut_tlv_gnd)} {sp(dut_tlv_out)} TLV70430_MACRO",
        ".subckt TLV70430_MACRO IN GND OUT",
        "B_LDO OUT GND V=limit(V(IN)-0.1, 0, 3.3)",
        "R_OUT OUT GND 1Meg",
        ".ends",
        
        "* ==========================================",
        "* Automatic Measurement Probes (Bound to physical testbed nodes)",
        "* ==========================================",
        ".meas TRAN v_in_usb AVG V(net_ldo_in) FROM 1m TO 1.9m",
        ".meas TRAN v_in_bat AVG V(net_ldo_in) FROM 3m TO 3.9m",
        ".meas TRAN v_out_usb AVG V(net_vref) FROM 1m TO 1.9m",
        ".meas TRAN v_out_bat AVG V(net_vref) FROM 3m TO 3.9m",
        ".meas TRAN v_out_sag MIN V(net_vref) FROM 1m TO 5m",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    # Force cleanup of all old files to prevent ghost logs from causing false positives.
    for file in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(file):
            try:
                os.remove(file)
            except OSError:
                pass
            
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: 
            f.write(build_netlist())
            
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
        # If simulation crashes and no log is generated, intercept the error.
        if not os.path.exists(LOG_FILE):
            print("FATAL ERROR: Simulation engine aborted, no log file generated. Please check the JSON topology network.")
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