import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_power.json")

CIR_FILE  = os.path.join(BASE_DIR, "power_arbitration_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "power_arbitration_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "power_arbitration_report.txt")

TARGET_MODULE = "Dual-Input Power Arbitration Network"

# Judgment Standards: Covers dual-source independent supply and reverse-current protection tests
TEST_CRITERIA = {
    "v_eeprom_hdmi": {"name": "[1] EEPROM_VCC (HDMI Only)",    "min": 4.50, "max": 4.85, "unit": "V"},
    "v_eeprom_usb":  {"name": "[2] EEPROM_VCC (USB Only)",     "min": 4.50, "max": 4.85, "unit": "V"},
    "v_eeprom_dual": {"name": "[3] EEPROM_VCC (Dual Active)",  "min": 4.70, "max": 5.05, "unit": "V"},
    # Anti-cheat: When USB(5.2V) is higher than HDMI(4.8V), reverse current into HDMI must be nearly zero
    "i_leak_hdmi":   {"name": "[4] HDMI_Reverse_Leakage",      "min": -0.0001, "max": 0.0001, "unit": "A"} 
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
    print(f"Auditing Core Power Domain: {TARGET_MODULE}")
    
    nets_hdmi   = parse_module_topology(JSON_FILE, TARGET_MODULE, "HDMI-01")
    nets_usb    = parse_module_topology(JSON_FILE, TARGET_MODULE, "GT-USB-7010ASV")
    nets_eeprom = parse_module_topology(JSON_FILE, TARGET_MODULE, "AT24C32")

    def get_net(nets_dict, pin_aliases):
        for alias in pin_aliases:
            if alias in nets_dict: return nets_dict[alias]
        return f"NC_{uuid.uuid4().hex[:5]}"

    # Extract core power nodes
    net_hdmi_5v  = get_net(nets_hdmi, ["+5V_Power", "18"])
    net_usb_5v   = get_net(nets_usb, ["VBUS", "A4", "A9", "B4", "B9"])
    net_eeprom   = get_net(nets_eeprom, ["VCC", "8"])

    # --- Physical Correction 3: Topology Anti-Cheat (Verifies isolation gap for dual diodes) ---
    is_missing = ("NC_" in net_hdmi_5v or "NC_" in net_usb_5v or "NC_" in net_eeprom)
    # HDMI/USB shorted, or direct connection between source and EEPROM, are fatal errors
    is_shorted = (net_hdmi_5v == net_usb_5v) or (net_hdmi_5v == net_eeprom) or (net_usb_5v == net_eeprom)

    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (Source or load not fully connected)"
    elif is_shorted:
        status_info = "CRITICAL FAIL: Fatal Power Short! (BAT54 isolation diodes not detected)"
    else:
        status_info = "TOPOLOGY PASS: Secure power isolation gap found, preparing ORing logic injection"

    print(f"  [JUDGMENT] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Power Arbitration Diagnostic Audit - Transient Physics",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 30m 0",
        
        "* Physical Correction 1: 1G dummy resistors to maintain matrix stability for floating nodes",
        f"R_D1 {sp(net_hdmi_5v)} 0 1G", f"R_D2 {sp(net_usb_5v)} 0 1G",
        f"R_D3 {sp(net_eeprom)} 0 1G",

        "* Simulate 3-stage power sequencing",
        "* 0-10ms: HDMI Only (5V) | 10-20ms: USB Only (5V) | 20-30ms: HDMI(4.8V) + USB(5.2V) hot-swap contention",
        f"V_HDMI {sp(net_hdmi_5v)} 0 PWL(0 5V 10m 5V 10.01m 0V 20m 0V 20.01m 4.8V 30m 4.8V)",
        f"V_USB  {sp(net_usb_5v)} 0 PWL(0 0V 10m 0V 10.01m 5V 20m 5V 20.01m 5.2V 30m 5.2V)",
        
        "* Simulate EEPROM and system static power load (~1mA)",
        f"R_EEPROM {sp(net_eeprom)} 0 5k",
    ]

    # Inject BAT54 Schottky OR-ing logic only if the topology is valid
    if not is_missing and not is_shorted:
        netlist.extend([
            "* Injecting Golden Standard dual Schottky diode OR-ing logic (Simulating BAT54C)",
            f"D_HDMI {sp(net_hdmi_5v)} {sp(net_eeprom)} D_BAT54",
            f"D_USB  {sp(net_usb_5v)} {sp(net_eeprom)} D_BAT54",
            ".model D_BAT54 D(Is=2e-6 N=1.02 Rs=0.5 Eg=0.69)"
        ])

    netlist.extend([
        "* Measurement Probes",
        f".meas TRAN v_eeprom_hdmi AVG V({sp(net_eeprom)}) FROM 2m TO 8m",
        f".meas TRAN v_eeprom_usb  AVG V({sp(net_eeprom)}) FROM 12m TO 18m",
        f".meas TRAN v_eeprom_dual AVG V({sp(net_eeprom)}) FROM 22m TO 28m",
        "* Measure reverse leakage current back to HDMI source during dual-supply phase",
        f".meas TRAN i_leak_hdmi   AVG I(V_HDMI) FROM 22m TO 28m",
        ".end"
    ])
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
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            if m: results[k] = float(m.group(1))
        
        report = ["="*65, " POWER ARBITRATION DIAGNOSTIC AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>8.3g} {spec['unit']}" if val is not None else "0.0 V/A"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: 
            f.write(final_report_str)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()