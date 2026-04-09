import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_usb.json")
CIR_FILE  = os.path.join(BASE_DIR, "usb_esd_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "usb_esd_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "usb_esd_audit_report.txt")

TEST_CRITERIA = {
    "v_vbus_steady":   {"name": "VBUS_Steady_Voltage",  "min": 4.5,  "max": 5.2,  "unit": "V"},
    "i_led_steady":    {"name": "LED_Steady_Current",   "min": 10.0, "max": 25.0, "unit": "mA"},
    "v_dp_clamp":      {"name": "DP_ESD_Clamp_Voltage", "min": 0.0,  "max": 15.0, "unit": "V"},
    "v_dn_clamp":      {"name": "DN_ESD_Clamp_Voltage", "min": 0.0,  "max": 15.0, "unit": "V"},
    "v_sys_surge":     {"name": "SYS_5V_Surge_Limit",   "min": 0.0,  "max": 8.0,  "unit": "V"}
}

def get_topology():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError("JSON File not found.")
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("Protected USB Interface & Power Supply", [])
    pin_to_nets = {}
    for net in target:
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            if key not in pin_to_nets: pin_to_nets[key] = []
            if net["net_id"] not in pin_to_nets[key]: pin_to_nets[key].append(net["net_id"])
            
    def fetch(comp, pin):
        res = pin_to_nets.get(f"{comp}:{pin}", [])
        if not res:
            return [f"NC_{uuid.uuid4().hex[:4]}"]
        return res
    return fetch

def build_netlist():
    fetch = get_topology()

    n_usb_vbus = fetch("USB", "VCC / VBUS")[0]
    n_sys_5v   = fetch("USBLC6-2SC6", "VBUS")[0]
    n_dp       = fetch("USB", "D+")[0]
    n_dn       = fetch("USB", "D-")[0]
    n_gnd      = fetch("USB", "GND")[0]

    def sp(n): return "0" if n == n_gnd else n

    netlist = [
        "* USB ESD Protection Behavioral Audit",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 1n 15u 0 uic",
        
        "* Testbench Power Supply and Normal Data Signals",
        f"V_USB_PWR {sp(n_usb_vbus)} 0 5V",
        f"V_DP_SIG {sp(n_dp)} 0 PULSE(0 3.3 1u 10n 10n 2u 4u)",
        f"V_DN_SIG {sp(n_dn)} 0 PULSE(3.3 0 1u 10n 10n 2u 4u)",
        
        "* Testbench IEC 61000-4-2 8kV ESD Pulse Simulation",
        f"I_ESD_DP 0 {sp(n_dp)} PWL(0 0 5u 0 5.001u 30 5.030u 15 5.100u 0)",
        f"I_ESD_DN 0 {sp(n_dn)} PWL(0 0 10u 0 10.001u 30 10.030u 15 10.100u 0)",
        
        "* Testbench PTC Fuse Equivalent",
        f"R_PTC {sp(n_usb_vbus)} {sp(n_sys_5v)} 0.1",
        
        "* Testbench System Load and Bypass Capacitor",
        f"R_SYS_LOAD {sp(n_sys_5v)} 0 100",
        f"C_SYS_BYPASS {sp(n_sys_5v)} 0 0.1u",
        
        "* Testbench LED Indicator Circuit",
        f"R_LED {sp(n_sys_5v)} N_LED_A 150",
        "D_LED N_LED_A 0 D_RED",
        ".model D_RED D(Is=1e-18 N=1.5 Rs=5 Xti=3 Eg=2.1)",
        
        "* USBLC6-2SC6 Equivalent Macro Model",
        f"D_DP_GND 0 {sp(n_dp)} D_ESD",
        f"D_DP_VBUS {sp(n_dp)} {sp(n_sys_5v)} D_ESD",
        f"D_DN_GND 0 {sp(n_dn)} D_ESD",
        f"D_DN_VBUS {sp(n_dn)} {sp(n_sys_5v)} D_ESD",
        f"D_TVS_VBUS 0 {sp(n_sys_5v)} D_TVS",
        
        ".model D_ESD D(Cjo=1.5p Rs=0.5)",
        ".model D_TVS D(BV=6 IBV=1m Cjo=10p Rs=0.1)",
        
        "* Automated Measurements",
        f".meas TRAN v_vbus_steady AVG V({sp(n_sys_5v)}) FROM 2u TO 4u",
        ".meas TRAN i_led_steady AVG ABS(I(R_LED)) FROM 2u TO 4u",
        f".meas TRAN v_dp_clamp MAX V({sp(n_dp)}) FROM 4.9u TO 5.5u",
        f".meas TRAN v_dn_clamp MAX V({sp(n_dn)}) FROM 9.9u TO 10.5u",
        f".meas TRAN v_sys_surge MAX V({sp(n_sys_5v)}) FROM 4.9u TO 11u",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: 
            f.write(build_netlist())
            
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
        with open(LOG_FILE, 'r', errors='ignore') as f: 
            log = f.read()

        results = {}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m:
                val = float(m.group(1))
                if "i_" in k: val = val * 1000 
                results[k] = val
            else:
                results[k] = None

        report_lines = []
        report_lines.append("---------------------------------------------------------")
        report_lines.append(f"{'Audit Item':<30} | {'Value':<15} | {'Status'}")
        report_lines.append("---------------------------------------------------------")

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results.get(k)
            is_ok = spec["min"] <= val <= spec["max"] if val is not None else False
            if is_ok: 
                pass_count += 1
            status = "PASS" if is_ok else "FAIL"
            val_str = f"{val:>11.3f} {spec['unit']}" if val is not None else "N/A"
            report_lines.append(f"{spec['name']:<30} | {val_str:<15} | {status}")

        report_lines.append("---------------------------------------------------------")
        rate = (pass_count / len(TEST_CRITERIA)) * 100
        report_lines.append(f"passrate: {rate:.1f}%")
        
        final_report = "\n".join(report_lines)
        print(final_report)
        
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_report)

    except Exception as e: 
        print(f"Simulation Error: {e}")

if __name__ == "__main__": 
    run_simulation()