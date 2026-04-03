import os
import subprocess
import re
import json
import uuid

LTSPICE_EXE = "D:/app/LTspice/LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
CIR_FILE = os.path.join(BASE_DIR, "eval_battery_prot.net")
LOG_FILE = os.path.join(BASE_DIR, "eval_battery_prot.log")

TEST_POINTS = [
    {"id": "V_OD_HIGH",   "unit": "V", "min": 4.0,  "max": 5.5,  "name": "Discharge_ON", "desc": "OD output when battery normal"},
    {"id": "V_OD_LOW",    "unit": "V", "min": -0.1, "max": 0.5,  "name": "UV_Shutdown", "desc": "OD command when battery < 2.4V"},
    {"id": "V_OC_NORMAL", "unit": "V", "min": 4.0,  "max": 5.5,  "name": "Charge_Permit", "desc": "OC output when battery normal"},
    {"id": "V_OC_PROT",   "unit": "V", "min": -0.1, "max": 0.5,  "name": "OVP_Command", "desc": "OC command when battery > 4.25V"},
    {"id": "V_BAT_SENSE", "unit": "V", "min": 2.2,  "max": 4.5,  "name": "Chip_Sense_In", "desc": "Verify DW01A:VCC connectivity"},
    {"id": "V_G1_LINK",   "unit": "V", "min": 4.0,  "max": 5.5,  "name": "Ctrl_Link_1", "desc": "Verify OD to M1:G connectivity"},
    {"id": "V_G2_LINK",   "unit": "V", "min": 4.0,  "max": 5.5,  "name": "Ctrl_Link_2", "desc": "Verify OC to M2:G connectivity"},
    {"id": "V_S1_GND",    "unit": "V", "min": -0.01,"max": 0.01, "name": "Power_GND", "desc": "Verify M1:S physical grounding"},
    {"id": "V_CS_LINK",   "unit": "V", "min": -0.1, "max": 0.5,  "name": "CS_Link", "desc": "Verify DW01A:CS connectivity"},
    {"id": "V_D_COMMON",  "unit": "V", "min": -0.5, "max": 4.5,  "name": "Intermediate_V", "desc": "Verify dual MOS drain connection"},
    {"id": "V_MCU_GND",   "unit": "V", "min": -0.01,"max": 0.01, "name": "MCU_GND_Quality", "desc": "Verify MCU ground connectivity"},
    {"id": "V_TP_BAT",    "unit": "V", "min": 2.2,  "max": 4.5,  "name": "Charge_Output", "desc": "Verify TP4056 to battery connection"}
]

def build_strict_netlist():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f).get("Power Management & Battery Safety", [])
    
    pins = {}
    for net in data:
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            if key in pins:
                if isinstance(pins[key], list): pins[key].append(net["net_id"])
                else: pins[key] = [pins[key], net["net_id"]]
            else: pins[key] = net["net_id"]

    def get_net(cp, idx=0):
        if cp in pins:
            val = pins[cp]
            return val[idx] if isinstance(val, list) else val
        return f"OPEN_{uuid.uuid4().hex[:6]}"

    n_vcc = get_net("DW01A:VCC")
    n_gnd = get_net("DW01A:GND")
    n_od  = get_net("DW01A:OD")
    n_oc  = get_net("DW01A:OC")
    n_cs  = get_net("DW01A:CS")
    n_mcu_v = get_net("ATtiny85-20SU:VCC")
    n_mcu_g = get_net("ATtiny85-20SU:GND")

    netlist = [
        "* PCB-Bench: STRICT BEHAVIORAL TOPOLOGY TEST",
        ".tran 0.6", ".options plotwinsize=0 numdgt=7",
        f"V_BAT {n_vcc} 0 PWL(0 4.2 0.1 4.3 0.2 3.0 0.3 2.3 0.4 2.3 0.5 3.5 0.6 3.7)",
        f"V_GND {n_gnd} 0 0",
        f"R_GND_CHECK {n_mcu_g} 0 1Meg", 
        f"B_OD {n_od} 0 V=IF(V({n_vcc}) > 2.4, 5, 0)",
        f"B_OC {n_oc} 0 V=IF(V({n_vcc}) < 4.25, 5, 0)",
        f"R_LOAD {n_vcc} {n_mcu_v} 1k",
        f"M1 {get_net('FS8205A:D',0)} {get_net('FS8205A:G',0)} {get_net('FS8205A:S',0)} {get_net('FS8205A:S',0)} MyMOS",
        f"M2 {get_net('FS8205A:D',1)} {get_net('FS8205A:G',1)} {get_net('FS8205A:S',1)} {get_net('FS8205A:S',1)} MyMOS",
        ".model MyMOS NMOS(Vto=1.5 Kp=20)",
        f".meas TRAN V_OD_HIGH FIND V({n_od}) AT 0.2",
        f".meas TRAN V_OD_LOW  FIND V({n_od}) AT 0.35",
        f".meas TRAN I_LOAD_NORM AVG I(V_BAT) FROM 0.15 TO 0.25",
        f".meas TRAN I_LOAD_PROT AVG I(V_BAT) FROM 0.35 TO 0.45",
        f".meas TRAN V_OC_NORMAL FIND V({n_oc}) AT 0.2",
        f".meas TRAN V_OC_PROT   FIND V({n_oc}) AT 0.1",
        f".meas TRAN V_MCU_VCC  FIND V({n_mcu_v}) AT 0.2",
        f".meas TRAN V_BAT_SENSE FIND V({n_vcc}) AT 0.2",
        f".meas TRAN V_G1_LINK  FIND V({get_net('FS8205A:G',0)}) AT 0.2",
        f".meas TRAN V_G2_LINK  FIND V({get_net('FS8205A:G',1)}) AT 0.2",
        f".meas TRAN V_S1_GND   FIND V({get_net('FS8205A:S',0)}) AT 0.2",
        f".meas TRAN V_CS_LINK  FIND V({n_cs}) AT 0.2",
        f".meas TRAN V_D_COMMON FIND V({get_net('FS8205A:D',0)}) AT 0.2",
        f".meas TRAN V_MCU_GND  FIND V({n_mcu_g}) AT 0.2",
        f".meas TRAN V_TP_BAT   FIND V({get_net('TP4056:BAT')}) AT 0.2",
        f".meas TRAN T_RESP_OK  TRIG V({n_vcc})=2.4 TARG V({get_net('FS8205A:G',0)})=0.5 FALL=1",
        ".end"
    ]
    return "\n".join(netlist)

def run_eval():
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f:
            f.write(build_strict_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], timeout=20, check=True)
    except Exception:
        return

    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log = f.read()

    pass_cnt = 0
    for tp in TEST_POINTS:
        match = re.search(rf"{tp['id']}[^=]*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
        val = float(match.group(1)) if match else -99.0
        status = "PASS" if tp['min'] <= val <= tp['max'] else "FAIL"
        if status == "PASS": pass_cnt += 1

if __name__ == "__main__":
    run_eval()