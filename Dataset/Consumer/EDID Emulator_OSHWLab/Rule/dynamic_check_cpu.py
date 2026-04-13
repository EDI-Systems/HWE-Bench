import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_cpu.json")

CIR_FILE  = os.path.join(BASE_DIR, "cpu_strict_diagnostic.net")
LOG_FILE  = os.path.join(BASE_DIR, "cpu_strict_diagnostic.log")
REPORT_FILE = os.path.join(BASE_DIR, "cpu_strict_report.txt")

TARGET_MODULE = "Central Processing Unit (CPU) & System Controller"

# Audit Metrics: Logic level verification for the full 4-stage state machine process
TEST_CRITERIA = {
    "v_uart_rx":   {"name": "[1] UART_RX_Firmware_Sync",     "min": 3.00, "max": 3.50, "unit": "V"},
    "v_wp_unlock": {"name": "[2] EEPROM_WP_Unlock_Sequence", "min": -0.10, "max": 0.50, "unit": "V"},
    "v_i2c_data":  {"name": "[3] I2C_SCL_Burn_Activity",     "min": 1.40, "max": 1.90, "unit": "V"}, # 1.65V AVG
    "v_hpd_reset": {"name": "[4] HDMI_HPD_Reset_Pulse",      "min": -0.10, "max": 0.50, "unit": "V"} 
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
    print(f"Auditing Core Brain Control Domain: {TARGET_MODULE}")
    
    nets_mcu    = parse_module_topology(JSON_FILE, TARGET_MODULE, "CH32V003")
    nets_eeprom = parse_module_topology(JSON_FILE, TARGET_MODULE, "AT24C32")
    nets_uart   = parse_module_topology(JSON_FILE, TARGET_MODULE, "HT42B534-2")
    nets_hdmi   = parse_module_topology(JSON_FILE, TARGET_MODULE, "HDMI-01")

    def get_net(nets_dict, pin_aliases):
        for alias in pin_aliases:
            for key in nets_dict.keys():
                if alias in key: return nets_dict[key]
        return f"NC_{uuid.uuid4().hex[:5]}"

    # Extract net connections for MCU and peripherals (Fuzzy matching for naming variations)
    n_uart_tx   = get_net(nets_uart, ["TX"])
    n_mcu_rx    = get_net(nets_mcu, ["RX", "PD6"])
    
    n_eeprom_wp = get_net(nets_eeprom, ["WP", "7"])
    n_mcu_wp    = get_net(nets_mcu, ["PC3", "T1CH3"]) # Assigned based on general schematic
    
    n_eeprom_scl= get_net(nets_eeprom, ["SCL", "6"])
    n_mcu_scl   = get_net(nets_mcu, ["SCL", "PC2"])
    
    n_hdmi_hpd  = get_net(nets_hdmi, ["Hot_Plug_Detect", "19"])
    n_mcu_hpd   = get_net(nets_mcu, ["PC0", "PD0", "PA1"]) # Compatible with common GPIO assignments

    # Topology Anti-Cheat Verification
    is_missing = any("NC_" in net for net in [n_uart_tx, n_mcu_rx, n_eeprom_wp, n_mcu_wp, n_eeprom_scl, n_mcu_scl, n_hdmi_hpd, n_mcu_hpd])

    if is_missing:
        status_info = "CRITICAL FAIL: Topology Missing (MCU control pins not fully connected to peripherals)"
    else:
        status_info = "TOPOLOGY PASS: Control bus fully connected, preparing for state machine timing injection"

    print(f"  [JUDGMENT] {status_info}")
    print("="*65)

    def sp(n): return "0" if n in ["net_gnd", "0", "GND"] else n

    netlist = [
        "* CPU State Machine & Timing Audit - Physics Tuned",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10u 30m 0",
        
        "V_VDD net_vdd 0 3.3V",

        "* Physical Correction 1: Strong impedance pull-up/down networks at peripheral ends",
        "* (Anti-cheat: If MCU is disconnected, peripheral voltage is locked by these resistors, resulting in FAIL)",
        f"R_PU_WP  {sp(n_eeprom_wp)} net_vdd 10k",
        f"R_PU_SCL {sp(n_eeprom_scl)} net_vdd 4.7k",
        f"R_PU_HPD {sp(n_hdmi_hpd)} net_vdd 10k",
        f"R_PD_RX  {sp(n_mcu_rx)} 0 10k",

        "* --- Timing Phase 1: UART receiving external firmware config (Pulse trigger) ---",
        f"V_UART {sp(n_uart_tx)} 0 PWL(0 0V 2m 0V 2.1m 3.3V 4m 3.3V 4.1m 0V)",
        f".meas TRAN v_uart_rx MAX V({sp(n_mcu_rx)}) FROM 1m TO 5m",

        "* --- Timing Phase 2: MCU releases EEPROM write protection (Pull-low unlock) ---",
        f"V_MCU_WP {sp(n_mcu_wp)} 0 PWL(0 3.3V 4.9m 3.3V 5m 0V 20m 0V 20.1m 3.3V)",
        f".meas TRAN v_wp_unlock MIN V({sp(n_eeprom_wp)}) FROM 10m TO 15m",

        "* --- Timing Phase 3: MCU flashing data via I2C (10kHz simulated clock) ---",
        f"B_SCL {sp(n_mcu_scl)} 0 V=(time>10m & time<15m) ? 1.65*sin(2*pi*10k*time)+1.65 : 3.3",
        f".meas TRAN v_i2c_data AVG V({sp(n_eeprom_scl)}) FROM 10m TO 15m",

        "* --- Timing Phase 4: MCU pulling down HPD to force GPU handshake (Spoof pulse) ---",
        f"V_MCU_HPD {sp(n_mcu_hpd)} 0 PWL(0 3.3V 21.9m 3.3V 22m 0V 28m 0V 28.1m 3.3V)",
        f".meas TRAN v_hpd_reset MIN V({sp(n_hdmi_hpd)}) FROM 23m TO 27m",
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
        
        report = ["="*65, " CPU STATE MACHINE & TIMING AUDIT (100% STRICT) ", "="*65]
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
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_simulation()