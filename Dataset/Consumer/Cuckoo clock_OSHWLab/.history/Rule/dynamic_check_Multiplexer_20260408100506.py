import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
# JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_shifter.json")
CIR_FILE = os.path.join(BASE_DIR, "mutiple.net")
LOG_FILE = os.path.join(BASE_DIR, "mutiple.log")
REPORT_FILE = os.path.join(BASE_DIR, "mutiple_report.txt")

# ================= 2. 扩展验证矩阵 (10 个关键测量点) =================
# 涵盖电压、电流、延迟、功耗及效率
TEST_POINTS = [
    {"id": "V_MCU_HI",     "min": 4.8,   "max": 5.2,   "name": "MCU PD3 驱动高电平", "unit": "V"},
    {"id": "V_LED_DROP",   "min": 1.1,   "max": 1.5,   "name": "PC817 LED端导通压降", "unit": "V"},
    {"id": "I_LED_DRV",    "min": 7.0e-3,"max": 9.5e-3,"name": "LED 驱动电流 (If)", "unit": "A"},
    {"id": "V_MCU_LO",     "min": 0.0,   "max": 0.5,   "name": "输出侧饱和导通电平 (Vol)", "unit": "V"},
    {"id": "V_MCU_HI_OUT", "min": 4.5,   "max": 5.1,   "name": "输出侧截止高电平 (Voh)", "unit": "V"},
    {"id": "T_PROP_DELAY", "min": -1e-8, "max": 3e-5,  "name": "光耦隔离传输总延迟", "unit": "s"},
    {"id": "P_R2_LOSS",    "min": 0.01,  "max": 0.05,  "name": "限流电阻 R2 实时功耗", "unit": "W"},
    {"id": "CTR_REAL",     "min": 0.5,   "max": 5.0,   "name": "有效电流传输比 (CTR)"},
    {"id": "V_GND_REF",    "min": -0.1,  "max": 0.1,   "name": "系统地参考电位", "unit": "V"},
    {"id": "I_OUT_SAT",    "min": 4.0e-4,"max": 6.0e-4,"name": "输出侧饱和负载电流", "unit": "A"}
]

def build_netlist():
    """解析 JSON 拓扑并生成包含 10 个测量点的 SPICE 网表"""
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target = data.get("Motor Signal Converter with Optoisolation", [])
    pins = {f"{c['ComponentID']}:{c['PinName']}": n['net_id'] for n in target for c in n['Connections']}

    # 动态匹配引脚
    n_mcu   = pins.get("ATmega328p:PD3", "MCU_DRIVE_PD3")
    n_anode = pins.get("PC817:Anode", "OPTO_LED_ANODE")
    n_cath  = pins.get("PC817:Cathode", "GND")
    n_coll  = pins.get("PC817:Collector", "MCU_MOTOR_SENSE") 
    n_emit  = pins.get("PC817:Emitter", "GND")
    n_gnd   = pins.get("AMS1117:GND/ADJ", "GND")

    def is_gnd(node_name):
        return node_name.upper() in ["GND", "0"]

    netlist = [
        "* Tapuino Motor Signal Converter Comprehensive Verify",
        # 高精度光耦模型
        ".subckt PC817_Exact 1 2 4 3",
        "D1 1 2 LED_Model",
        "G1 4 3 1 2 2.0", # 假设 CTR=200%
        ".model LED_Model D(Is=1e-14 N=1.5 Rs=0.1)",
        ".ends PC817_Exact",
        
        ".tran 0 50m 0 100u",
        
        # 核心激励与物理拓扑
        f"V_MCU {n_mcu} 0 PULSE(0 5 1m 1n 1n 10m 20m)",
        f"R2 {n_mcu} {n_anode} 470",
        f"XU3 {n_anode} {n_cath} {n_coll} {n_emit} PC817_Exact",
        
        # 隔离侧上拉负载
        f"V_ISO VCC_ISO 0 5",
        f"R_PULLUP VCC_ISO {n_coll} 10k"
    ]

    # 安全处理地电位节点
    if not is_gnd(n_cath): netlist.append(f"V_CATH_TIE {n_cath} 0 0")
    if not is_gnd(n_gnd):  netlist.append(f"V_GND_TIE {n_gnd} 0 0")

    # --- 10 个智能测量指令 ---
    netlist.append(f".meas TRAN V_MCU_HI MAX V({n_mcu})")
    
    # 压降测量：自动处理单端或差分
    if is_gnd(n_cath):
        netlist.append(f".meas TRAN V_LED_DROP AVG V({n_anode}) FROM 5m TO 6m")
    else:
        netlist.append(f".meas TRAN V_LED_DROP AVG V({n_anode})-V({n_cath}) FROM 5m TO 6m")

    netlist.append(f".meas TRAN I_LED_DRV AVG I(R2) FROM 5m TO 6m")
    netlist.append(f".meas TRAN V_MCU_LO MIN V({n_coll}) FROM 5m TO 6m")
    netlist.append(f".meas TRAN V_MCU_HI_OUT MAX V({n_coll}) FROM 15m TO 16m")
    # 动态特性：触发延迟
    netlist.append(f".meas TRAN T_PROP_DELAY TRIG V({n_mcu})=2.5 RISE=1 TARG V({n_coll})=2.5 FALL=1")
    # 功耗与效率
    netlist.append(f".meas TRAN P_R2_LOSS AVG (V({n_mcu})-V({n_anode}))*I(R2) FROM 5m TO 6m")
    netlist.append(f".meas TRAN CTR_REAL PARAM abs(I(R_PULLUP)/I(R2))") 
    
    if is_gnd(n_gnd):
        netlist.append(f".meas TRAN V_GND_REF PARAM 0")
    else:
        netlist.append(f".meas TRAN V_GND_REF AVG V({n_gnd})")
        
    netlist.append(f".meas TRAN I_OUT_SAT AVG I(R_PULLUP) FROM 5m TO 6m")
    netlist.append(".end")

    return "\n".join(netlist)

def run_and_report():
    # 生成网表并执行仿真
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(build_netlist())
    
    print(f">>> 正在提取 JSON 拓扑并启动 10 点深度验证...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE):
        print("[错误] 仿真未能生成日志文件。")
        return

    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log = f.read()

    # 报告生成
    report = [
        "=======================================================",
        f"Tapuino 电机转换模块深度验证报告 | {datetime.now().strftime('%Y-%m-%d')}",
        "-------------------------------------------------------",
        f"{'检测项目':<28} | {'测量值':<12} | {'判定'}"
    ]

    pass_count = 0
    for tp in TEST_POINTS:
        # 使用正则表达式从 log 提取测量数据
        match = re.search(rf"{tp['id']}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log, re.I)
        val = float(match.group(1)) if match else float('nan')
        
        status = "PASS" if tp['min'] <= val <= tp['max'] else "FAIL"
        if status == "PASS": pass_count += 1
        
        unit = tp.get('unit', '')
        report.append(f"{tp['name']:<28} | {val:>10.4f} {unit:<2} | {status}")

    report.append("-------------------------------------------------------")
    report.append(f"最终结果: {pass_count} / {len(TEST_POINTS)} 项通过")
    report.append(f"通过率: {pass_count/len(TEST_POINTS)*100:.2f}%")
    report.append("=======================================================")

    final_report = "\n".join(report)
    print(final_report)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_report)

if __name__ == "__main__":
    try:
        run_and_report()
    except Exception as e:
        print(f"[致命错误] 自动化流水线执行失败: {e}")