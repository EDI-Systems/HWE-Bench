import os
import subprocess
import re
import json
from datetime import datetime

LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON_FILE = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "module_step3.json")
JSON_FILE = os.path.join(BASE_DIR, "..", "Correct", "dynamic_Multiplexer.json")
CIR_FILE = os.path.join(BASE_DIR, "ppmux_sim.net")
LOG_FILE = os.path.join(BASE_DIR, "ppmux_sim.log")

# ================= 2. 判定指标与阈值配置 =================
# 定义测试项目、对应的 log 变量名、期望范围及单位
TEST_CRITERIA = {
    # --- 阶段 A: 纯电池供电 (0ms - 10ms) ---
    "v_out_stage_a":   {"name": "初始电池供电电压", "min": 3.5, "max": 3.8, "unit": "V"},
    
    # --- 阶段 B: USB 插入瞬态 (10ms 附近) ---
    "v_dip_plug":      {"name": "插入瞬态最小电压", "min": 3.2, "max": 5.5, "unit": "V"},
    "i_peak_usb":      {"name": "USB 插入冲击电流", "min": -1.0, "max": 0.5, "unit": "A"}, # 浪涌电流检测
    
    # --- 阶段 C: USB 稳态 (15ms - 25ms) ---
    "v_out_stage_c":   {"name": "USB 稳态输出电压", "min": 4.3, "max": 5.0, "unit": "V"},
    "v_drop_d9":       {"name": "二极管正向压降",   "min": 0.1, "max": 0.6, "unit": "V"},
    "i_leak_bat":      {"name": "电池端倒灌电流",   "min": -1e-6, "max": 1e-9, "unit": "A"},
    
    # --- 阶段 D: USB 拔出瞬态 (30ms 附近) ---
    "v_dip_unplug":    {"name": "拔出瞬态跌落电压", "min": 2.8, "max": 4.0, "unit": "V"},
    
    # --- 阶段 E: 恢复电池供电 (40ms - 50ms) ---
    "v_out_stage_e":   {"name": "切回电池后电压",   "min": 3.5, "max": 3.8, "unit": "V"}
}

def build_ppmux_netlist():
    """从 JSON 提取拓扑并增加更多测量点"""
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"找不到文件: {JSON_FILE}")
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    ppmux_module = data.get("Power Path Multiplexer (PPMUX)", [])
    
    pins = {}
    for net in ppmux_module:
        net_id = net["net_id"]
        for conn in net["Connections"]:
            key = f"{conn['ComponentID']}:{conn['PinName']}"
            pins[key] = net_id

    # 节点提取
    net_usb = pins.get("USB:A9", "VBUS_NET")
    net_bat = pins.get("TP4057ST26P:3", "BAT_NET")
    net_out = pins.get("IRLM:2", "OUT_NET")
    net_gnd_raw = pins.get("USB:A12", "GND_NET")

    def n(node_name):
        return "0" if node_name == net_gnd_raw else node_name

    # 映射关键引脚用于测量
    mos_g = pins.get("IRLM:1", net_usb)  

    netlist = [
        "* Updated PPMUX Auto-Simulation with Advanced Metrics",
        ".model D_SCHOTTKY D(Is=1e-5 Rs=0.05 N=1)",
        ".model P_MOS VDMOS(pchan Vto=-1.5 Rs=0.05)",
        ".tran 0 50m 0 100u",
        
        # 电源激励：10ms 插入 USB，30ms 拔出
        f"V_BAT {n(net_bat)} 0 3.7",
        f"V_USB {n(net_usb)} 0 PULSE(0 5 10m 1ms 1ms 20m 50m)",
        
        # 拓扑元件
        f"D9 {n(net_usb)} {n(net_out)} D_SCHOTTKY",
        f"M1 {n(net_out)} {n(mos_g)} {n(net_bat)} {n(net_bat)} P_MOS",
        f"R_LOAD {n(net_out)} 0 100",
        
        # --- 增强测量点 ---
        # 1. 稳态电压测量
        f".meas TRAN v_out_bat_only AVG V({n(net_out)}) FROM 5m TO 9m",
        f".meas TRAN v_out_usb_on AVG V({n(net_out)}) FROM 15m TO 25m",
        # 2. 漏电流测量 (USB 开启时 V_BAT 的电流)
        f".meas TRAN i_bat_leak AVG I(V_BAT) FROM 15m TO 25m",
        # 3. 压降测量 (USB 供电时二极管压降)
        f".meas TRAN v_drop_d9 AVG (V({n(net_usb)})-V({n(net_out)})) FROM 15m TO 25m",
        # 4. 切换瞬态测量 (找 10ms 左右切换过程中的最低电压点)
        f".meas TRAN v_out_dip MIN V({n(net_out)}) FROM 8m TO 12m",
        
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    # 1. 生成网表
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(build_ppmux_netlist())
    
    print(">>> 网表生成完毕，启动 LTspice 仿真...")
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE):
        print("[错误] 未生成日志文件。")
        return
        
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()
        
    # 2. 解析与验证
    print("\n" + "="*70)
    print(f"{'测试项目':<20} | {'实测值':<12} | {'标准范围':<18} | {'结果'}")
    print("-" * 70)
    
    passed_count = 0
    total_count = len(TEST_CRITERIA)
    
    for key, spec in TEST_CRITERIA.items():
        # 正则匹配测量值
        match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log_content, re.I)
        
        if match:
            val = float(match.group(1))
            # 判定逻辑
            is_ok = spec["min"] <= val <= spec["max"]
            status = "✅ PASS" if is_ok else "❌ FAIL"
            if is_ok: passed_count += 1
            
            val_str = f"{val:.4f} {spec['unit']}"
            range_str = f"{spec['min']}~{spec['max']} {spec['unit']}"
            print(f"{spec['name']:<16} | {val_str:<12} | {range_str:<18} | {status}")
        else:
            print(f"{spec['name']:<16} | {'N/A':<12} | {'ERROR':<18} | ❌ MISSING")

    # 3. 输出统计结果
    pass_rate = (passed_count / total_count) * 100
    print("-" * 70)
    print(f"统计结果: 总计 {total_count} 项 | 通过 {passed_count} 项 | 失败 {total_count - passed_count} 项")
    print(f"📊 最终通过率 (Pass Rate): {pass_rate:.2f}%")
    print("="*70)

if __name__ == "__main__":
    try:
        run_simulation()
    except Exception as e:
        print(f"脚本执行失败: {e}")