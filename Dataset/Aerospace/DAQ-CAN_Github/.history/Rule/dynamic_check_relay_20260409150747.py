import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_relay.json")

CIR_FILE  = os.path.join(BASE_DIR, "relay_audit_pro.net")
LOG_FILE  = os.path.join(BASE_DIR, "relay_audit_pro.log")
REPORT_FILE = os.path.join(BASE_DIR, "relay_audit_report.txt")

# ================= 2. 全生命周期 10 项极限指标 =================
TEST_CRITERIA = {
    # 修正：放宽 0V 判定的浮点数容差，防止 -0.00001V 被误判为 FAIL
    "v_gate_idle":   {"name": "01_Gate_Idle_Voltage",    "min": -0.05, "max": 0.10,  "unit": "V"},
    "v_drain_idle":  {"name": "02_Drain_Idle_Voltage",   "min": 23.90, "max": 24.10, "unit": "V"},
    "v_gate_on":     {"name": "03_Gate_Active_Voltage",  "min": 3.10,  "max": 3.35,  "unit": "V"},
    "v_drain_on":    {"name": "04_Drain_Active_Drop",    "min": 0.00,  "max": 0.50,  "unit": "V"},
    "i_coil_steady": {"name": "05_Coil_Steady_Current",  "min": 10.0,  "max": 25.0,  "unit": "mA"},
    "t_rc_gate":     {"name": "06_Gate_Drive_RC_Delay",  "min": 0.1,   "max": 5.0,   "unit": "us"},
    "v_kick_peak":   {"name": "07_Kickback_Peak_Voltage","min": 24.10, "max": 25.50, "unit": "V"},
    "i_diode_peak":  {"name": "08_Flyback_Diode_Current","min": 10.0,  "max": 25.0,  "unit": "mA"},
    "v_diode_fwd":   {"name": "09_Diode_Forward_Drop",   "min": 0.60,  "max": 1.20,  "unit": "V"},
    "safe_soa":      {"name": "10_MOSFET_SOA_Safety",    "min": 1.0,   "max": 1.0,   "unit": "bool"}
}

def get_topology():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"未找到 JSON 文件: {JSON_FILE}")
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("24V Relay Actuation & Protection", [])
    pin_to_nets = {}
    for net in target:
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            if key not in pin_to_nets: pin_to_nets[key] = []
            if net["net_id"] not in pin_to_nets[key]: pin_to_nets[key].append(net["net_id"])
            
    def fetch(comp, pin):
        res = pin_to_nets.get(f"{comp}:{pin}", [])
        if not res:
            nc = f"NC_{uuid.uuid4().hex[:4]}"
            print(f"❌ 拓扑断路: 找不到 {comp}:{pin} -> 悬空 {nc}")
            return [nc]
        return res
    return fetch

