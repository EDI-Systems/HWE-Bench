import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_Multiplexer.json")
CIR_FILE = os.path.join(BASE_DIR, "ppmux_full_scope.net")
LOG_FILE = os.path.join(BASE_DIR, "ppmux_full_scope.log")
REPORT_FILE = os.path.join(BASE_DIR, "ppmux_comprehensive_report.txt")

TEST_CRITERIA = {
    # --- 阶段 1: 初始电池供电 (0-10ms) ---
    "v_bat_init":    {"name": "01_初始电池输出", "min": 3.4, "max": 3.8, "unit": "V"},
    
    # --- 阶段 2: USB 插入瞬态 (10ms 附近) ---
    "v_plug_dip":    {"name": "02_插入瞬态跌落", "min": 3.0, "max": 5.5, "unit": "V"},
    "i_usb_surge":   {"name": "03_插入冲击电流", "min": -2.0, "max": 0.5, "unit": "A"},
    "t_switch_on":   {"name": "04_USB接管速度",  "min": 0, "max": 2e-3, "unit": "s"}, 
    
    # --- 阶段 3: USB 稳态供电 (15-25ms) ---
    "v_usb_stable":  {"name": "05_USB稳态电压",  "min": 4.4, "max": 5.1, "unit": "V"},
    "v_gs_mos_off":  {"name": "06_MOS关断栅压",  "min": 0.5, "max": 5.5, "unit": "V"}, 
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
    """严格从 JSON 提取拓扑，如果缺失连接则产生悬空节点"""
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"Missing {JSON_FILE}")

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. 提取网络映射字典
    pins = {}
    for net in data.get("Power Path Multiplexer (PPMUX)", []):
        for conn in net["Connections"]:
            pins[f"{conn['ComponentID']}:{conn['PinName']}"] = net["net_id"]

    # 2. 严格定义各个部件的具体引脚所在的网络 ID
    # 规则：如果 JSON 里没写，分配一个带有 FLOAT 字样的乱码节点，确保它悬空
    n_usb = pins.get("USB:A9", "NC_FLOAT_USB")
    n_bat = pins.get("TP4057ST26P:3", "NC_FLOAT_BAT")
    n_gnd = pins.get("USB:A12", "NC_FLOAT_GND")
    
    # 设定 MOS 漏极所在网络作为整体系统的输出端，用于挂载负载和测量
    n_out = pins.get("IRLM:2", "NC_FLOAT_OUT") 

    # 核心元器件的每个引脚都必须单独从 JSON 拿映射
    d_a = pins.get("SS34LH:1", "NC_D_A")  # 二极管阳极
    d_k = pins.get("SS34LH:2", "NC_D_K")  # 二极管阴极
    m_g = pins.get("IRLM:1", "NC_M_G")    # MOS Gate
    m_d = pins.get("IRLM:2", "NC_M_D")    # MOS Drain
    m_s = pins.get("IRLM:3", "NC_M_S")    # MOS Source

    # 将识别到的地网络强制转换为 SPICE 识别的 0 节点
    def n(name): return "0" if name == n_gnd else name

    # 3. 构造网表 (完全剥离了理想化假设)
    netlist = [
        "* Comprehensive PPMUX STRICT Validation Netlist",
        ".model D_SCHOTTKY D(Is=1e-5 Rs=0.05 N=1.1)",
        ".model P_MOS VDMOS(pchan Vto=-1.2 Rs=0.05 Kp=2.0)",
        ".tran 0 50m 0 5u", 
        
        # --- 电源与负载 ---
        # 激励源绑定在从 JSON 提取的对应引脚网络上
        f"V_BAT {n(n_bat)} 0 3.7",
        f"V_USB {n(n_usb)} 0 PULSE(0 5 10m 50u 50u 20m 50m)",
        # 负载统一挂载在 n_out (即 MOS 漏极所在网络)
        f"R_LOAD {n(n_out)} 0 100",
        f"C_OUT {n(n_out)} 0 10u",
        
        # --- 核心拓扑 (严格依据 JSON 连接) ---
        f"D9 {n(d_a)} {n(d_k)} D_SCHOTTKY",
        f"M1 {n(m_d)} {n(m_g)} {n(m_s)} {n(m_s)} P_MOS",
        
        # --- 精细化测量指令 (基于 n_out 进行测量) ---
        f".meas TRAN v_bat_init AVG V({n(n_out)}) FROM 2m TO 8m",
        f".meas TRAN v_plug_dip MIN V({n(n_out)}) FROM 9m TO 13m",
        f".meas TRAN i_usb_surge MIN I(V_USB) FROM 9.5m TO 11m",
        f".meas TRAN t_switch_on WHEN V({n(n_out)})=4.3 RISE=1", 
        
        f".meas TRAN v_usb_stable AVG V({n(n_out)}) FROM 18m TO 25m",
        f".meas TRAN v_gs_mos_off AVG (V({n(m_g)})-V({n(m_s)})) FROM 18m TO 25m",
        f".meas TRAN i_leak_bat AVG I(V_BAT) FROM 18m TO 25m",
        # 二极管功耗测量：利用其自身的阳极/阴极网络计算
        f".meas TRAN p_loss_d9 AVG (V({n(d_a)})-V({n(d_k)}))*I(D9) FROM 18m TO 25m",
        
        f".meas TRAN v_unplug_dip MIN V({n(n_out)}) FROM 29m TO 35m",
        f".meas TRAN t_recovery WHEN V({n(n_out)})=3.5 FALL=1",
        
        f".meas TRAN v_bat_final AVG V({n(n_out)}) FROM 42m TO 48m",
        f".meas TRAN v_gs_mos_on AVG (V({n(m_g)})-V({n(m_s)})) FROM 42m TO 48m",
        ".end"
    ]
    
    final_netlist = "\n".join(netlist)
    
    # 调试用：打印生成的网表，方便检查是否真的正确映射了 JSON
    print("\n--- 动态生成的 SPICE 网表预览 ---")
    print(final_netlist)
    print("---------------------------------\n")
    
    return final_netlist

def run_simulation():
    try:
        content = build_dynamic_netlist()
    except Exception as e:
        print(f"网表生成失败: {e}")
        return

    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(">>> 正在进行多时间点全扫描验证...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): 
        print("错误：未能生成 LTspice Log 文件。")
        return
        
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_raw = f.read()

    # 报告生成逻辑保持不变
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