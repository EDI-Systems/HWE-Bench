import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_power.json")
CIR_FILE  = os.path.join(BASE_DIR, "power_strict_diagnostic.net")
LOG_FILE  = os.path.join(BASE_DIR, "power_strict_diagnostic.log")
REPORT_FILE = os.path.join(BASE_DIR, "power_strict_report.txt")

# --- 2. Full-flow Power Audit Metrics ---
TEST_CRITERIA = {
    "v_usb_link":  {"name": "[1] Charger_Receiving_5V_USB", "min": 4.90, "max": 5.10, "unit": "V"},
    "v_ldo_vin":   {"name": "[2] LDO_VIN_Connected",        "min": 3.00, "max": 5.10, "unit": "V"},
    "v_mcu_vdd":   {"name": "[3] MCU_Receiving_3.3V_LDO",   "min": 3.20, "max": 3.40, "unit": "V"},
    "v_chrg_low":  {"name": "[4] MCU_Detects_Charging_LOW", "min": 0.00, "max": 0.50, "unit": "V"},
    "v_chrg_high": {"name": "[5] MCU_Detects_Full_HIGH",    "min": 3.10, "max": 3.40, "unit": "V"}
}

def parse_module_topology(json_path, module_name, component_id):
    if not os.path.exists(json_path):
        print(f"  [Fatal Error] JSON file not found!: {json_path}")
        return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        try: data = json.load(f)
        except Exception as e: return {}
        
    module_nets = data.get(module_name, [])
    target_nets = {}
    for net in module_nets:
        for conn in net.get("Connections", []):
            if conn.get("ComponentID") == component_id:
                target_nets[conn.get("PinName")] = net.get("net_id", "")
    return target_nets

def build_netlist():
    print("="*65)
    print("Checking Power Management module JSON topology...")
    # Strictly search only within the Power Management module
    nets_usb  = parse_module_topology(JSON_FILE, "Power Management & Battery Charging", "USB")
    nets_chrg = parse_module_topology(JSON_FILE, "Power Management & Battery Charging", "MCP73831T")
    nets_ldo  = parse_module_topology(JSON_FILE, "Power Management & Battery Charging", "ME6209")
    nets_mcu  = parse_module_topology(JSON_FILE, "Power Management & Battery Charging", "ATtiny")

    def get_net(nets_dict, pin_name, comp_name):
        if not nets_dict or pin_name not in nets_dict:
            print(f"  [Warning] {comp_name} missing pin '{pin_name}', forcing generation of floating open-circuit node!")
            return f"NC_{uuid.uuid4().hex[:5]}"
        return nets_dict[pin_name]

    # Extract key energy and signal nodes
    net_usb_vbus  = get_net(nets_usb,  "VBUS", "USB")
    net_chrg_vcc  = get_net(nets_chrg, "VCC",  "MCP73831T")
    net_chrg_bat  = get_net(nets_chrg, "BAT",  "MCP73831T")
    net_chrg_stat = get_net(nets_chrg, "CHRG", "MCP73831T")
    
    net_ldo_vin   = get_net(nets_ldo,  "VIN",  "ME6209")
    net_ldo_vout  = get_net(nets_ldo,  "VOUT", "ME6209")
    
    net_mcu_vdd   = get_net(nets_mcu,  "VDD",  "ATtiny")
    net_mcu_pa6   = get_net(nets_mcu,  "PA6",  "ATtiny")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* Power Management Strict Diagnostic Audit",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 20m 0",
        
        # High-impedance resistors to prevent isolated node errors
        f"R_D1 {sp(net_usb_vbus)} 0 1G",  f"R_D2 {sp(net_chrg_vcc)} 0 1G",
        f"R_D3 {sp(net_chrg_bat)} 0 1G",  f"R_D4 {sp(net_chrg_stat)} 0 1G",
        f"R_D5 {sp(net_ldo_vin)} 0 1G",   f"R_D6 {sp(net_ldo_vout)} 0 1G",
        f"R_D7 {sp(net_mcu_vdd)} 0 1G",   f"R_D8 {sp(net_mcu_pa6)} 0 1G",

        # --- 1. USB Power Injection ---
        f"V_USB {sp(net_usb_vbus)} 0 5V",
        f".meas TRAN v_usb_link AVG V({sp(net_chrg_vcc)}) FROM 10m TO 20m",

        # --- 2. Simulate Real Li-ion Battery Charging Curve (3.8V to 4.2V) ---
        f"V_BAT_SIM {sp(net_chrg_bat)} 0 PWL(0 3.8 10m 4.2 20m 4.2)",
        
        # --- 3. Charging Indicator Logic (MCP73831 Model) ---
        # Logic: When VCC is 5V and Battery Voltage < 4.15V, it's in charging state (ctrl=1)
        f"B_CHRG_LOGIC ctrl 0 V=V({sp(net_chrg_vcc)})>4.5 & V({sp(net_chrg_bat)})<4.15 ? 1 : 0",
        # During charging, the internal open-drain switch pulls the CHRG pin low to GND
        f"S_STAT {sp(net_chrg_stat)} 0 ctrl 0 SW_MOD",
        ".model SW_MOD SW(Ron=1 Roff=1G Vt=0.5)",

        # --- 4. LDO Voltage Regulator Model (ME6209) ---
        # Measure if the LDO successfully connects to power (VIN) in the JSON
        f".meas TRAN v_ldo_vin AVG V({sp(net_ldo_vin)}) FROM 10m TO 20m",
        # Logic: If VIN > 3.4V, output 3.3V; otherwise, output VIN
        f"B_LDO {sp(net_ldo_vout)} 0 V=V({sp(net_ldo_vin)})>3.4 ? 3.3 : V({sp(net_ldo_vin)})",
        f".meas TRAN v_mcu_vdd AVG V({sp(net_mcu_vdd)}) FROM 10m TO 20m",

        # --- 5. MCU Pull-up Resistor and Pin State Monitoring ---
        # Internal GPIO pull-up resistor of the ATtiny (approx. 30k)
        f"R_PU_PA6 {sp(net_mcu_vdd)} {sp(net_mcu_pa6)} 30k",
        
        # 0-10ms (Battery < 4.15V) Charging: CHRG should be 0V
        f".meas TRAN v_chrg_low MIN V({sp(net_mcu_pa6)}) FROM 2m TO 8m",
        # 10-20ms (Battery reaches 4.2V) Full: CHRG should be pulled back to 3.3V by MCU
        f".meas TRAN v_chrg_high MAX V({sp(net_mcu_pa6)}) FROM 15m TO 20m",
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
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)? )", log, re.I)
            if m: results[k] = float(m.group(1))
        
        report = ["="*65, " POWER MANAGEMENT FULL-FLOW DIAGNOSTIC AUDIT ", "="*65]
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
        report.append(f"TOTAL DIAGNOSTIC PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
        print("\n".join(report))
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write("\n".join(report))
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()