def build_netlist():
    fetch = get_topology()
    print("\n" + "="*80)
    print(">>> 🔌 正在从 JSON 读取物理拓扑，构建动态测试台...")
    print("-" * 80)

    # =========================================================================
    # 核心：动态读取 JSON 中的 net_id。如果 JSON 变了，这些名字也会跟着变
    # =========================================================================
    n_mos_g   = fetch("DMN63D8", "G")[0]
    n_mos_d   = fetch("DMN63D8", "D")[0]
    n_mos_s   = fetch("DMN63D8", "S")[0]
    
    n_coil_1  = fetch("G5Q-1A", "COIL_1")[0]
    n_coil_2  = fetch("G5Q-1A", "COIL_2")[0]
    
    n_dio_a   = fetch("1N4148WX", "Anode")[0]
    n_dio_k   = fetch("1N4148WX", "Cathode")[0]

    # 将被读取到的源极网络定义为 SPICE 的全局地 (0)
    def sp(n): return "0" if n == n_mos_s else n

    netlist = [
        "* Dynamic Topology Relay Testbench",
        ".model N_DMN63D8 VDMOS(Vto=1.0 Rs=2.8 Kp=0.7 Cgdmax=10p Cjo=30p Vds=30 mtriodes=1)",
        ".model D_4148 D(Is=2.5n Rs=0.5 N=1.75 Cjo=4p tt=4n)",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 10n 10m 0 uic",
        
        # =========================================================================
        # 1. 固化在测试台 (Testbench) 中的外部刺激环境
        # =========================================================================
        # 24V 电源挂载在继电器线圈2 (n_coil_2) 所在的网络上
        f"V_24V_PWR {sp(n_coil_2)} 0 24V",
        # 产生单片机控制脉冲 (2ms开启，6ms关闭)
        "V_CTRL_PULSE SIGNAL_IN 0 PULSE(0 3.3 2m 1u 1u 4m 10m)", 
        # 外围栅极驱动电阻挂载在 MOSFET 栅极 (n_mos_g) 所在的网络上
        f"R_GATE SIGNAL_IN {sp(n_mos_g)} 250",
        f"R_PD {sp(n_mos_g)} 0 10k",
        
        # =========================================================================
        # 2. 从 JSON 动态实例化的被测设备 (DUT: Device Under Test)
        # =========================================================================
        # 它们之间的连线完全取决于读取到的 net_id (例如 n_mos_d 和 n_coil_1 是否相等)
        f"M_Q1 {sp(n_mos_d)} {sp(n_mos_g)} 0 N_DMN63D8",
        
        # 继电器线圈电感等效
        f"L_COIL {sp(n_coil_1)} N_COIL_MID 10mH",
        f"R_COIL N_COIL_MID {sp(n_coil_2)} 1440",
        
        # 续流二极管
        f"D_FLY {sp(n_dio_a)} {sp(n_dio_k)} D_4148",
        
        # =========================================================================
        # 3. 测量指令 (使用读取到的关键网络进行测量)
        # =========================================================================
        f".meas TRAN v_gate_idle AVG V({sp(n_mos_g)}) FROM 0.5m TO 1.5m",
        f".meas TRAN v_drain_idle AVG V({sp(n_mos_d)}) FROM 0.5m TO 1.5m",
        f".meas TRAN v_gate_on AVG V({sp(n_mos_g)}) FROM 4m TO 5m",
        f".meas TRAN v_drain_on AVG V({sp(n_mos_d)}) FROM 4m TO 5m",
        
        # 修正：加入 ABS() 获取电流绝对值，防止被判负数
        f".meas TRAN i_coil_steady AVG ABS(I(R_COIL)) FROM 5m TO 5.5m",
        
        "*.meas TRAN t_s WHEN V(SIGNAL_IN)=1.65 RISE=1",
        f".meas TRAN t_g WHEN V({sp(n_mos_g)})=1.65 RISE=1",
        ".meas TRAN t_rc_gate PARAM (t_g-2e-3)*1e6",
        
        # 反电动势与钳位监测点在 MOSFET 的漏极上
        f".meas TRAN v_kick_peak MAX V({sp(n_mos_d)}) FROM 6m TO 6.5m",
        f".meas TRAN i_diode_peak MAX ABS(I(D_FLY)) FROM 6m TO 6.5m",
        f".meas TRAN v_diode_fwd PARAM v_kick_peak-24.0",
        ".meas TRAN safe_soa PARAM v_kick_peak<29.0",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    try:
        with open(CIR_FILE, 'w', encoding='utf-8') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
        if not os.path.exists(LOG_FILE): return
        with open(LOG_FILE, 'r', errors='ignore') as f: log = f.read()

        results = {}
        for k in TEST_CRITERIA.keys():
            m = re.search(rf"{k}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
            if m:
                val = float(m.group(1))
                if "i_" in k: val = val * 1000  # 转换为 mA
                results[k] = val
            else:
                results[k] = None

        report = ["="*85, f" 🛡️ Real Topology Relay Audit Report | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "="*85]
        report.append(f"{'Audit Item':<30} | {'Value':<15} | {'Status'}")
        report.append("-" * 85)

        pass_count = 0
        for k, spec in TEST_CRITERIA.items():
            val = results.get(k)
            is_ok = spec["min"] <= val <= spec["max"] if val is not None else False
            if is_ok: pass_count += 1
            status = "✅ PASS" if is_ok else "❌ FAIL (DANGER!)"
            val_str = f"{val:>11.3f} {spec['unit']}" if val is not None else "N/A"
            report.append(f"{spec['name']:<30} | {val_str:<15} | {status}")

        report.append("-" * 85)
        rate = (pass_count/len(TEST_CRITERIA))*100
        report.append(f"passrate: {rate:.1f}%")
        
        final_out = "\n".join(report)
        print("\n" + final_out)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_out)

    except Exception as e: print(f"审计执行失败: {e}")

if __name__ == "__main__": run_simulation()