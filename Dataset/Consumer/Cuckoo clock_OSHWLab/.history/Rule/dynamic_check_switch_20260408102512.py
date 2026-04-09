import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_shifter.json")
CIR_FILE = os.path.join(BASE_DIR, "motor_switch_strict.net")
LOG_FILE = os.path.join(BASE_DIR, "motor_switch_strict.log")
REPORT_FILE = os.path.join(BASE_DIR, "motor_switch_report.txt")

# ================= 2. 全维度判定标准 =================
TEST_CRITERIA = {
    # --- 阶段 1: 待机状态 (0-10ms) ---
    "i_leak_off":      {"name": "01_关断态漏电流",   "min": -1e-6, "max": 1e-6, "unit": "A"},
    "v_motor_off":     {"name": "02_关断态电机压降", "min": -0.1,  "max": 0.1,  "unit": "V"},
    
    # --- 阶段 2: 启动瞬态与浪涌缓冲 (10ms 附近) ---
    # TRIG 和 TARG 配合测量电压从 4.5V 下降到 0.5V 的时间，验证 RC 缓启动是否生效
    "t_soft_start":    {"name": "03_缓启动上升时间", "min": 0.5e-3,"max": 5e-3, "unit": "s"}, 
    "i_inrush_peak":   {"name": "04_启动浪涌峰值",   "min": 0.0,   "max": 1.5,  "unit": "A"}, # 假设稳态1A，限制峰值不超过1.5A
    
    # --- 阶段 3: 稳态运行 (20-30ms) ---
    "v_drop_on":       {"name": "05_MOS导通管压降",  "min": 0.0,   "max": 0.15, "unit": "V"}, # 评估 Rdson 是否足够小
    "i_motor_run":     {"name": "06_电机稳态电流",   "min": 0.8,   "max": 1.2,  "unit": "A"},
    
    # --- 阶段 4: 关断瞬态与续流保护 (30ms 附近) ---
    # 5V 系统关断时，如果续流二极管有效，尖峰会被钳位在 5V + 0.7V 左右
    "v_flyback_spike": {"name": "07_关断反电动势尖峰","min": 5.0,   "max": 6.5,  "unit": "V"} 
}

