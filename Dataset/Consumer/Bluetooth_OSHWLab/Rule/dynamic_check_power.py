import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE  = os.path.join(BASE_DIR, "power_strict_diagnostic.net")
LOG_FILE  = os.path.join(BASE_DIR, "power_strict_diagnostic.log")
REPORT_FILE = os.path.join(BASE_DIR, "power_strict_report.txt")

# Modified judgment criteria: Introduced Schottky diode voltage drops and short-circuit anti-cheat
TEST_CRITERIA = {
    "v_usb_in":   {"name": "[1] TYPE-C_VBUS_Entry (5V)",  "min": 4.90, "max": 5.10, "unit": "V"},
    "v_chrg_vcc": {"name": "[2] TP4054_VCC_Drop Test",    "min": 4.50, "max": 4.85, "unit": "V"},
    "i_chrg_bat": {"name": "[3] Charge_Current (500mA)",  "min": 0.45, "max": 0.55, "unit": "A"},
    "v_mcu_vbat": {"name": "[4] AC6955F_VBAT_Receiving",  "min": 3.70, "max": 3.90, "unit": "V"} 
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
            # Fuzzy match to support AC6955F, AC6955F4, etc.
            if component_id in str(conn.get("ComponentID", "")):
                target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def build_netlist():
    nets_usb  = parse_module_topology(JSON_FILE, "Power Management & Battery Charging Module", "TYPE-C")
    nets_dio  = parse_module_topology(JSON_FILE, "Power Management & Battery Charging Module", "1N5819WS")
    nets_chrg = parse_module_topology(JSON_FILE, "Power Management & Battery Charging Module", "TP4054")
    nets_mcu  = parse_module_topology(JSON_FILE, "Power Management & Battery Charging Module", "AC6955F")

    def get_net(nets_dict, pin_name, comp_name):
        if not nets_dict or pin_name not in nets_dict:
            return f"NC_{uuid.uuid4().hex[:5]}"
        return nets_dict[pin_name]

    net_vbus  = get_net(nets_usb, "VBUS", "TYPE-C")
    net_dio_a = get_net(nets_dio, "Anode", "1N5819WS")
    net_dio_k = get_net(nets_dio, "Cathode", "1N5819WS")
    net_vcc   = get_net(nets_chrg, "VCC", "TP4054")
    net_bat   = get_net(nets_chrg, "BAT", "TP4054")
    net_mcu   = get_net(nets_mcu, "VBAT", "AC6955F")

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Power Management Diagnostic Audit - Physics Tuned",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        "* Physical Correction 1: Remove 'uic' to allow LTspice to automatically calculate DC bias",
        ".tran 10u 20m 0",
        
        "* Physical Correction 2: Dummy resistors increased to 1G to eliminate system impedance effects",
        f"R_D1 {sp(net_vbus)} 0 1G", f"R_D2 {sp(net_dio_a)} 0 1G",
        f"R_D3 {sp(net_dio_k)} 0 1G", f"R_D4 {sp(net_vcc)} 0 1G",
        f"R_D5 {sp(net_bat)} 0 1G", f"R_D6 {sp(net_mcu)} 0 1G",

        "* Simulate USB input: 5V DC",
        f"V_USB {sp(net_vbus)} 0 5V",
        f".meas TRAN v_usb_in AVG V({sp(net_vbus)}) FROM 10m TO 20m",

        "* Simulate 3.8V Li-ion voltage and MCU system load",
        f"V_BAT net_bat_real 0 3.8V",
        f"V_SENSE {sp(net_bat)} net_bat_real 0V", 
        f"R_MCU {sp(net_mcu)} 0 10k",
    ]

    # * Physical Correction 3: Topology anti-cheat interception
    # Verifies if space was actually reserved for the diode and charger IC topology
    is_missing_dio = ("NC_" in net_dio_a or "NC_" in net_dio_k)
    is_shorted_dio = (net_dio_a == net_dio_k and not is_missing_dio)
    is_missing_chrg = ("NC_" in net_vcc or "NC_" in net_bat)
    is_shorted_chrg = (net_vcc == net_bat and not is_missing_chrg)

    # Inject golden standard components only if the netlist is valid
    if not is_missing_dio and not is_shorted_dio:
        netlist.append(f"D_PROT {sp(net_dio_a)} {sp(net_dio_k)} D_1N5819")
        netlist.append(".model D_1N5819 D(Is=3e-6 N=1.04 Rs=0.08 eg=0.69)")

    if not is_missing_chrg and not is_shorted_chrg:
        netlist.append(f"B_CHRG {sp(net_vcc)} {sp(net_bat)} I=(V({sp(net_vcc)})>4.0 ? 0.5 : 0)")

    netlist.extend([
        f".meas TRAN v_chrg_vcc AVG V({sp(net_vcc)}) FROM 10m TO 20m",
        f".meas TRAN i_chrg_bat AVG I(V_SENSE) FROM 10m TO 20m",
        f".meas TRAN v_mcu_vbat AVG V({sp(net_mcu)}) FROM 10m TO 20m",
        ".end"
    ])
    return "\n".join(netlist)

def run_simulation():
    # Clean up old files before each run
    for f in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(f): os.remove(f)
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        if not os.path.exists(LOG_FILE): return
        
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()
        results = {k: None for k in TEST_CRITERIA}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            if m: results[k] = float(m.group(1))
        
        report = ["="*65, " POWER MANAGEMENT DIAGNOSTIC AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3g} {spec['unit']}" if val is not None else "0.0 V"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: 
            f.write(final_report_str)
            
    except Exception as e: 
        print(f"Error: {e}")

if __name__ == "__main__": run_simulation()