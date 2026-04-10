import os
import subprocess
import re
import json
import uuid

LTSPICE_EXE = "D:/app/LTspice/LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct","dynamic_protect.json")

CIR_FILE  = os.path.join(BASE_DIR, "lipo_protect_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "lipo_protect_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "lipo_protect_audit_report.txt")

# Added multiple deep detection points to cover OD/OC logic levels and various operating conditions
TEST_CRITERIA = {
    "i_charging":     {"name": "TP4056_Charge_Current",   "min": 0.90, "max": 1.10, "unit": "A"},
    "v_bat_charge":   {"name": "Battery_Voltage_Charging","min": 2.90, "max": 3.10, "unit": "V"},
    "v_od_normal":    {"name": "DW01A_OD_Pin_Normal",     "min": 4.50, "max": 5.50, "unit": "V"},
    "v_oc_normal":    {"name": "DW01A_OC_Pin_Normal",     "min": 4.50, "max": 5.50, "unit": "V"},
    "v_out_normal":   {"name": "System_Output_Normal",    "min": 2.90, "max": 3.10, "unit": "V"},
    "v_out_cutoff":   {"name": "System_Output_Cutoff",    "min": -0.10, "max": 0.10, "unit": "V"}
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
    nets_tp = parse_dut_topology(JSON_FILE, "LiPo Charging and Protection", "TP4056")
    nets_dw = parse_dut_topology(JSON_FILE, "LiPo Charging and Protection", "DW01A")
    nets_fs = parse_dut_topology(JSON_FILE, "LiPo Charging and Protection", "FS8205")

    # Dynamically allocate pin nets; isolate as a floating net if no match is found
    dut_tp_vcc = nets_tp.get("VCC", f"NC_TPV_{uuid.uuid4().hex[:4]}")
    dut_tp_bat = nets_tp.get("BAT", f"NC_TPB_{uuid.uuid4().hex[:4]}")
    dut_tp_gnd = nets_tp.get("GND", f"NC_TPG_{uuid.uuid4().hex[:4]}")

    dut_dw_vcc = nets_dw.get("VCC", f"NC_DWV_{uuid.uuid4().hex[:4]}")
    dut_dw_gnd = nets_dw.get("GND", f"NC_DWG_{uuid.uuid4().hex[:4]}")
    dut_dw_od  = nets_dw.get("OD",  f"NC_DWD_{uuid.uuid4().hex[:4]}")
    dut_dw_oc  = nets_dw.get("OC",  f"NC_DWC_{uuid.uuid4().hex[:4]}")
    dut_dw_cs  = nets_dw.get("CS",  f"NC_DWS_{uuid.uuid4().hex[:4]}")

    dut_fs_d1  = nets_fs.get("D1",  f"NC_FS1_{uuid.uuid4().hex[:4]}")
    dut_fs_d2  = nets_fs.get("D2",  f"NC_FS2_{uuid.uuid4().hex[:4]}")
    dut_fs_g1  = nets_fs.get("G1",  f"NC_FSG1_{uuid.uuid4().hex[:4]}")
    dut_fs_g2  = nets_fs.get("G2",  f"NC_FSG2_{uuid.uuid4().hex[:4]}")

    def sp(n): return "0" if n in ["net_out_minus", "0"] else n

    netlist = [
        "* Multi-Point LiPo Protection Audit (Strictly Hardened)",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 10u 6m 0 uic",
        
        "* ==========================================",
        "* TESTBENCH: Fixed Physical Testbed Nets",
        "* ==========================================",
        "* 0-2ms: 5V Charging; 2-6ms: 0V Power-off",
        "V_VIN net_vin 0 PWL(0 5 2m 5 2.01m 0 6m 0)",
        
        "* 0-4ms: Normal Voltage 3.0V; 4-6ms: Drop to Over-discharge threshold 2.0V",
        "V_BATT net_b_plus net_b_minus PWL(0 3.0 4m 3.0 4.01m 2.0 6m 2.0)",
        
        "R_LOAD net_b_plus 0 100",
        
        "* Ultimate Defense: Prevent Singular Matrix collapse",
        "R_DUM1 net_vin 0 1G",
        "R_DUM2 net_b_plus 0 1G",
        "R_DUM3 net_b_minus 0 1G",
        "R_DUM4 net_od 0 1G",
        "R_DUM5 net_oc 0 1G",
        
        "* ==========================================",
        "* DUT: JSON Dynamic Topology Mapping",
        "* ==========================================",
        f"X_TP4056 {sp(dut_tp_vcc)} {sp(dut_tp_bat)} {sp(dut_tp_gnd)} TP4056_MACRO",
        ".subckt TP4056_MACRO VCC BAT GND",
        "B_CHG VCC BAT I=if(V(VCC)>4.5 & V(BAT)<4.2, 1.0, 0)",
        ".ends",

        f"X_DW01A {sp(dut_dw_od)} {sp(dut_dw_cs)} {sp(dut_dw_oc)} {sp(dut_dw_vcc)} {sp(dut_dw_gnd)} DW01A_MACRO",
        ".subckt DW01A_MACRO OD CS OC VCC GND",
        "B_OD OD GND V=if(V(VCC,GND)<2.4, 0, 5)",
        "B_OC OC GND V=if(V(VCC,GND)>4.3, 0, 5)",
        "R_D1 OD GND 1Meg",
        "R_D2 OC GND 1Meg",
        "R_D3 CS GND 1Meg",
        ".ends",

        f"X_FS8205 {sp(dut_fs_d1)} {sp(dut_fs_d2)} {sp(dut_fs_g1)} {sp(dut_fs_g2)} {sp(dut_dw_gnd)} FS8205_MACRO",
        ".subckt FS8205_MACRO D1 D2 G1 G2 VSS",
        "B_GATE gate_int 0 V=if(V(G1,VSS)>2 & V(G2,VSS)>2, 5, 0)",
        "S_M1 D1 D2 gate_int 0 SW_NMOS",
        ".model SW_NMOS SW(Ron=0.04 Roff=1G Vt=2.5)",
        "C_DUM gate_int 0 1p",
        ".ends",
        
        "* ==========================================",
        "* Multi-node Array Measurement (Full Monitoring)",
        "* ==========================================",
        "* Phase 1 (1-1.9ms): USB Charging Mode",
        ".meas TRAN i_charging AVG -I(V_VIN) FROM 1m TO 1.9m",
        ".meas TRAN v_bat_charge AVG V(net_b_plus) FROM 1m TO 1.9m",
        
        "* Phase 2 (3-3.9ms): Normal Battery Discharge Mode",
        ".meas TRAN v_od_normal AVG V(net_od) FROM 3m TO 3.9m",
        ".meas TRAN v_oc_normal AVG V(net_oc) FROM 3m TO 3.9m",
        ".meas TRAN v_out_normal AVG V(net_b_plus) FROM 3m TO 3.9m",
        
        "* Phase 3 (5-5.9ms): Battery Over-discharge Cutoff Mode",
        ".meas TRAN v_od_cutoff AVG V(net_od) FROM 5m TO 5.9m",
        ".meas TRAN v_out_cutoff AVG V(net_b_plus) FROM 5m TO 5.9m",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    # Force removal of ghost logs
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
        
        if not os.path.exists(LOG_FILE):
            print("FATAL ERROR: Simulation engine aborted; log file not generated. Check JSON topology nets.")
            return

        with open(LOG_FILE, 'r', errors='ignore') as f: 
            log = f.read()

        results = {}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
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