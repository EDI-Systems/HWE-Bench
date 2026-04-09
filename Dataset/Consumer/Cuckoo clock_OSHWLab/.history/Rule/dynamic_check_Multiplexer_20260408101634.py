import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_Multiplexer.json")
CIR_FILE = os.path.join(BASE_DIR, "ppmux_full_scope.net")
LOG_FILE = os.path.join(BASE_DIR, "ppmux_full_scope.log")
REPORT_FILE = os.path.join(BASE_DIR, "ppmux_comprehensive_report.txt")

# ================= 2. 全维度判定标准 =================
# 涵盖：启动、插入、稳态、拔出、恢复 五大阶段
TEST_CRITERIA = {
    # --- 阶段 1: 初始电池供电 (0-10ms) ---
    "v_bat_init":    {"name": "01_初始电池输出", "min": 3.4, "max": 3.8, "unit": "V"},
    
    # --- 阶段 2: USB 插入瞬态 (10ms 附近) ---
    "v_plug_dip":    {"name": "02_插入瞬态跌落", "min": 3.0, "max": 5.5, "unit": "V"},
    "i_usb_surge":   {"name": "03_插入冲击电流", "min": -2.0, "max": 0.5, "unit": "A"},
    "t_switch_on":   {"name": "04_USB接管速度",  "min": 0, "max": 2e-3, "unit": "s"}, # 切换应在2ms内完成
    
    # --- 阶段 3: USB 稳态供电 (15-25ms) ---
    "v_usb_stable":  {"name": "05_USB稳态电压",  "min": 4.4, "max": 5.1, "unit": "V"},
    "v_gs_mos_off":  {"name": "06_MOS关断栅压",  "min": 0.5, "max": 5.5, "unit": "V"}, # Vgs应为正(关断)
    "i_leak_bat":    {"name": "07_电池倒灌电流", "min": -1e-6, "max": 1e-9, "unit": "A"},
    "p_loss_d9":     {"name": "08_二极管功耗",   "min": 0, "max": 0.1, "unit": "W"},
    
    # --- 阶段 4: USB 拔出瞬态 (30ms 附近) ---
    "v_unplug_dip":  {"name": "09_拔出瞬态跌落", "min": 2.7, "max": 4.5, "unit": "V"},
    "t_recovery":    {"name": "10_电池恢复速度", "min": 0, "max": 5e-3, "unit": "s"},
    
    # --- 阶段 5: 回归电池稳态 (40-50ms) ---
    "v_bat_final":   {"name": "11_后期电池输出", "min": 3.4, "max": 3.8, "unit": "V"},
    "v_gs_mos_on":   {"name": "12_MOS导通栅压",  "min": -5.0, "max": -2.5, "unit": "V"}
}

def build_dynamic_netlist():
    """从 JSON 提取拓扑并注入多节点测量指令"""
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"Missing {JSON_FILE}")

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 提取网络映射
    pins = {}
    for net in data.get("Power Path Multiplexer (PPMUX)", []):
        for conn in net["Connections"]:
            pins[f"{conn['ComponentID']}:{conn['PinName']}"] = net["net_id"]

    # 识别核心节点
    n_usb = pins.get("USB:A9", "VBUS")
    n_bat = pins.get("TP4057ST26P:3", "VBAT")
    n_out = pins.get("IRLM:2", "VOUT")
    n_gnd = pins.get("USB:A12", "GND")
    
    m_gate = pins.get("IRLM:1", n_usb)
    m_src  = pins.get("IRLM:3", n_bat)

    def n(name): return "0" if name == n_gnd else name

    netlist = [
        "* Comprehensive PPMUX Validation Netlist",
        ".model D_SCHOTTKY D(Is=1e-5 Rs=0.05 N=1.1)",
        ".model P_MOS VDMOS(pchan Vto=-1.2 Rs=0.05 Kp=2.0)",
        ".tran 0 50m 0 5u", # 提高采样率以捕捉毛刺
        
        # 电源与负载
        f"V_BAT {n(n_bat)} 0 3.7",
        f"V_USB {n(n_usb)} 0 PULSE(0 5 10m 50u 50u 20m 50m)",
        f"R_LOAD {n(n_out)} 0 100",
        f"C_OUT {n(n_out)} 0 10u", # 模拟真实输出电容
        
        # 核心拓扑
        f"D9 {n(n_usb)} {n(n_out)} D_SCHOTTKY",
        f"M1 {n(n_out)} {n(m_gate)} {n(m_src)} {n(m_src)} P_MOS",
        
        # --- 精细化测量指令 ---
        # 阶段 1:
        f".meas TRAN v_bat_init AVG V({n(n_out)}) FROM 2m TO 8m",
        # 阶段 2:
        f".meas TRAN v_plug_dip MIN V({n(n_out)}) FROM 9m TO 13m",
        f".meas TRAN i_usb_surge MIN I(V_USB) FROM 9.5m TO 11m",
        f".meas TRAN t_switch_on WHEN V({n(n_out)})=4.3 RISE=1", # 计算达到稳态的时间点
        # 阶段 3:
        f".meas TRAN v_usb_stable AVG V({n(n_out)}) FROM 18m TO 25m",
        f".meas TRAN v_gs_mos_off AVG (V({n(m_gate)})-V({n(m_src)})) FROM 18m TO 25m",
        f".meas TRAN i_leak_bat AVG I(V_BAT) FROM 18m TO 25m",
        f".meas TRAN p_loss_d9 AVG (V({n(n_usb)})-V({n(n_out)}))*I(D9) FROM 18m TO 25m",
        # 阶段 4:
        f".meas TRAN v_unplug_dip MIN V({n(n_out)}) FROM 29m TO 35m",
        f".meas TRAN t_recovery WHEN V({n(n_out)})=3.5 FALL=1",
        # 阶段 5:
        f".meas TRAN v_bat_final AVG V({n(n_out)}) FROM 42m TO 48m",
        f".meas TRAN v_gs_mos_on AVG (V({n(m_gate)})-V({n(m_src)})) FROM 42m TO 48m",
        
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    content = build_dynamic_netlist()
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(">>> 正在进行多时间点全扫描验证...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_raw = f.read()

    # 报告生成
    report = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append("="*90)
    report.append(f" PPMUX 模块全流程仿真报告 | 生成时间: {timestamp}")
    report.append("="*90)
    report.append(f"{'指标代码':<18} | {'测试项名称':<20} | {'实测值':<15} | {'判定标准':<15} | {'状态'}")
    report.append("-" * 90)

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
        report.append(f"{key:<18} | {spec['name']:<16} | {val_str:<15} | {range_str:<15} | {status}")

    pass_rate = (pass_count / len(TEST_CRITERIA)) * 100
    report.append("-" * 90)
    report.append(f"结果总结: 共计 {len(TEST_CRITERIA)} 个监测点 | 通过 {pass_count} 项 | 失败 {len(TEST_CRITERIA)-pass_count} 项")
    report.append(f"📊 模块总通过率 (Pass Rate): {pass_rate:.2f}%")
    report.append("="*90)

    output = "\n".join(report)
    print(output)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"\n>>> 详细报告已保存至: {REPORT_FILE}")

if __name__ == "__main__":
    run_simulation()