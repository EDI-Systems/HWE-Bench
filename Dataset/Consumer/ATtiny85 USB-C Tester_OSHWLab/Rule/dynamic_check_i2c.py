import os
import subprocess
import re
import json
import uuid

LTSPICE_EXE = "D:/app/LTspice/LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct","dynamic_i2c.json")
CIR_FILE  = os.path.join(BASE_DIR, "i2c_strict_diagnostic.net")
LOG_FILE  = os.path.join(BASE_DIR, "i2c_strict_diagnostic.log")
REPORT_FILE = os.path.join(BASE_DIR, "i2c_strict_report.txt")

# --- 2. Fine-grained Audit Metrics (Step-by-step detection points) ---
TEST_CRITERIA = {
    # Power link step-by-step audit
    "v_usb_in":      {"name": "USB VBUS Input",        "min": 8.50, "max": 9.50, "unit": "V"},
    "v_ldo_out":     {"name": "LDO 7805 Output",       "min": 4.80, "max": 5.20, "unit": "V"},
    
    # Sampling link
    "v_shunt_drop":  {"name": "Shunt 8mOhm Sense",     "min": 0.015, "max": 0.017, "unit": "V"},
    
    # I2C link step-by-step audit
    "i2c_mcu_low":   {"name": "I2C MCU Side (Low)",    "min": 0.00, "max": 0.60, "unit": "V"}
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path): return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except: return {}
    for mod in data.get("Functional Modules", []):
        if mod.get("Module Name") == module_name:
            target_nets = {}
            for net in mod.get("Nets", []):
                for conn in net.get("Connections", []):
                    if conn.get("ComponentID") == component_id:
                        target_nets[conn.get("PinName")] = net.get("net_id", "")
            return target_nets
    return {}

def build_netlist():
    # Strictly extract from functional modules
    nets_usb = parse_module_topology(JSON_FILE, "USB-C Power Input & Regulation", "USB1")
    nets_pwr = parse_module_topology(JSON_FILE, "USB-C Power Input & Regulation", "U3")
    nets_sns = parse_module_topology(JSON_FILE, "High-Side Current/Power Sensing", "INA219")
    nets_mcu = parse_module_topology(JSON_FILE, "Microcontroller & User Interface", "ATtiny85")

    # UUID Isolation: Assign a unique random node if the pin is missing
    def get_net(nets_dict, pin_name):
        return nets_dict.get(pin_name, f"NC_{uuid.uuid4().hex[:5]}")

    # Extract and decouple nodes
    net_usb_vbus = get_net(nets_usb, "VBUS")
    net_ldo_out  = get_net(nets_pwr, "OUTPUT") # 78L05 Pin Name
    net_mcu_vcc  = get_net(nets_mcu, "VCC")
    
    net_sns_inp  = get_net(nets_sns, "IN+")
    net_sns_inn  = get_net(nets_sns, "IN-")
    
    net_mcu_sda  = get_net(nets_mcu, "PB0")
    net_sns_sda  = get_net(nets_sns, "SDA")

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* I2C Strict Diagnostic Topology Audit",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 20m 0 uic",
        
        # Bleeding resistors to prevent floating node errors
        f"R_D1 {sp(net_usb_vbus)} 0 1Meg", f"R_D2 {sp(net_ldo_out)} 0 1Meg",
        f"R_D3 {sp(net_mcu_vcc)} 0 1Meg",  f"R_D4 {sp(net_sns_inp)} 0 1Meg",
        f"R_D5 {sp(net_sns_inn)} 0 1Meg",  f"R_D6 {sp(net_mcu_sda)} 0 1Meg",
        f"R_D7 {sp(net_sns_sda)} 0 1Meg",

        # --- Module 1: Power ---
        f"V_USB {sp(net_usb_vbus)} 0 9V", 
        f"X_U3 {sp(net_usb_vbus)} 0 {sp(net_ldo_out)} LDO_7805", 
        ".subckt LDO_7805 IN GND OUT",
        "B_REG OUT GND V=V(IN)>6.7 ? 5 : 0",
        "C_O OUT GND 100n",
        ".ends",

        # --- Module 2: Sensing ---
        f"R_SHUNT {sp(net_sns_inp)} {sp(net_sns_inn)} 0.008",
        f"R_LOAD {sp(net_sns_inn)} 0 4.5", # Approx. 2A load

        # --- Module 3: I2C ---
        # Force pull-up resistor connection at the MCU side
        f"R_PULL_SDA {sp(net_mcu_vcc)} {sp(net_mcu_sda)} 10k", 
        
        # Force pull-down control at the Sensor side
        f"V_I2C_CTL mcu_drive 0 PULSE(0 5 10m 100n 100n 5m 10m)",
        f"S_SDA {sp(net_sns_sda)} 0 mcu_drive 0 I2C_MOSFET",
        ".model I2C_MOSFET SW(Ron=10 Roff=10Meg Vt=2.5)",

        # --- Measurement Instructions ---
        f".meas TRAN v_usb_in AVG V({sp(net_usb_vbus)}) FROM 10m TO 20m",
        f".meas TRAN v_ldo_out AVG V({sp(net_ldo_out)}) FROM 10m TO 20m",
        f".meas TRAN v_cc_stable AVG V({sp(net_mcu_vcc)}) FROM 10m TO 20m",
        
        f".meas TRAN v_shunt_drop AVG V({sp(net_sns_inp)},{sp(net_sns_inn)}) FROM 10m TO 20m",
        
        f".meas TRAN i2c_mcu_high MAX V({sp(net_mcu_sda)}) FROM 2m TO 8m",
        f".meas TRAN i2c_sns_high MAX V({sp(net_sns_sda)}) FROM 2m TO 8m",
        f".meas TRAN i2c_mcu_low MIN V({sp(net_mcu_sda)}) FROM 12m TO 18m",
        ".end"
    ]
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
        
        report = ["="*65, " STRICT DIAGNOSTIC TOPOLOGY AUDIT ", "="*65]
        report.append(f"{'Audit Node':<30} | {'Value':<12} | {'Status'}")
        report.append("-" * 65)
        
        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results[k]
            is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
            if is_ok: pass_count += 1
            
            # Explicitly flag broken links if 0V or negligible drift is detected
            status_text = "PASS" if is_ok else "FAIL (BROKEN LINK)"
            val_str = f"{val:>8.3g} {spec['unit']}" if val is not None else "0.0 V"
            report.append(f"{spec['name']:<30} | {val_str:<12} | {status_text}")
            
        report.append("-" * 65)
        report.append(f"TOTAL STRICT PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        print("\n".join(report))
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write("\n".join(report))
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": 
    run_simulation()