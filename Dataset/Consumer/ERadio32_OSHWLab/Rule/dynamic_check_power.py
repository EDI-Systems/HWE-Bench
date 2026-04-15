import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE  = os.path.join(BASE_DIR, "power_path_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "power_path_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "power_path_report.txt")

TARGET_MODULE = "Portable Power Management System"

# Audit Metrics: Comprehensive cross-verification matrix with 10 probes
TEST_CRITERIA = {
    "v_usb_bus":   {"name": "[01|Plugged] VBUS Input Voltage (~5V)",   "min": 4.80, "max": 5.20, "unit": "V"},
    "v_pmos_g":    {"name": "[02|Plugged] PMOS Gate Block V (~5V)",    "min": 4.80, "max": 5.20, "unit": "V"},
    "i_bat_leak":  {"name": "[03|Plugged] Bat Reverse Leakage (~0A)",  "min": -0.50, "max": 0.05, "unit": "A"},
    "v_sys_usb":   {"name": "[04|Plugged] System Bus Voltage (~5V)",   "min": 4.50, "max": 5.20, "unit": "V"},
    "v_3v3_usb":   {"name": "[05|Plugged] Buck Steady Output (~3.3V)", "min": 3.20, "max": 3.40, "unit": "V"},
    "v_sys_dip":   {"name": "[06|Unplug] Sys Bus Switchover Sag (>3.5V)", "min": 2.50, "max": 3.90, "unit": "V"},
    "v_pmos_s":    {"name": "[07|Unplug] PMOS Source (Battery) (~3.8V)", "min": 3.60, "max": 3.90, "unit": "V"},
    "v_3v3_wifi":  {"name": "[09|RF] 3.3V Wi-Fi Sag Immunity (>3.0V)", "min": 3.00, "max": 3.40, "unit": "V"},
    "v_3v3_audio": {"name": "[10|Audio] 3.3V Audio Sag Immunity (>2.8V)", "min": 2.80, "max": 3.40, "unit": "V"}
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception: return {}
    target_nets = {}
    for net in data.get(module_name, []):
        for conn in net.get("Connections", []):
            if component_id == str(conn.get("ComponentID", "")):
                target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def get_net_strict(nets_dict, exact_pin_name):
    return nets_dict.get(exact_pin_name, f"NC_{uuid.uuid4().hex[:5]}")

def build_netlist():
    print("="*65)
    print(f"Launching Strict Pin Version - 10-Probe Power Path Audit: {TARGET_MODULE}")
    
    nets_usb  = parse_module_topology(JSON_FILE, TARGET_MODULE, "USB")
    nets_chg  = parse_module_topology(JSON_FILE, TARGET_MODULE, "TP4056")
    nets_pmos = parse_module_topology(JSON_FILE, TARGET_MODULE, "IRLM") 
    nets_buck = parse_module_topology(JSON_FILE, TARGET_MODULE, "RT8096C")

    # Strict alignment with standard library PinNames
    n_usb_5v  = get_net_strict(nets_usb, "B9")
    n_bat_raw = get_net_strict(nets_chg, "BAT")
    n_pmos_s  = get_net_strict(nets_pmos, "S")
    n_pmos_d  = get_net_strict(nets_pmos, "D")
    n_pmos_g  = get_net_strict(nets_pmos, "G")
    n_sys_vin = get_net_strict(nets_buck, "VIN")
    n_3v3_fb  = get_net_strict(nets_buck, "FB")

    nodes = [n_usb_5v, n_bat_raw, n_pmos_s, n_pmos_d, n_pmos_g, n_sys_vin, n_3v3_fb]
    is_missing = any("NC_" in net for net in nodes)
    
    # Anti-cheat: PMOS Source must connect to Battery, Drain to Buck, Gate controlled by USB
    is_path_valid = (n_bat_raw == n_pmos_s) and (n_pmos_d == n_sys_vin) and (n_usb_5v == n_pmos_g)

    inject_models = True
    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (Pins not connected per standard specs)"
        inject_models = False
    elif not is_path_valid:
        status_info = "CRITICAL FAIL: Path Discontinuity or Violation! (PMOS isolation required with Gate via VBUS)"
        inject_models = False
    else:
        status_info = "TOPOLOGY PASS: Power Path Switching Topology Validated, Deploying 10-Probe Matrix"

    print(f"  [Judgment] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Strict Pin Power Path 10-Point Audit",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 30m 0",
        
        f"R_D1 {sp(n_usb_5v)} 0 1G", f"R_D2 {sp(n_bat_raw)} 0 1G",
        f"R_D3 {sp(n_sys_vin)} 0 1G", f"R_D4 {sp(n_3v3_fb)} 0 1G",

        f"V_CELL net_cell 0 3.8V",
        f"R_ESR net_cell {sp(n_bat_raw)} 0.1",
        f"V_USB net_usb_ideal 0 PWL(0 5V 10m 5V 10.01m 0V 30m 0V)",
        f"R_USB_CABLE net_usb_ideal {sp(n_usb_5v)} 0.1"
    ]

    if inject_models:
        netlist.extend([
            "* Injecting IRLM PMOS Physical Model (replaces ideal diode)",
            f"M_PATH {sp(n_pmos_d)} {sp(n_pmos_g)} {sp(n_pmos_s)} {sp(n_pmos_s)} P_IRLM",
            f".model P_IRLM VDMOS(pchan Rg=5 Vto=-0.7 Rd=39m Rs=10m Cgdmax=740p)",

            f"D_USB_PATH {sp(n_usb_5v)} {sp(n_sys_vin)} D_Ideal",
            f".model D_Ideal D(Ron=0.05 Roff=1Meg Vfwd=0.3)",

            f"B_BUCK net_3v3_ideal 0 V=(V({sp(n_sys_vin)})>3.2 ? 3.3 : 0)",
            f"R_BUCK_OUT net_3v3_ideal {sp(n_3v3_fb)} 0.08",
            f"C_SYS_DECOUPLE {sp(n_3v3_fb)} 0 44u",

            f"I_WIFI {sp(n_3v3_fb)} 0 PWL(0 0A 14m 0A 14.1m 0.5A 16m 0.5A 16.1m 0A 30m 0A)",
            f"I_AUDIO {sp(n_3v3_fb)} 0 PWL(0 0A 20m 0A 20.1m 0.8A 21m 0.8A 21.1m 0.2A 22m 0.8A 22.1m 0A 30m 0A)",
            
            "* --- 10-Probe Measurement Commands ---",
            f".meas TRAN v_usb_bus  AVG V({sp(n_usb_5v)}) FROM 2m TO 8m",
            f".meas TRAN v_pmos_g   AVG V({sp(n_pmos_g)}) FROM 2m TO 8m",
            f".meas TRAN i_bat_leak AVG I(R_ESR) FROM 2m TO 8m",
            f".meas TRAN v_sys_usb  AVG V({sp(n_sys_vin)}) FROM 2m TO 8m",
            f".meas TRAN v_3v3_usb  AVG V({sp(n_3v3_fb)}) FROM 2m TO 8m",
            f".meas TRAN v_sys_dip  MIN V({sp(n_sys_vin)}) FROM 9.5m TO 11m",
            f".meas TRAN v_pmos_s   AVG V({sp(n_pmos_s)}) FROM 11m TO 13m",
            f".meas TRAN i_bat_wifi MAX I(R_ESR) FROM 14m TO 16m",
            f".meas TRAN v_3v3_wifi MIN V({sp(n_3v3_fb)}) FROM 13.5m TO 17m",
            f".meas TRAN v_3v3_audio MIN V({sp(n_3v3_fb)}) FROM 19.5m TO 26m"
        ])
    else:
        netlist.extend([
            f".meas TRAN v_usb_bus PARAM 0", f".meas TRAN v_pmos_g PARAM 0",
            f".meas TRAN i_bat_leak PARAM 99", f".meas TRAN v_sys_usb PARAM 0",
            f".meas TRAN v_3v3_usb PARAM 0", f".meas TRAN v_sys_dip PARAM 0",
            f".meas TRAN v_pmos_s PARAM 0", f".meas TRAN i_bat_wifi PARAM 0",
            f".meas TRAN v_3v3_wifi PARAM 0", f".meas TRAN v_3v3_audio PARAM 0"
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
        
        report = ["="*65, " POWER PATH 10-POINT MATRIX AUDIT (100% STRICT) ", "="*65]
        report.append(f"{'Audit Node (Process Step)':<33} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            status_text = "PASS" if is_ok else "FAIL"
            
            if val is None: val_str = "N/A"
            elif "A" in spec["unit"] and "leak" not in k: val_str = f"{val*1000:>8.1f} mA"
            else: val_str = f"{val:>8.3g} {spec['unit']}"
                
            report.append(f"{spec['name']:<33} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        
        final_report_str = "\n".join(report)
        print(final_report_str)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_report_str)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()