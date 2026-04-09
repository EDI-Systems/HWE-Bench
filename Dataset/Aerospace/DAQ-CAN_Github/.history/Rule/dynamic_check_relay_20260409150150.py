import os
import subprocess
import re
import json
from datetime import datetime
import uuid

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_realy.json")

CIR_FILE  = os.path.join(BASE_DIR, "relay_audit_pro.net")
LOG_FILE  = os.path.join(BASE_DIR, "relay_audit_pro.log")
REPORT_FILE = os.path.join(BASE_DIR, "relay_audit_report.txt")

# ================= 2. 全生命周期 10 项极限指标 =================
TEST_CRITERIA = {
    "v_gate_idle":   {"name": "01_Gate_Idle_Voltage",    "min": 0.00,  "max": 0.10,  "unit": "V"},
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
            print(f"❌ 拓扑断路: {comp}:{pin} 缺失 -> 悬空 {nc}")
            return [nc]
        return res
    return fetch

def build_netlist():
    fetch = get_topology()
    print("\n" + "="*80)
    print(">>> 纯净提取物理实体，注入 SPICE 仿真环境基建...")
    print("-" * 80)

    # 仅提取 JSON 中真实存在的芯片引脚网络
    n_gate  = fetch("DMN63D8", "G")[0]
    n_drain = fetch("DMN63D8", "D")[0]
    n_gnd   = fetch("DMN63D8", "S")[0]
    n_24v   = fetch("1N4148WX", "Cathode")[0]
    
    # 交叉验证防呆：继电器线圈一端和二极管阳极必须跟 MOSFET 漏极连在一起
    n_coil1 = fetch("G5Q-1A", "COIL_1")[0]
    n_anode = fetch("1N4148WX", "Anode")[0]
    
    if n_drain == n_coil1 == n_anode:
        print("✅ 物理验证: 漏极-线圈-二极管阳极 完美汇聚于节点:", n_drain)
    else:
        print("⚠️ 警告: 续流保护回路可能存在断路！")

    def sp(n): return "0" if n == n_gnd else n

    netlist = [
        "* Relay Actuation Testbench (Hardcoded Stimulus)",
        ".model N_DMN63D8 VDMOS(Vto=1.0 Rs=2.8 Kp=0.7 Cgdmax=10p Cjo=30p Vds=30 mtriodes=1)",
        ".model D_4148 D(Is=2.5n Rs=0.5 N=1.75 Cjo=4p tt=4n)",
        ".options abstol=1n reltol=0.01 vntol=1m cshunt=1p method=gear",
        ".tran 10n 10m 0 uic",
        
        # === 固化在测试台中的外部环境与信号源 ===
        f"V_24V {sp(n_24v)} 0 24V",
        "V_CTRL SIGNAL_IN 0 PULSE(0 3.3 2m 1u 1u 4m 10m)", # 测试激励
        
        # === 固化在测试台中的外围电阻 ===
        f"R4 SIGNAL_IN {sp(n_gate)} 250",
        f"R5 {sp(n_gate)} 0 10k",
        
        # === JSON 提取的真实被测硬件 ===
        f"M_Q1 {sp(n_drain)} {sp(n_gate)} 0 N_DMN63D8",
        f"L_COIL {sp(n_drain)} N_COIL_MID 10mH",
        f"R_COIL N_COIL_MID {sp(n_24v)} 1440",
        f"D_FLY {sp(n_drain)} {sp(n_24v)} D_4148",
        
        # === 全流程 10 项测量 ===
        f".meas TRAN v_gate_idle AVG V({sp(n_gate)}) FROM 0.5m TO 1.5m",
        f".meas TRAN v_drain_idle AVG V({sp(n_drain)}) FROM 0.5m TO 1.5m",
        f".meas TRAN v_gate_on AVG V({sp(n_gate)}) FROM 4m TO 5m",
        f".meas TRAN v_drain_on AVG V({sp(n_drain)}) FROM 4m TO 5m",
        f".meas TRAN i_coil_steady AVG I(R_COIL) FROM 5m TO 5.5m",
        
        "*.meas TRAN t_s WHEN V(SIGNAL_IN)=1.65 RISE=1",
        f".meas TRAN t_g WHEN V({sp(n_gate)})=1.65 RISE=1",
        # 修正：直接在测令中使用常数 2ms (2e-3) 作为基准触发时间，避免时序语法报错
        ".meas TRAN t_rc_gate PARAM (t_g-2e-3)*1e6",
        
        f".meas TRAN v_kick_peak MAX V({sp(n_drain)}) FROM 6m TO 6.5m",
        f".meas TRAN i_diode_peak MAX I(D_FLY) FROM 6m TO 6.5m",
        f".meas TRAN v_diode_fwd PARAM v_kick_peak-24.0",
        ".meas TRAN safe_soa PARAM v_kick_peak<29.0",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    try:
        with open(CIR_FILE, 'w') as f: f.write(build_netlist())
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True, timeout=30)
        
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

        report = ["="*85, f" 🛡️ Relay Testbench Audit Report | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "="*85]
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
        report.append(f"📊 模块保护合规率: {rate:.1f}%")
        if results.get('safe_soa') == 1.0:
            report.append("🏆 判定：续流回路畅通，反电动势成功钳位，MOSFET 处于绝对安全工作区 (SOA)！")
        else:
            report.append("💀 致命错误：未检测到钳位效应，出现超高压击穿尖峰，MOSFET 已烧毁！请检查 D2 是否漏接。")
        
        final_out = "\n".join(report)
        print("\n" + final_out)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f: f.write(final_out)

    except Exception as e: print(f"审计执行失败: {e}")

if __name__ == "__main__": run_simulation()