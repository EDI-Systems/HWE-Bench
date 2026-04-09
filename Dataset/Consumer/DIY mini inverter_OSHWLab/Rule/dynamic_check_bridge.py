import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_bridge.json")

CIR_FILE  = os.path.join(BASE_DIR, "bridge_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "bridge_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "bridge_report.txt")

# 10 Core Audit Test Points (Covers 300V Modified Sine Wave physical specs)
TEST_CRITERIA = {
    "v_out_pos":    {"name": "01_Positive_Peak",      "min": 280.0, "max": 320.0, "unit": "V"},
    "v_out_rms":    {"name": "03_AC_Output_RMS",      "min": 200.0, "max": 240.0, "unit": "V"},
    "i_peak_load":  {"name": "04_Peak_Load_Current",  "min": 0.5,   "max": 5.0,   "unit": "A"},
    "v_gs_m1":      {"name": "05_M1_HighSide_Vgs",    "min": 8.0,   "max": 12.0,  "unit": "V"},
    "t_deadtime":   {"name": "06_Deadtime_Interval",  "min": 1e-3,  "max": 5e-3,  "unit": "s"},
    "i_shoot_thru": {"name": "07_Shoot_Thru_Check",   "min": -0.1,  "max": 0.1,   "unit": "A"}
}

def extract_topology_from_json():
    """Extract core component pin net mappings from JSON, ignoring resistors/capacitors"""
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Locate H-Bridge module
    hb_data = data.get("H-Bridge Inverter & Isolated Gate Drive", [])
    
    # Build mapping table: "ComponentID:PinName" -> "net_id"
    # Focus on MCU, Optocouplers (EL357N), MOSFETs (IRF840), HVDC, and 78L05
    pins = {}
    for net in hb_data:
        for conn in net["Connections"]:
            comp_id = conn['ComponentID']
            # Filter critical components
            if any(key in comp_id for key in ["ATmega", "EL357N", "IRF840", "HVDC", "78L05"]):
                pins[f"{comp_id}:{conn['PinName']}"] = net["net_id"]
    return pins