def build_motor_netlist():
    """严格从 JSON 提取电机驱动拓扑"""
    if not os.path.exists(JSON_FILE):
        print(f"警告: 找不到 {JSON_FILE}，将尝试使用测试模式运行（可能失败）")
        data = {}
    else:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

    # 1. 提取网络映射字典 (请确保 JSON 中的模块名称匹配)
    pins = {}
    for net in data.get("Motor Load Switch & Inrush Buffer", []):
        for conn in net["Connections"]:
            pins[f"{conn['ComponentID']}:{conn['PinName']}"] = net["net_id"]

    # 2. 严格定义拓扑网络映射
    # 【注意】请将下面的 "MCU:1", "NMOS:1" 等替换为你 JSON 里真实的元件/引脚名！
    n_ctrl = pins.get("MCU:GPIO_MOTOR", "NC_FLOAT_CTRL")  # MCU 控制信号
    n_bat  = pins.get("VBAT:OUT", "NC_FLOAT_BAT")         # 系统电源 (如5V)
    n_gnd  = pins.get("GND:1", "NC_FLOAT_GND")            # 系统地
    
    # NMOS (低边开关)
    m_g = pins.get("NMOS:1", "NC_MOS_G")
    m_d = pins.get("NMOS:2", "NC_MOS_D")
    m_s = pins.get("NMOS:3", "NC_MOS_S")
    
    # 续流二极管 (并联在电机两端：阴极接电源，阳极接 MOS_Drain)
    d_a = pins.get("D_FLYBACK:1", "NC_D_A")
    d_k = pins.get("D_FLYBACK:2", "NC_D_K")

    # 缓启动 RC 网络 (如果 JSON 里有这些元件)
    rg_1 = pins.get("R_GATE:1", "NC_RG_1")
    rg_2 = pins.get("R_GATE:2", "NC_RG_2")
    cg_1 = pins.get("C_BUFFER:1", "NC_CG_1")
    cg_2 = pins.get("C_BUFFER:2", "NC_CG_2")

    def n(name): return "0" if name == n_gnd else name

    # 3. 构造网表
    netlist = [
        "* Motor Load Switch & Inrush Buffer STRICT Validation",
        ".model D_FAST D(Is=1e-5 Rs=0.05 N=1.1 Cjo=50p tt=10n)", # 快恢复/肖特基二极管模型
        ".model N_MOS VDMOS(nchan Vto=1.5 Rs=0.02 Kp=10.0)",     # 低内阻 NMOS 模型
        ".tran 0 50m 0 1u", # 电感瞬态需要极高分辨率(1us)
        
        # --- 电源与控制信号 ---
        f"V_BAT {n(n_bat)} 0 5",
        # 控制信号：10ms 开启 (3.3V)，30ms 关闭 (0V)
        f"V_CTRL {n(n_ctrl)} 0 PULSE(0 3.3 10m 1u 1u 20m 50m)",
        
        # --- 提取到的核心物理拓扑 ---
        f"M1 {n(m_d)} {n(m_g)} {n(m_s)} {n(m_s)} N_MOS",
        f"D_FWD {n(d_a)} {n(d_k)} D_FAST",
        
        # 填充 RC 缓启动网络 (确保控制信号经过 RC 延迟)
        f"R_GATE {n(rg_1)} {n(rg_2)} 10k",
        f"C_BUF  {n(cg_1)} {n(cg_2)} 1uF",
        
        # --- 电机等效负载模型 (L-R 串联模型) ---
        # 假设 JSON 里没有提供详细的电机模型参数，我们在测试脚本中补全电机连接
        # 电机接在 BAT 和 MOS_Drain 之间
        f"R_MOTOR {n(n_bat)} N_MOTOR_MID 5",   # 电机线圈内阻 5欧姆 -> 稳态电流 = 5V/5R = 1A
        f"L_MOTOR N_MOTOR_MID {n(m_d)} 1mH",   # 电机感性负载 1mH
        
        # --- 精细化测量指令 ---
        # 阶段 1: 待机漏电
        f".meas TRAN i_leak_off AVG I(V_BAT) FROM 2m TO 8m",
        f".meas TRAN v_motor_off AVG (V({n(n_bat)})-V({n(m_d)})) FROM 2m TO 8m",
        
        # 阶段 2: 启动动态 (测量 Drain 电压从高电平跌落到低电平的延迟时间)
        f".meas TRAN t_soft_start TRIG V({n(m_d)}) VAL=4.5 FALL=1 TARG V({n(m_d)}) VAL=0.5 FALL=1",
        f".meas TRAN i_inrush_peak MAX I(L_MOTOR) FROM 9m TO 15m",
        
        # 阶段 3: 稳态运行
        f".meas TRAN v_drop_on AVG V({n(m_d)}) FROM 20m TO 28m",
        f".meas TRAN i_motor_run AVG I(L_MOTOR) FROM 20m TO 28m",
        
        # 阶段 4: 关断反电动势尖峰 (捕捉 30ms 关断瞬间的最高电压)
        f".meas TRAN v_flyback_spike MAX V({n(m_d)}) FROM 29.5m TO 35m",
        
        ".end"
    ]
    
    final_netlist = "\n".join(netlist)
    print("\n--- 动态生成的 SPICE 网表预览 ---")
    print(final_netlist)
    print("---------------------------------\n")
    return final_netlist

def run_simulation():
    try:
        content = build_motor_netlist()
    except Exception as e:
        print(f"网表生成失败: {e}")
        return

    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(">>> 正在进行电机驱动多时间点全扫描验证...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): 
        print("错误：未能生成 LTspice Log 文件。")
        return
        
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_raw = f.read()

    # 报告生成逻辑
    report = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append("="*95)
    report.append(f" Motor Load Switch 模块全流程仿真报告 | 生成时间: {timestamp}")
    report.append("="*95)
    report.append(f"{'指标代码':<18} | {'测试项名称':<22} | {'实测值':<15} | {'判定标准':<15} | {'状态'}")
    report.append("-" * 95)

    pass_count = 0
    for key, spec in TEST_CRITERIA.items():
        match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log_raw, re.I)
        val = float(match.group(1)) if match else None
        
        if val is not None:
            # 针对时间的科学计数法优化显示
            display_val = val
            if spec['unit'] == 's' and val < 0.1:
                val_str = f"{val*1000:>10.3f} ms"
            else:
                val_str = f"{val:>11.4f} {spec['unit']}"
                
            is_ok = spec["min"] <= val <= spec["max"]
            status = "✅ PASS" if is_ok else "❌ FAIL"
            if is_ok: pass_count += 1
        else:
            status = "⚠️ MISSING"
            val_str = "N/A"
            
        range_str = f"{spec['min']}~{spec['max']}"
        report.append(f"{key:<18} | {spec['name']:<20} | {val_str:<15} | {range_str:<15} | {status}")

    pass_rate = (pass_count / len(TEST_CRITERIA)) * 100
    report.append("-" * 95)
    report.append(f"结果总结: 共计 {len(TEST_CRITERIA)} 个监测点 | 通过 {pass_count} 项 | 失败 {len(TEST_CRITERIA)-pass_count} 项")
    report.append(f"📊 模块总通过率 (Pass Rate): {pass_rate:.2f}%")
    report.append("="*95)

    output = "\n".join(report)
    print(output)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"\n>>> 详细报告已保存至: {REPORT_FILE}")

if __name__ == "__main__":
    run_simulation()