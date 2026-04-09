import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE = os.path.join(BASE_DIR, "ppmux_full_scope.net")
LOG_FILE = os.path.join(BASE_DIR, "ppmux_full_scope.log")
REPORT_FILE = os.path.join(BASE_DIR, "ppmux_comprehensive_report.txt")

TEST_CRITERIA = {
    # --- Phase 1: Initial Battery Power (0-10ms) ---
    "v_bat_init":    {"name": "01_Init_Bat_Output",   "min": 3.4, "max": 3.8, "unit": "V"},
    
    # --- Phase 2: USB Plug-in Transient (~10ms) ---
    "v_plug_dip":    {"name": "02_Plug_In_Dip",      "min": 3.0, "max": 5.5, "unit": "V"},
    
    # --- Phase 3: USB Steady State (15-25ms) ---
    "v_usb_stable":  {"name": "05_USB_Stable_V",      "min": 4.4, "max": 5.1, "unit": "V"},
    "v_gs_mos_off":  {"name": "06_MOS_OFF_Vgs",       "min": 0.5, "max": 5.5, "unit": "V"}, 
    
    # --- Phase 4: USB Unplug Transient (~30ms) ---
    "v_unplug_dip":  {"name": "09_Unplug_Dip",        "min": 2.7, "max": 4.5, "unit": "V"},
    
    # --- Phase 5: Return to Battery Steady State (40-50ms) ---
    "v_bat_final":   {"name": "11_Final_Bat_Output",  "min": 3.4, "max": 3.8, "unit": "V"},
    "v_gs_mos_on":   {"name": "12_MOS_ON_Vgs",        "min": -5.0, "max": -2.5, "unit": "V"}
}

def build_dynamic_netlist():
    """Extracts topology from JSON; missing connections result in floating nodes."""
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"Missing {JSON_FILE}")

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Extract net mapping dictionary
    pins = {}
    for net in data.get("Power Path Multiplexer (PPMUX)", []):
        for conn in net["Connections"]:
            pins[f"{conn['ComponentID']}:{conn['PinName']}"] = net["net_id"]

    # 2. Map specific component pins to Net IDs
    # If missing in JSON, assign a random string with 'FLOAT' to ensure it remains open.
    n_usb = pins.get("USB:A9", "NC_FLOAT_USB")
    n_bat = pins.get("TP4057ST26P:3", "NC_FLOAT_BAT")
    n_gnd = pins.get("USB:A12", "NC_FLOAT_GND")
    
    # Set MOS Drain as the system output for load and measurement
    n_out = pins.get("IRLM:2", "NC_FLOAT_OUT") 

    # Core component pin mapping
    d_a = pins.get("SS34LH:1", "NC_D_A")  # Diode Anode
    d_k = pins.get("SS34LH:2", "NC_D_K")  # Diode Cathode
    m_g = pins.get("IRLM:1", "NC_M_G")    # MOS Gate
    m_d = pins.get("IRLM:2", "NC_M_D")    # MOS Drain
    m_s = pins.get("IRLM:3", "NC_M_S")    # MOS Source

    # Force identified Ground net to SPICE node '0'
    def n(name): return "0" if name == n_gnd else name

    # 3. Construct Netlist (Strict topology without idealized assumptions)
    netlist = [
        "* Comprehensive PPMUX STRICT Validation Netlist",
        ".model D_SCHOTTKY D(Is=1e-5 Rs=0.05 N=1.1)",
        ".model P_MOS VDMOS(pchan Vto=-1.2 Rs=0.05 Kp=2.0)",
        ".tran 0 50m 0 5u", 
        
        # --- Power Sources & Load ---
        f"V_BAT {n(n_bat)} 0 3.7",
        f"V_USB {n(n_usb)} 0 PULSE(0 5 10m 50u 50u 20m 50m)",
        f"R_LOAD {n(n_out)} 0 100",
        f"C_OUT {n(n_out)} 0 10u",
        
        # --- Core Topology ---
        f"D9 {n(d_a)} {n(d_k)} D_SCHOTTKY",
        f"M1 {n(m_d)} {n(m_g)} {n(m_s)} {n(m_s)} P_MOS",
        
        # --- Measurement Instructions ---
        f".meas TRAN v_bat_init AVG V({n(n_out)}) FROM 2m TO 8m",
        f".meas TRAN v_plug_dip MIN V({n(n_out)}) FROM 9m TO 13m",
        f".meas TRAN i_usb_surge MIN I(V_USB) FROM 9.5m TO 11m",
        f".meas TRAN t_switch_on WHEN V({n(n_out)})=4.3 RISE=1", 
        
        f".meas TRAN v_usb_stable AVG V({n(n_out)}) FROM 18m TO 25m",
        f".meas TRAN v_gs_mos_off AVG (V({n(m_g)})-V({n(m_s)})) FROM 18m TO 25m",
        f".meas TRAN i_leak_bat AVG I(V_BAT) FROM 18m TO 25m",
        f".meas TRAN p_loss_d9 AVG (V({n(d_a)})-V({n(d_k)}))*I(D9) FROM 18m TO 25m",
        
        f".meas TRAN v_unplug_dip MIN V({n(n_out)}) FROM 29m TO 35m",
        f".meas TRAN t_recovery WHEN V({n(n_out)})=3.5 FALL=1",
        
        f".meas TRAN v_bat_final AVG V({n(n_out)}) FROM 42m TO 48m",
        f".meas TRAN v_gs_mos_on AVG (V({n(m_g)})-V({n(m_s)})) FROM 42m TO 48m",
        ".end"
    ]
    
    final_netlist = "\n".join(netlist)
    print("\n--- Dynamically Generated SPICE Netlist Preview ---")
    print(final_netlist)
    print("--------------------------------------------------\n")
    
    return final_netlist

def run_simulation():
    try:
        content = build_dynamic_netlist()
    except Exception as e:
        print(f"Netlist generation failed: {e}")
        return

    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(">>> Performing multi-timepoint full scan validation...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): 
        print("Error: Failed to generate LTspice Log file.")
        return
        
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_raw = f.read()

    report = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append("="*95)
    report.append(f" PPMUX Module Comprehensive Simulation Report | Generated at: {timestamp}")
    report.append("="*95)
    report.append(f"{'Metric Code':<18} | {'Test Item Name':<22} | {'Measured Value':<15} | {'Criteria':<15} | {'Status'}")
    report.append("-" * 95)

    pass_count = 0
    for key, spec in TEST_CRITERIA.items():
        match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log_raw, re.I)
        val = float(match.group(1)) if match else None
        
        if val is not None:
            is_ok = spec["min"] <= val <= spec["max"]
            status = "✅ PASS" if is_ok else "❌ FAIL"
            if is_ok: pass_count += 1
            val_str = f"{val:>11.4f} {spec['unit']}"
        else:
            status = "⚠️ MISSING"
            val_str = "N/A"
        
        range_str = f"{spec['min']}~{spec['max']}"
        report.append(f"{key:<18} | {spec['name']:<22} | {val_str:<15} | {range_str:<15} | {status}")

    pass_rate = (pass_count / len(TEST_CRITERIA)) * 100
    report.append("-" * 95)
    report.append(f"Summary: Total {len(TEST_CRITERIA)} checkpoints | Passed {pass_count} | Failed {len(TEST_CRITERIA)-pass_count}")
    report.append(f"📊 Module Pass Rate: {pass_rate:.2f}%")
    report.append("="*95)

    output = "\n".join(report)
    print(output)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"\n>>> Detailed report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    run_simulation()