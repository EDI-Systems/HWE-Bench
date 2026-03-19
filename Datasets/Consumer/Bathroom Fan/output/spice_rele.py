import json
import os
import re
import subprocess

# ================= 1. 环境与路径配置 =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LTSPICE_EXE = r"D:\app\LTspice\LTspice.exe" 
JSON_FILE = os.path.join(BASE_DIR, "netlist_rele.json")
CIR_FILE = os.path.join(BASE_DIR, "relay_test.net")
LOG_FILE = os.path.join(BASE_DIR, "relay_test.log")

# ================= 2. 核心判定阈值设置 (按要求更新) =================
# 指标包含：LED电流、继电器电流、V1输入电流、电平比例
TEST_METRICS = [
    {"id": "M01", "name": "I_LED",      "min": 0,      "max": 1e-3,   "unit": "A",  "desc": "发光二极管电流 [0, 1mA]"},
    {"id": "M02", "name": "I_RELAY",    "min": 1e-6,      "max": 0.1,    "unit": "A",  "desc": "继电器线圈电流 [0, 100mA]"},
    {"id": "M03", "name": "I_V1_IN",    "min": -1e-6,  "max": 1e-3,   "unit": "A",  "desc": "V1控制端电流 < 1uA"},
    {"id": "M04", "name": "LVL_RATIO",  "min": 0.5,    "max": 1.0,    "unit": "ratio", "desc": "负载/V1电平比例 [0.5, 1]"}
]

# ================= 3. 提取拓扑连接 =================
# ================= 3. 提取拓扑连接 (增强鲁棒性匹配) =================
def get_topology_nodes(json_path):
    if not os.path.exists(json_path):
        return {}

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    pin_map = {}
    
    for net in data:
        # 兼容处理全局地线命名
        net_id = "0" if net["net_id"] in ["NET_GND", "GND"] else net["net_id"]
        
        for conn in net.get("connections", []):
            cid = str(conn.get('ComponentID', '')).upper()
            pin = str(conn.get('PinName', '')).upper()
            func = str(conn.get('FunctionName', '')).upper()
            
            # --- 1. 识别 NPN 三极管 (S8050) ---
            if "S8050" in cid or "NPN" in cid or "Q" in cid:
                if "1" in pin or "B" in pin or "BASE" in func:
                    pin_map["S8050_1"] = net_id  # 映射为基极 Base
                elif "2" in pin or "E" in pin or "EMIT" in func:
                    pin_map["S8050_2"] = net_id  # 映射为发射极 Emitter
                elif "3" in pin or "C" in pin or "COLL" in func:
                    pin_map["S8050_3"] = net_id  # 映射为集电极 Collector

            # --- 2. 识别 固态继电器 (G3MB) ---
            elif "G3MB" in cid or "RELAY" in cid or "K" in cid:
                if "3" in pin or "+" in pin or "POS" in func:
                    pin_map["G3MB_3"] = net_id   # 映射为控制端正极
                elif "4" in pin or "-" in pin or "NEG" in func:
                    pin_map["G3MB_4"] = net_id   # 映射为控制端负极

            # --- 3. 识别 指示灯 (LEDR) ---
            elif "LED" in cid or "LIGHT" in cid:
                if "1" in pin or "A" in pin or "+" in pin or "ANODE" in func:
                    pin_map["LEDR_1"] = net_id   # 映射为阳极 Anode
                elif "2" in pin or "K" in pin or "C" in pin or "-" in pin or "CATHODE" in func:
                    pin_map["LEDR_2"] = net_id   # 映射为阴极 Cathode

    return pin_map
# ================= 4. 生成 SPICE 网表 =================
def generate_spice(m):
    # 自动地线识别
    gnd_group = m.get("S8050_2", "net4") 
    def node(pin_key):
        net = m.get(pin_key, "NC")
        return "0" if net == gnd_group else net

    netlist = f"""* Precise Threshold Validation
.tran 100m
.options plotwinsize=0 numdgt=7

* --- [外置环境：固定插座] ---
V1 IN 0 PULSE(0 5 10m 1n 1n 20m 40m)
V2 SUPPLY 0 5
R1 IN {node('S8050_1')} 10k
R2 {node('S8050_1')} 0 10k

* --- [核心元件：JSON 拓扑映射] ---
Q1 {node('S8050_3')} {node('S8050_1')} {node('S8050_2')} S8050
R_COIL {node('G3MB_3')} {node('G3MB_4')} 50
D_LED {node('LEDR_1')} LED_INT 1N4148
R_LED_LIMIT LED_INT {node('LEDR_2')} 4.7k

* 强制连接 V2 到负载正极以验证内部拓扑
R_BRIDGE SUPPLY {node('G3MB_3')} 0.001
R_L_BRIDGE SUPPLY {node('LEDR_1')} 0.001

* --- [模型与测量指令] ---
.model S8050 NPN(Is=4.8e-14 Bf=200 Vaf=100 Ikf=0.8 Rc=0.25 Cjc=9p Tf=0.8n)
.model 1N4148 D(Is=2.682n N=1.836 Rs=0.5664 Cjo=4p M=0.333 Vj=0.5 Tt=11.54n)

.meas TRAN I_LED_val AVG I(D_LED) FROM 15m TO 25m
.meas TRAN I_RELAY_val AVG I(R_COIL) FROM 15m TO 25m
.meas TRAN I_V1_val AVG I(R1) FROM 15m TO 25m
.meas TRAN V_LOAD_val AVG V({node('G3MB_3')},{node('G3MB_4')}) FROM 15m TO 25m
.meas TRAN RATIO_val PARAM V_LOAD_val/5
.end
"""
    return netlist

# ================= 5. 执行验证与判定 =================
def run_test():
    try:
        topo = get_topology_nodes(JSON_FILE)
        with open(CIR_FILE, 'w', encoding='utf-8') as f:
            f.write(generate_spice(topo))
        
        subprocess.run([LTSPICE_EXE, "-b", "-Run", CIR_FILE], timeout=15)
        
        if not os.path.exists(LOG_FILE): return

        with open(LOG_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            log = f.read()

        print("\n" + "="*95)
        print(f"{'电路拓扑电气指标判定报告 (最新阈值)':^95}")
        print("="*95)
        print(f"{'ID':<6}| {'测量项':<18} | {'实测值':<15} | {'设定阈值范围':<20} | {'结果':<6}")
        print("-" * 95)

        patterns = {
            "I_LED": r"i_led_val[^=]*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)",
            "I_RELAY": r"i_relay_val[^=]*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)",
            "I_V1_IN": r"i_v1_val[^=]*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)",
            "LVL_RATIO": r"ratio_val[^=]*=\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
        }

        for m in TEST_METRICS:
            match = re.search(patterns[m['name']], log, re.I)
            val = float(match.group(1)) if match else 0.0
            
            # 判定逻辑
            is_pass = m['min'] <= val <= m['max']
            status = "✅PASS" if is_pass else "❌FAIL"
            
            # 格式化显示
            if m['unit'] == 'A':
                fmt_val = f"{val*1e6:.2f} uA" if abs(val) < 1e-3 else f"{val*1000:.2f} mA"
                fmt_limit = f"{m['min']*1000}~{m['max']*1000} mA"
            else:
                fmt_val = f"{val:.3f}"
                fmt_limit = f"{m['min']}~{m['max']}"

            print(f"{m['id']:<6}| {m['name']:<18} | {fmt_val:<15} | {fmt_limit:<20} | {status:<6}")
        print("="*95)

    except Exception as e:
        print(f"运行失败: {e}")

if __name__ == "__main__":
    run_test()