import os
import subprocess
import re
import json

# ================= 1. 环境与路径配置 =================
LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CIR_FILE = os.path.join(BASE_DIR, "soft_latch_auto.net")
LOG_FILE = os.path.join(BASE_DIR, "soft_latch_auto.log")
JSON_FILE = os.path.join(BASE_DIR, "netlist_switcher.json")

# ================= 2. 25项全生命周期检测点配置 =================
TEST_POINTS_CONFIG = [
    # --- 阶段 1: 0~10ms 上电待机 (零功耗) ---
    {"id": "TP01", "name": "S1_VOUT",   "min": -0.1,   "max": 0.1,   "unit": "V", "desc": "待机: 主电源(NET_VOUT)必须为0V"},
    {"id": "TP02", "name": "S1_DET",    "min": -0.1,   "max": 0.1,   "unit": "V", "desc": "待机: 检测脚(NET_DET)应为0V"},
    {"id": "TP03", "name": "S1_UPV",    "min": -0.1,   "max": 0.1,   "unit": "V", "desc": "待机: 单片机控制(NET_UPV)应为0V"},
    {"id": "TP04", "name": "S1_PGATE",  "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "待机: PMOS栅极被上拉锁定至5V(关断)"},
    {"id": "TP05", "name": "S1_ILOAD",  "min": -1e-6,  "max": 1e-6,  "unit": "A", "desc": "待机: 负载电流必须为0A (零功耗确认)"},

    # --- 阶段 2: 10~20ms 首次按键 (硬件开机响应) ---
    {"id": "TP06", "name": "S2_VOUT",   "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "按键: 主电源被瞬间开启至5V"},
    {"id": "TP07", "name": "S2_DET",    "min": 0.4,    "max": 0.9,   "unit": "V", "desc": "按键: 检测脚被按键经二极管拉低(~0.7V)"},
    {"id": "TP08", "name": "S2_UPV",    "min": -0.1,   "max": 0.1,   "unit": "V", "desc": "按键: 单片机还在启动中,维持0V"},
    {"id": "TP09", "name": "S2_PGATE",  "min": 0.4,    "max": 0.9,   "unit": "V", "desc": "按键: PMOS栅极被拉低(~0.7V导通)"},
    {"id": "TP10", "name": "S2_ILOAD",  "min": 4.5e-3, "max": 5.5e-3,"unit": "A", "desc": "按键: 负载出现约5mA正常工作电流"},

    # --- 阶段 3: 30~60ms 开机自锁 (MCU接管电源) ---
    {"id": "TP11", "name": "S3_VOUT",   "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "自锁: 松手后,主电源稳如泰山维持5V"},
    {"id": "TP12", "name": "S3_DET",    "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "自锁: 按键已松开,检测脚被上拉回5V"},
    {"id": "TP13", "name": "S3_UPV",    "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "自锁: 单片机输出高电平5V接管控制"},
    {"id": "TP14", "name": "S3_PGATE",  "min": -0.1,   "max": 0.2,   "unit": "V", "desc": "自锁: PMOS栅极被NMOS死死拉到绝对0V"},
    {"id": "TP15", "name": "S3_ILOAD",  "min": 4.5e-3, "max": 5.5e-3,"unit": "A", "desc": "自锁: 负载正常供电约5mA"},

    # --- 阶段 4: 70~90ms 二次按键检测 (防反串与信号复用) ---
    {"id": "TP16", "name": "S4_VOUT",   "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "检测: 二次按键时,主电源毫无波动维持5V"},
    {"id": "TP17", "name": "S4_DET",    "min": 0.4,    "max": 0.9,   "unit": "V", "desc": "检测: 检测脚完美掉入低电平坑(~0.7V)"},
    {"id": "TP18", "name": "S4_UPV",    "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "检测: 单片机维持输出5V"},
    {"id": "TP19", "name": "S4_PGATE",  "min": -0.1,   "max": 0.2,   "unit": "V", "desc": "检测: NMOS继续将PMOS栅极焊死在0V"},
    {"id": "TP20", "name": "S4_ILOAD",  "min": 4.5e-3, "max": 5.5e-3,"unit": "A", "desc": "检测: 负载电流不受按键干扰"},

    # --- 阶段 5: 125~150ms 彻底软关机 (放手掉电) ---
    {"id": "TP21", "name": "S5_VOUT",   "min": -0.1,   "max": 0.2,   "unit": "V", "desc": "关机: 主电源被彻底切断回0V"},
    {"id": "TP22", "name": "S5_DET",    "min": -0.1,   "max": 0.2,   "unit": "V", "desc": "关机: 检测脚随主电源一同掉电至0V"},
    {"id": "TP23", "name": "S5_UPV",    "min": -0.1,   "max": 0.2,   "unit": "V", "desc": "关机: 单片机输出拉低释放控制权"},
    {"id": "TP24", "name": "S5_PGATE",  "min": 4.8,    "max": 5.2,   "unit": "V", "desc": "关机: NMOS断开,PMOS栅极被上拉回5V"},
    {"id": "TP25", "name": "S5_ILOAD",  "min": -1e-6,  "max": 1e-6,  "unit": "A", "desc": "关机: 负载电流回归完美的0A"}
]

# ================= 3. 核心：纯拓扑解析引擎 =================
def extract_topology_to_spice():
    if not os.path.exists(JSON_FILE):
        return "", "NC"

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 提取结构：元件类型 -> {引脚特征 -> 绑定的网络名}
    pmos_pins, nmos_pins = {}, {}
    diode_anodes, diode_cathodes = [], []

    for net in data:
        # 将我们规范的 NET_GND 映射为 SPICE 的全局地 "0"
        net_name = "0" if net["net_id"] == "NET_GND" else net["net_id"]
        
        for conn in net.get("connections", []):
            cid = str(conn["ComponentID"]).upper()
            pin = str(conn["PinName"]).upper()
            
            # 分配至对应元件组 (做模糊匹配以增强鲁棒性)
            if "IRL" in cid or "PMOS" in cid:
                pmos_pins[pin] = net_name
            elif "2N7002" in cid or "NMOS" in cid:
                nmos_pins[pin] = net_name
            elif "1N4007" in cid or "DIODE" in cid:
                if pin == "1" or "ANODE" in str(conn.get("FunctionName", "")).upper():
                    diode_anodes.append(net_name)
                elif pin == "2" or "CATHODE" in str(conn.get("FunctionName", "")).upper():
                    diode_cathodes.append(net_name)

    spice_lines = []


    def find_pin(pins_dict, *keywords):
        for key, val in pins_dict.items():
            for kw in keywords:
                if kw in key: return val
        return 'NC'
    # 组装 PMOS (D G S B)
    p_d = find_pin(pmos_pins, 'D', 'DRAIN', '3')
    p_g = find_pin(pmos_pins, 'G', 'GATE', '1')
    p_s = find_pin(pmos_pins, 'S', 'SOURCE', '2')
    spice_lines.append(f"M1 {p_d} {p_g} {p_s} {p_s} IRLML6402")

    # 组装 NMOS (D G S B)
    n_d = find_pin(nmos_pins, 'D', 'DRAIN', '2')
    n_g = find_pin(nmos_pins, 'G', 'GATE', '1')
    n_s = find_pin(nmos_pins, 'S', 'SOURCE', '3')
    spice_lines.append(f"M2 {n_d} {n_g} {n_s} {n_s} 2N7002")

    # 组装 二极管
    diode_count = max(len(diode_anodes), len(diode_cathodes))
    for i in range(diode_count):
        a = diode_anodes[i] if i < len(diode_anodes) else "NC"
        c = diode_cathodes[i] if i < len(diode_cathodes) else "NC"
        spice_lines.append(f"D{i+1} {a} {c} 1N4148")

    return "\n".join(spice_lines), p_g  # 返回内部拓扑，并提取 PMOS 栅极节点供测点使用

def generate_spice_netlist():
    dynamic_topology, pmos_gate_node = extract_topology_to_spice()

    netlist = f"""* Pure Topology Mapping Benchmark
.tran 150m startup
.options plotwinsize=0 numdgt=7

* --- [外置测试底板与激励源] ---
* (这些对应你在 Prompt 提供的 NET_xxx 接口)
V1 NET_VIN 0 5
V2 UPV_CTRL 0 PULSE(0 5 15m 1n 1n 110m)
V3 N_V3 0 PULSE(0 5 10m 1n 1n 20m 60m 2)

S1 UPV_CTRL NET_UPV UPV_CTRL 0 SW_MCU
S2 NET_BTN 0 N_V3 0 MY_BTN

* 固定的外置电阻 (绑定至外部接口)
R4 NET_VOUT 0 1K          ; 主负载
R2 NET_VOUT NET_DET 10K   ; 按键检测上拉
R3 NET_UPV 0 100K         ; MCU 下拉
R1 NET_VIN {pmos_gate_node} 100K  ; PMOS 栅极被动上拉 (节点由大模型拓扑动态决定)

* --- [LLM 生成的核心拓扑覆盖] ---
{dynamic_topology}
* ----------------------------------

* --- [模型定义] ---
.model MY_BTN SW(Vt=2.5 Ron=0.1 Roff=10Meg)
.model SW_MCU SW(Vt=2.5 Ron=0.1 Roff=10Meg)
.model 1N4148 D(Is=2.52n Rs=.568 N=1.752 Cjo=4p M=.4 tt=20n)
.model IRLML6402 VDMOS(pchan Rg=5 Vto=-0.85 Rd=0.035 Rs=0.015 Rb=0.02 Kp=15)
.model 2N7002 VDMOS(Rg=100 Vto=2.1 Rd=2 Rs=0.5 Kp=0.4)

* --- [25 项动态测量点] ---
* (Stage 1: 2m~8m)
.meas TRAN TP01_val AVG V(NET_VOUT) FROM 2m TO 8m
.meas TRAN TP02_val AVG V(NET_DET) FROM 2m TO 8m
.meas TRAN TP03_val AVG V(NET_UPV) FROM 2m TO 8m
.meas TRAN TP04_val AVG V({pmos_gate_node}) FROM 2m TO 8m
.meas TRAN TP05_val AVG I(R4) FROM 2m TO 8m

* (Stage 2: 12m~14m)
.meas TRAN TP06_val AVG V(NET_VOUT) FROM 12m TO 14m
.meas TRAN TP07_val MIN V(NET_DET) FROM 12m TO 14m
.meas TRAN TP08_val AVG V(NET_UPV) FROM 12m TO 14m
.meas TRAN TP09_val MIN V({pmos_gate_node}) FROM 12m TO 14m
.meas TRAN TP10_val AVG I(R4) FROM 12m TO 14m

* (Stage 3: 40m~50m)
.meas TRAN TP11_val AVG V(NET_VOUT) FROM 40m TO 50m
.meas TRAN TP12_val AVG V(NET_DET) FROM 40m TO 50m
.meas TRAN TP13_val AVG V(NET_UPV) FROM 40m TO 50m
.meas TRAN TP14_val AVG V({pmos_gate_node}) FROM 40m TO 50m
.meas TRAN TP15_val AVG I(R4) FROM 40m TO 50m

* (Stage 4: 75m~85m)
.meas TRAN TP16_val AVG V(NET_VOUT) FROM 75m TO 85m
.meas TRAN TP17_val MIN V(NET_DET) FROM 75m TO 85m
.meas TRAN TP18_val AVG V(NET_UPV) FROM 75m TO 85m
.meas TRAN TP19_val AVG V({pmos_gate_node}) FROM 75m TO 85m
.meas TRAN TP20_val AVG I(R4) FROM 75m TO 85m

* (Stage 5: 135m~145m)
.meas TRAN TP21_val AVG V(NET_VOUT) FROM 135m TO 145m
.meas TRAN TP22_val AVG V(NET_DET) FROM 135m TO 145m
.meas TRAN TP23_val AVG V(NET_UPV) FROM 135m TO 145m
.meas TRAN TP24_val AVG V({pmos_gate_node}) FROM 135m TO 145m
.meas TRAN TP25_val AVG I(R4) FROM 135m TO 145m
.end
"""
    return netlist

# ================= 4. 运行验证 =================
def run_and_report():
    print("正在基于底层拓扑映射生成 SPICE 仿真环境...")
    with open(CIR_FILE, 'w', encoding='utf-8') as f:
        f.write(generate_spice_netlist())

    try:
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], timeout=15, check=True)
    except Exception as e:
        print(f"LTspice 执行失败，请检查路径: {e}")
        return

    with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    print("\n" + "=" * 115)
    print(f"{'纯拓扑映射驱动 - 25项自动化验证报告':^115}")
    print("=" * 115)
    print(f"{'ID':<6}| {'测点 (Node)':<12} | {'仿真值':<12} | {'合格区间':<18} | {'状态':<6} | {'时序描述'}")
    print("-" * 115)

    pass_cnt = 0
    for tp in TEST_POINTS_CONFIG:
        match = re.search(rf"{tp['id']}_val[^=]*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", content, re.I)
        val = float(match.group(1)) if match else 0.0
        
        status = "✅PASS" if tp['min'] <= val <= tp['max'] else "❌FAIL"
        if status == "✅PASS": pass_cnt += 1
        
        if tp['unit'] == 'A' and abs(val) > 1e-6:
            val_fmt, limit_fmt = f"{val*1000:.3f} mA", f"{tp['min']*1000}~{tp['max']*1000} mA"
        elif tp['unit'] == 'A' and abs(val) <= 1e-6:
            val_fmt, limit_fmt = "0.000 mA", "0.000 mA"
        else:
            val_fmt, limit_fmt = f"{val:.3f} {tp['unit']}", f"{tp['min']}~{tp['max']} {tp['unit']}"

        print(f"{tp['id']:<6}| {tp['name']:<12} | {val_fmt:<12} | {limit_fmt:<18} | {status:<6} | {tp['desc']}")

        if tp['id'] in ["TP05", "TP10", "TP15", "TP20"]:
            print("-" * 115)

    print("-" * 115)
    print(f"拓扑逻辑匹配度: {(pass_cnt / 25) * 100:.1f}%  [通过项: {pass_cnt}/25]")
    print("=" * 115)

if __name__ == "__main__":
    run_and_report()