import os
import subprocess
import re
import json

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE = os.path.join(BASE_DIR, "heater_switch_strict.net")
LOG_FILE = os.path.join(BASE_DIR, "heater_switch_strict.log")

TEST_POINTS_CONFIG = [
    {"id": "V_P_ON",      "unit": "V", "min": 23.0, "max": 25.0, "name": "Output Turn-on Voltage", "desc": "Verify if power path is established"},
    {"id": "VGS_BOOT",    "unit": "V", "min": 5.0,  "max": 18.0, "name": "Bootstrap VGS",          "desc": "Verify if bootstrap circuit is effective"},
    {"id": "I_LOAD",      "unit": "A", "min": 2.8,  "max": 3.2,  "name": "Load Output Current",    "desc": "Verify loop integrity"},
    {"id": "V_BOOT_HI",   "unit": "V", "min": 40.0, "max": 48.0, "name": "Bootstrap Potential",    "desc": "Verify potential pump superposition"},
    {"id": "V_GATE_LO",   "unit": "V", "min": -0.1, "max": 0.5,  "name": "Turn-off Gate Potential", "desc": "Verify low-level turn-off capability"},
    {"id": "V_PWM_IN",    "unit": "V", "min": 3.0,  "max": 3.6,  "name": "Input Signal Level",     "desc": "Verify MCU output level"},
    {"id": "I_V1_AVG",    "unit": "A", "min": 1.4,  "max": 1.6,  "name": "Bus Average Current",    "desc": "Verify power consumption at 50% duty cycle"},
    {"id": "V_DS_ON",     "unit": "V", "min": -0.1, "max": 1.0,  "name": "MOSFET On-state Drop",   "desc": "Verify operation in switching region"},
    {"id": "V_P_OFF",     "unit": "V", "min": -0.1, "max": 0.5,  "name": "Output Turn-off Voltage", "desc": "Verify complete shutdown"}
]

def build_netlist():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"FileNotFound: {JSON_FILE}")

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    module_data = data.get("High-Side PWM Gate Driver with Active Clamp", [])
    
    pins = {}
    comps = set()
    for net in module_data:
        net_id = net["net_id"]
        for conn in net["Connections"]:
            comp_id = conn["ComponentID"]
            pin_name = conn["PinName"]
            pins[f"{comp_id}:{pin_name}"] = net_id
            comps.add(comp_id)

    netlist_lines = [
        "* Heater Switch Strict Evaluation Netlist",
        ".tran 0 1.2m 0 100n",
        ".options plotwinsize=0 numdgt=7",
        "V_STIM_PWR net_24v_raw 0 24",
        "V_STIM_PWM net_mcu_raw 0 PULSE(3.3 0 0.1m 10n 10n 0.5m 1m)"
    ]

    # Stimuli Mapping
    if "V1:P" in pins: netlist_lines.append(f"V_B1 {pins['V1:P']} net_24v_raw 0")
    if "ATmega328P:PD3" in pins: netlist_lines.append(f"V_B2 {pins['ATmega328P:PD3']} net_mcu_raw 0")
    if "V1:N" in pins: netlist_lines.append(f"V_B3 {pins['V1:N']} 0 0")

    # Component Mapping
    if "IRLR" in comps:
        d, g, s = pins.get("IRLR:D", "NC_D"), pins.get("IRLR:G", "NC_G"), pins.get("IRLR:S", "P_OUT")
        netlist_lines.append(f"M_Q2 {d} {g} {s} {s} MyMOS")

    if "Q1" in comps:
        c, b, e = pins.get("Q1:C", "NC_C"), pins.get("Q1:B", "NC_B"), pins.get("Q1:E", "0")
        netlist_lines.append(f"Q_Q1 {c} {b} {e} MyNPN")

    if "D1" in comps:
        netlist_lines.append(f"D_D1 {pins.get('D1:A','NC_A')} {pins.get('D1:K','NC_K')} MyDiode")

    if "C7" in comps:
        netlist_lines.append(f"C_C7 {pins.get('C7:P','NC_P')} {pins.get('C7:N','NC_N')} 10u")

    if "D4" in comps:
        netlist_lines.append(f"D_D4 {pins.get('D4:A','NC_ZA')} {pins.get('D4:K','NC_ZK')} MyZener")

    if "R5" in comps: netlist_lines.append(f"R_R5 {pins.get('R5:1','NC_R51')} {pins.get('R5:2','NC_R52')} 1k")
    if "R6" in comps: netlist_lines.append(f"R_R6 {pins.get('R6:1','NC_R61')} {pins.get('R6:2','NC_R62')} 1k")

    if "HEATER" in comps:
        netlist_lines.append(f"R_LOAD {pins.get('HEATER:1','P_OUT')} {pins.get('HEATER:2','0')} 8")

    node_p_out = pins.get("IRLR:S", "P_OUT")
    node_gate = pins.get("IRLR:G", "NC_G")
    node_boot = pins.get("C7:P", "NC_P")
    node_mcu = pins.get("ATmega328P:PD3", "NC_PWM")

    netlist_lines.extend([
        ".model MyMOS NMOS(Vto=2.1 Kp=10)",
        ".model MyNPN NPN(Bf=200)",
        ".model MyDiode D(Vd=0.7)",
        ".model MyZener D(Vz=15 Bv=15 Ibv=1m)",
        f".meas TRAN V_P_ON MAX V({node_p_out}) FROM 0.2m TO 0.4m",
        f".meas TRAN VGS_BOOT MAX V({node_gate})-V({node_p_out}) FROM 0.2m TO 0.4m",
        f".meas TRAN I_LOAD MAX I(R_LOAD) FROM 0.2m TO 0.4m",
        f".meas TRAN V_BOOT_HI MAX V({node_boot}) FROM 0.2m TO 0.4m",
        f".meas TRAN V_GATE_LO FIND V({node_gate}) AT 0.8m",
        f".meas TRAN V_PWM_IN MAX V({node_mcu})",
        f".meas TRAN I_V1_AVG AVG ABS(I(V_STIM_PWR)) FROM 0.1m TO 1.1m",
        f".meas TRAN V_DS_ON FIND V(net_24v_raw)-V({node_p_out}) AT 0.3m",
        f".meas TRAN V_P_OFF FIND V({node_p_out}) AT 0.8m",
        f".meas TRAN T_RISE TRIG V({node_p_out})=2 TD=0.05m TARG V({node_p_out})=22 RISE=1",
        ".end"
    ])
    return "\n".join(netlist_lines)

def run_benchmark():
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f:
            f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], timeout=15, check=True)
    except Exception:
        return

    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()

    pass_cnt = 0
    for tp in TEST_POINTS_CONFIG:
        pattern = rf"{tp['id']}.*?(?:diff\s*[:=]|[:=])\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
        match = re.search(pattern, log_content, re.IGNORECASE)
        val = float(match.group(1)) if match else -0.001
        
        status = "PASS" if tp['min'] <= val <= tp['max'] else "FAIL"
        if status == "PASS": pass_cnt += 1

if __name__ == "__main__":
    run_benchmark()