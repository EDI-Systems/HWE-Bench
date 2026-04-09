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

EST_CRITERIA = {
    # 待机阶段 (Gate=5V, PMOS OFF)
    "v_motor_off":  {"name": "01_关断时电机电压", "min": -0.1, "max": 0.1,  "unit": "V"},
    "i_leak_off":   {"name": "02_关断态漏电流",   "min": -1e-6,"max": 1e-6, "unit": "A"},
    
    # 导通阶段 (Gate=0V, PMOS ON)
    "v_motor_on":   {"name": "03_导通时电机电压", "min": 4.5,  "max": 5.0,  "unit": "V"},
    "i_motor_run":  {"name": "04_电机稳态电流",   "min": 0.8,  "max": 1.2,  "unit": "A"},
    "v_drop_pmos":  {"name": "05_PMOS导通压降",   "min": 0.0,  "max": 0.5,  "unit": "V"},
    
    # 瞬态阶段
    "t_switch_on":  {"name": "06_直接启动响应",   "min": 0.0,  "max": 1e-3, "unit": "s"}, # 无RC缓冲，响应极快
    "v_spike_neg":  {"name": "07_关断负压尖峰",   "min": -50.0,"max": 0.0,  "unit": "V"}  # 无续流二极管，Drain会被电感拉到负压
}

def build_pmos_netlist():
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"找不到 JSON 文件: {JSON_FILE}")

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. 提取映射
    pins = {}
    for net in data.get("Motor Load Switch & Inrush Buffer", []):
        for conn in net["Connections"]:
            pins[f"{conn['ComponentID']}:{conn['PinName']}"] = net["net_id"]

    # 2. 严格绑定 JSON 中的元件引脚
    n_pwr  = pins.get("Arduino:TOP_4", "NC_PWR")
    n_gnd  = pins.get("Arduino:TOP_5", "NC_GND")
    n_ctrl = pins.get("Arduino:LEFT_10", "NC_CTRL")
    
    # PMOS IRLM
    m_g = pins.get("IRLM:1", "NC_MG")
    m_d = pins.get("IRLM:2", "NC_MD")
    m_s = pins.get("IRLM:3", "NC_MS")
    
    # 电机 ES9251II
    mot_vcc = pins.get("ES9251II:2", "NC_MOT_V")
    mot_gnd = pins.get("ES9251II:3", "NC_MOT_G")

    def n(name): return "0" if name in [n_gnd, mot_gnd] else name

    # 3. 构建高边 PMOS 网表
    netlist = [
        "* PMOS High-Side Motor Switch Strict Validation",
        ".model P_MOS VDMOS(pchan Vto=-1.5 Rs=0.05 Kp=5.0)", 
        ".tran 0 50m 0 1u", 
        
        # --- 电源 ---
        f"V_BAT {n(n_pwr)} 0 5",
        
        # --- PMOS 逻辑控制 ---
        # 初始5V(关断)，10ms拉低到0V(导通)，30ms恢复5V(关断)
        f"V_CTRL {n(n_ctrl)} 0 PULSE(5 0 10m 1u 1u 20m 50m)",
        
        # --- JSON 映射的物理器件 ---
        # M<name> Nd Ng Ns Nb <model> 
        f"M1 {n(m_d)} {n(m_g)} {n(m_s)} {n(m_s)} P_MOS",
        
        # 补全电机的内部等效模型 (连接到 ES9251II 的引脚上)
        f"R_MOTOR {n(mot_vcc)} N_MID 5",
        f"L_MOTOR N_MID {n(mot_gnd)} 1mH",
        
        # --- 测量指令 ---
        f".meas TRAN v_motor_off AVG V({n(mot_vcc)}) FROM 2m TO 8m",
        f".meas TRAN i_leak_off AVG I(V_BAT) FROM 2m TO 8m",
        
        f".meas TRAN v_motor_on AVG V({n(mot_vcc)}) FROM 20m TO 28m",
        f".meas TRAN i_motor_run AVG I(L_MOTOR) FROM 20m TO 28m",
        f".meas TRAN v_drop_pmos AVG (V({n(n_pwr)})-V({n(m_d)})) FROM 20m TO 28m",
        
        # 测量下降沿启动速度
        f".meas TRAN t_switch_on TRIG V({n(n_ctrl)}) VAL=2.5 FALL=1 TARG V({n(mot_vcc)}) VAL=4.5 RISE=1",
        
        # 测量电感关断瞬间拉出的负压尖峰 (验证纯 PMOS 的物理特性)
        f".meas TRAN v_spike_neg MIN V({n(mot_vcc)}) FROM 29m TO 35m",
        ".end"
    ]
    return "\n".join(netlist)

def run_simulation():
    content = build_pmos_netlist()
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], check=True)
    
    if not os.path.exists(LOG_FILE): return
    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        log_raw = f.read()

    print("\n" + "="*85)
    print(f" PMOS 高边电机驱动验证报告 | 纯净拓扑验证")
    print("="*85)
    print(f"{'测试项':<18} | {'实测值':<15} | {'判定标准':<15} | {'状态'}")
    print("-" * 85)

    pass_count = 0
    for key, spec in TEST_CRITERIA.items():
        match = re.search(rf"{key}.*?[:=]\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", log_raw, re.I)
        val = float(match.group(1)) if match else None
        
        if val is not None:
            is_ok = spec["min"] <= val <= spec["max"]
            status = "✅ PASS" if is_ok else "❌ FAIL"
            if is_ok: pass_count += 1
            
            # 时间格式优化
            if spec['unit'] == 's' and val < 0.1:
                val_str = f"{val*1000:>10.4f} ms"
            else:
                val_str = f"{val:>11.4f} {spec['unit']}"
        else:
            status = "⚠️ MISSING"
            val_str = "N/A"
            
        print(f"{spec['name']:<18} | {val_str:<15} | {spec['min']}~{spec['max']:<10} | {status}")

    print("-" * 85)
    print(f"📊 模块最终通过率 (Pass Rate): {(pass_count / len(TEST_CRITERIA)) * 100:.2f}%")
    print("="*85)

if __name__ == "__main__":
    run_simulation()