def build_netlist():
    """Dynamically generate SPICE netlist based on extracted pin topology"""
    p = extract_topology_from_json()

    # --- Extract critical topology path points ---
    # Control Side
    n_pd3 = p.get("ATmega328P-AU:PD3", "NC_PD3")
    n_pd5 = p.get("ATmega328P-AU:PD5", "NC_PD5")
    n_pd6 = p.get("ATmega328P-AU:PD6", "NC_PD6")
    n_pd7 = p.get("ATmega328P-AU:PD7", "NC_PD7")
    n_mcu_gnd = p.get("ATmega328P-AU:GND", "NC_MGND")

    # Power Side
    n_hvdc = p.get("IRF840_1:D", "NC_HVDC")
    n_pwr_gnd = p.get("IRF840_2:S", "NC_PGND")
    
    # Load connection points (Phase nodes)
    n_out_l = p.get("IRF840_1:S", "NC_OL")
    n_out_r = p.get("IRF840_3:S", "NC_OR")

    # Gate Drive Paths (Opto to MOS)
    n_g1 = p.get("IRF840_1:G", "NC_G1")
    n_g2 = p.get("IRF840_2:G", "NC_G2")
    n_g3 = p.get("IRF840_3:G", "NC_G3")
    n_g4 = p.get("IRF840_4:G", "NC_G4")

    # Normalize Ground levels
    def n(name): return "0" if name in [n_mcu_gnd, n_pwr_gnd, "GND", "net5", "net14"] else name

    netlist = [
        "* H-Bridge Strict Topology Audit Netlist",
        ".model N_MOS VDMOS(nchan Vto=3.5 Rs=0.85 Kp=4 Cgdmax=1.3n) ; IRF840 Approx",
        ".options abstol=1n reltol=0.01 vntol=1m plotwinsize=0",
        ".tran 0 40m 0 100u",
        
        # 310V HVDC Input Source
        f"V_HVDC {n(n_hvdc)} 0 310",
        
        # --- MCU Signal Sources (Inject based on JSON PD pin mappings) ---
        f"V_L_HI {n(n_pd3)} 0 PULSE(0 5 2m 1u 1u 6m 20m)",
        f"V_L_LO {n(n_pd5)} 0 PULSE(0 5 12m 1u 1u 6m 20m)",
        f"V_R_HI {n(n_pd6)} 0 PULSE(0 5 12m 1u 1u 6m 20m)",
        f"V_R_LO {n(n_pd7)} 0 PULSE(0 5 2m 1u 1u 6m 20m)",
        
        # --- Behavioral Isolation Drive Model (Active only if pins are connected correctly) ---
        # Simulate "Optocoupler + Isolated Power" using controlled voltage sources
        f"E_G1 {n(n_g1)} {n(n_out_l)} VALUE={{V({n(n_pd3)})*2}}",
        f"E_G2 {n(n_g2)} 0 VALUE={{V({n(n_pd5)})*2}}",
        f"E_G3 {n(n_g3)} {n(n_out_r)} VALUE={{V({n(n_pd6)})*2}}",
        f"E_G4 {n(n_g4)} 0 VALUE={{V({n(n_pd7)})*2}}",
        
        # --- H-Bridge Power Stage ---
        f"M1 {n(n_hvdc)} {n(n_g1)} {n(n_out_l)} {n(n_out_l)} N_MOS",
        f"M2 {n(n_out_l)} {n(n_g2)} 0 0 N_MOS",
        f"M3 {n(n_hvdc)} {n(n_g3)} {n(n_out_r)} {n(n_out_r)} N_MOS",
        f"M4 {n(n_out_r)} {n(n_g4)} 0 0 N_MOS",
        
        # Design load cross-connected between extracted phase nodes
        f"R_LOAD {n(n_out_l)} {n(n_out_r)} 150",
        
        # --- Measurement Instructions ---
        f".meas TRAN v_out_pos MAX V({n(n_out_l)},{n(n_out_r)}) FROM 2m TO 8m",
        f".meas TRAN v_out_rev MIN V({n(n_out_l)},{n(n_out_r)}) FROM 12m TO 18m",
        f".meas TRAN v_out_rms RMS V({n(n_out_l)},{n(n_out_r)}) FROM 0 TO 20m",
        f".meas TRAN i_peak_load MAX I(R_LOAD)",
        f".meas TRAN v_gs_m1 MAX V({n(n_g1)},{n(n_out_l)})",
        f".meas TRAN t_fall WHEN V({n(n_out_l)},{n(n_out_r)})=10 FALL=1",
        f".meas TRAN t_rise_neg WHEN V({n(n_out_l)},{n(n_out_r)})=-10 FALL=1",
        " .meas TRAN t_deadtime PARAM t_rise_neg-t_fall",
        f".meas TRAN i_shoot_thru MAX I(V_HVDC) FROM 8m TO 12m",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    # Generate netlist
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(build_netlist())
    
    print(f">>> Auditing H-Bridge module based on JSON topology...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_raw = f.read()

    # Generate Audit Report
    report = ["="*85, f" H-Bridge Topology Audit Report | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "="*85]
    report.append(f"{'Audit Item':<25} | {'Measured':<15} | {'Status'}")
    report.append("-" * 85)

    pass_count = 0
    for key, spec in TEST_CRITERIA.items():
        match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+?)?)", log_raw, re.I)
        val = float(match.group(1)) if match else None
        
        if val is not None:
            # Special handling for negative peak
            check_val = abs(val) if key == "v_out_rev" else val
            is_ok = spec["min"] <= val <= spec["max"] if key != "v_out_rev" else spec["min"] <= val <= spec["max"]
            status = "✅ PASS" if is_ok else "❌ FAIL"
            if is_ok: pass_count += 1
            val_str = f"{val:>11.4f} {spec['unit']}"
        else:
            status = "❌ FAIL (Open Circuit)"; val_str = "0.0000"

        report.append(f"{spec['name']:<25} | {val_str:<15} | {status}")

    report.append("-" * 85)
    report.append(f"📊 Topology Integrity Rate: {(pass_count/len(TEST_CRITERIA))*100:.2f}%")
    
    final_output = "\n".join(report)
    print(final_output)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_output)

if __name__ == "__main__":
    run_simulation()