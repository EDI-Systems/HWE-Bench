import os
import subprocess
import re
import json
import uuid
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_sensor.json")

CIR_FILE  = os.path.join(BASE_DIR, "sensor_si_audit.net")
LOG_FILE  = os.path.join(BASE_DIR, "sensor_si_audit.log")
REPORT_FILE = os.path.join(BASE_DIR, "sensor_si_report.txt")

TARGET_MODULE = "Redundant Sensory Array"

TEST_CRITERIA = {
    "v_3v3_sys":      {"name": "[01|Power] 3.3V Bus Power-on Steady State (~3.3V)", "min": 3.20, "max": 3.40, "unit": "V"},
    "i_inrush":       {"name": "[02|Power] Bypass Cap Array Inrush Current (<0.5A)", "min": -0.10, "max": 0.50, "unit": "A"},
    "v_i2c_scl_low":  {"name": "[05|I2C] SCL Falling Edge Strong Drive (<0.4V)",    "min": -0.10, "max": 0.40, "unit": "V"},
    "t_scl_rise":     {"name": "[06|I2C] SCL Loaded Rise Time (<1.0us)",           "min": 0.00, "max": 1.00, "unit": "us"},
    "t_sda_rise":     {"name": "[07|I2C] SDA Loaded Rise Time (<1.0us)",           "min": 0.00, "max": 1.00, "unit": "us"}
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

# Robust redundant pin extraction: Compatible with tools that may swap PinNumber and PinName
def get_net_robust(nets_dict, pin_number, pin_name):
    if pin_number in nets_dict: return nets_dict[pin_number]
    if pin_name in nets_dict: return nets_dict[pin_name]
    return f"NC_{uuid.uuid4().hex[:5]}"

def build_netlist():
    print("="*65)
    print(f"Launching All-Weather Crash-Resistant Version - Physical Layer SI Audit: {TARGET_MODULE}")
    
    nets_mcu  = parse_module_topology(JSON_FILE, TARGET_MODULE, "ESP32")
    nets_bmi  = parse_module_topology(JSON_FILE, TARGET_MODULE, "BMI160")
    nets_mpu  = parse_module_topology(JSON_FILE, TARGET_MODULE, "MPU-9250")
    nets_bmp  = parse_module_topology(JSON_FILE, TARGET_MODULE, "BMP280")
    nets_hmc  = parse_module_topology(JSON_FILE, TARGET_MODULE, "HMC5883L")
    
    # Extract ESP32 Driver-side Pins
    n_3v3  = get_net_robust(nets_mcu, "2", "3V3")
    n_scl  = get_net_robust(nets_mcu, "36", "IO22")
    n_sda  = get_net_robust(nets_mcu, "33", "IO21")
    n_sck  = get_net_robust(nets_mcu, "30", "IO18")
    n_mosi = get_net_robust(nets_mcu, "37", "IO23")
    n_miso = get_net_robust(nets_mcu, "31", "IO19")

    # Extract Sensor Receiver-side Pins
    bmp_vdd  = get_net_robust(nets_bmp, "8", "VDD")
    hmc_scl  = get_net_robust(nets_hmc, "1", "SCL")
    hmc_sda  = get_net_robust(nets_hmc, "16", "SDA")
    bmi_sck  = get_net_robust(nets_bmi, "13", "SCX")
    bmi_mosi = get_net_robust(nets_bmi, "14", "SDX")
    bmi_miso = get_net_robust(nets_bmi, "1", "SDO")

    print(f"  [INFO] Topology captured. Disregarding errors, forcing SPICE testbench generation...")
    print("="*65)

    def sp(n): return "0" if str(n).lower() in ["net_gnd", "0", "gnd"] else n

    netlist = [
        "* Robust Sensor SI Testbench (Always Run)",
        ".options abstol=1n reltol=0.01 vntol=1m method=gear",
        ".tran 10n 10m 0"
    ]

    # --- Core Crash-Prevention: Assign 1G pull-down to all nodes to eliminate Floating Node errors ---
    all_nodes = [n_3v3, n_scl, n_sda, n_sck, n_mosi, n_miso, bmp_vdd, hmc_scl, hmc_sda, bmi_sck, bmi_mosi, bmi_miso]
    for idx, node in enumerate(set(all_nodes)):
        if sp(node) != "0":
            netlist.append(f"R_DUMMY_{idx} {sp(node)} 0 1G")

    netlist.extend([
        "* [1] Power Rail Injection (Drive from MCU, Measure at Sensors)",
        f"V_3V3_IDEAL net_3v3_raw 0 PWL(0 0V 10u 3.3V 10m 3.3V)",
        f"R_LDO_OUT net_3v3_raw {sp(n_3v3)} 0.05",
        f"C_BYPASS_TOTAL {sp(bmp_vdd)} 0 500n",

        "* [2] Real PCB Parasitic Capacitance Injection (Loaded at Sensor end)",
        f"C_PARASITIC_SCL {sp(hmc_scl)} 0 40p",
        f"C_PARASITIC_SDA {sp(hmc_sda)} 0 40p",
        f"C_PARASITIC_SCK {sp(bmi_sck)} 0 20p",
        f"C_PARASITIC_MOSI {sp(bmi_mosi)} 0 20p",
        f"C_PARASITIC_MISO {sp(bmi_miso)} 0 20p",
        
        "* [3] ESP32 Internal Weak Pull-up (Mounted at Controller end)",
        f"R_INT_PU_SCL {sp(n_3v3)} {sp(n_scl)} 45k",
        f"R_INT_PU_SDA {sp(n_3v3)} {sp(n_sda)} 45k",

        "* [4] I2C 400kHz Driver (Signal issued by Controller)",
        f"V_SCL_DRIVE net_scl_drv 0 PULSE(0 3.3 1m 50n 50n 1.25u 2.5u 20)",
        f"R_SCL_DRV net_scl_drv {sp(n_scl)} 50", 
        f"V_SDA_DRIVE net_sda_drv 0 PULSE(0 3.3 1.1m 50n 50n 1.25u 2.5u 20)",
        f"R_SDA_DRV net_sda_drv {sp(n_sda)} 50",

        "* [5] SPI 8MHz Driver (MCU issues SCK/MOSI, Sensor returns MISO)",
        f"V_SCK_DRIVE net_sck_drv 0 PULSE(0 3.3 6m 5n 5n 57n 125n 50)",
        f"R_SCK_DRV net_sck_drv {sp(n_sck)} 30",
        f"V_MOSI_DRIVE net_mosi_drv 0 PULSE(0 3.3 6.02m 5n 5n 57n 125n 50)",
        f"R_MOSI_DRV net_mosi_drv {sp(n_mosi)} 30",
        f"V_MISO_DRIVE net_miso_drv 0 PULSE(0 3.3 7m 10n 10n 50n 125n 50)",
        f"R_MISO_DRV net_miso_drv {sp(bmi_miso)} 200",

        "* --- [6] Probe Matrix Deployment (Leapfrog measurement; open circuits yield 0V) ---",
        f".meas TRAN v_3v3_sys AVG V({sp(bmp_vdd)}) FROM 0.5m TO 0.9m",
        f".meas TRAN i_inrush  MAX I(R_LDO_OUT) FROM 0m TO 50u",
        f".meas TRAN v_i2c_scl_high MAX V({sp(hmc_scl)}) FROM 0.5m TO 0.9m",
        f".meas TRAN v_i2c_sda_high MAX V({sp(hmc_sda)}) FROM 0.5m TO 0.9m",
        f".meas TRAN v_i2c_scl_low MIN V({sp(hmc_scl)}) FROM 1.01m TO 1.02m",
        
        f".meas TRAN t_scl_rise TRIG V({sp(hmc_scl)}) VAL=0.99 RISE=2 TARG V({sp(hmc_scl)}) VAL=2.31 RISE=2",
        f".meas TRAN t_sda_rise TRIG V({sp(hmc_sda)}) VAL=0.99 RISE=2 TARG V({sp(hmc_sda)}) VAL=2.31 RISE=2",
        
        f".meas TRAN v_spi_sck_high MAX V({sp(bmi_sck)}) FROM 6.05m TO 6.1m",
        f".meas TRAN v_spi_mosi_high MAX V({sp(bmi_mosi)}) FROM 6.05m TO 6.1m",
        f".meas TRAN v_spi_miso_high MAX V({sp(n_miso)}) FROM 7.05m TO 7.1m"
    ])

    netlist.append(".end")
    return "\n".join(netlist)

def run_simulation():
    for f in [CIR_FILE, LOG_FILE, REPORT_FILE]:
        if os.path.exists(f): os.remove(f)
        
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
        # Execute SPICE; as long as syntax is correct, it will run despite topological logic errors
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
    except subprocess.CalledProcessError as e:
        # Graceful interception of fatal calculation crashes (e.g., division by zero). Score will be set to 0%.
        print(f"  [⚠️] WARNING: SPICE engine low-level calculation crash (Exit Code 1). Fatal short circuit loops may exist. Automatic score calculation: 0%.")
        
    results = {k: None for k in TEST_CRITERIA}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m: results[k] = float(m.group(1))
    
    report = ["="*65, " SENSOR BUS SIGNAL INTEGRITY MATRIX (ALWAYS RUN) ", "="*65]
    report.append(f"{'Audit Node (Process Step)':<38} | {'Value':<12} | {'Status'}")
    report.append("-" * 65)
    
    pass_count = 0
    for k, spec in TEST_CRITERIA.items():
        val = results[k]
        if val is not None and "rise" in k: val = val * 1e6 # Display seconds as microseconds
            
        is_ok = spec["min"] <= (val if val is not None else -999) <= spec["max"]
        if is_ok: pass_count += 1
        status_text = "PASS" if is_ok else "FAIL"
        
        if val is None: val_str = "N/A"
        elif "rise" in k: val_str = f"{val:>8.2f} us"
        elif "A" in spec["unit"]: val_str = f"{val*1000:>8.1f} mA"
        else: val_str = f"{val:>8.2f} {spec['unit']}"
            
        report.append(f"{spec['name']:<38} | {val_str:<12} | {status_text}")
        
    report.append("-" * 65)
    report.append(f"PASS RATE: {(pass_count/len(TEST_CRITERIA))*100:.1f}%")
    
    final_report_str = "\n".join(report)
    print(final_report_str)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_report_str)

if __name__ == "__main__": 
    run_simulation()