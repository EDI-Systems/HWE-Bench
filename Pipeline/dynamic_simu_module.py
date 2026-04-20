import os
import json
from openai import OpenAI

# ---------- 1. 初始化 LLM ----------
# 请确保环境变量中已设置 API Key
api_key = os.getenv("ZHIZENGZENG_API_KEY")
if not api_key:
    raise ValueError("❌ 环境变量 ZHIZENGZENG_API_KEY 未设置。")
client = OpenAI(api_key=api_key, base_url="https://api.zhizengzeng.com/v1")

# ---------- 2. 核心生成逻辑 ----------
def generate_netlist_with_prompt(components, function_desc):
    """
    基于组件库和抽象功能描述，利用 LLM 的硬件推理能力生成网表。
    """
    system_prompt = (
    "You are an Expert Electronic Hardware Engineer. Your task is to generate a complete "
    "Netlist topology based on the provided Component JSONs and the specified Functional Principles.\n\n"
    
    "【Core Directives】\n"
    "1. Logic Inference: Analyze the pins of the ICs (e.g., Gate/Drain/Source for MOSFETs, Anode/Cathode for Diodes, "
    "Base/Collector/Emitter for BJTs). You must derive connections based on electronic design patterns "
    "(e.g., High-side switching, Pull-up/down logic, Diode isolation).\n"
    
    "2. Auto-Supplement Passives (CRITICAL): You MUST autonomously introduce essential passive components "
    "required for the circuit to function safely and stably.\n"
    "   - For MOSFETs: Include Gate pull-up/pull-down resistors (e.g., 100K) to prevent floating states.\n"
    "   - For BJTs: Always include base-current-limiting resistors.\n"
    "   - Create standard ComponentIDs: `<Type>_<Value>_<InstanceNumber>` (e.g., `R_100K_1`).\n"
    "   - Assume passives have pin names `1` and `2`.\n"
    
    "3. Multi-Instance Support: Instantiate separate entities for multiple identical components (e.g., Q1, Q2, D4, D5).\n\n"
    
    "【Formatting Rules】\n"
    "1. Output Structure: Use exactly `<NetName>: ComponentID|PinName|FunctionName|,ComponentID|PinName|FunctionName|...` \n"
    "2. Net Naming: Use semantic names (e.g., `NET_Q1_GATE`, `NET_PWR_LATCH`).\n"
    "3. Output purity: Output ONLY the raw netlist string. NO markdown, NO code blocks, NO conversational text."
)

    user_prompt_content = (
        "【Target Functional Principle】\n"
        f"{function_desc}\n\n"

        "【Available Component Library (JSON)】\n"
        f"{json.dumps(components, ensure_ascii=False, indent=2)}"
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat", # 或使用 deepseek-reasoner (v3/r1) 获得更强推理
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt_content}
            ],
            temperature=0.1
        )
        result = response.choices[0].message.content.strip()
        # 移除可能出现的 Markdown 标记
        if result.startswith("```"):
            result = "\n".join(line for line in result.splitlines() if not line.strip().startswith("```"))
        return result
    except Exception as e:
        print(f"❌ 调用 LLM 失败: {e}")
        return ""

# ---------- 3. 辅助函数 (解析与加载) ----------
def parse_netlist_to_json(netlist_text: str):
    netlist_data = []
    for line in netlist_text.strip().splitlines():
        if ":" not in line: continue
        net_part, conns_part = line.split(":", 1)
        connections = []
        for conn in conns_part.split(","):
            parts = conn.strip().split("|")
            if len(parts) >= 3:
                connections.append({
                    "ComponentID": parts[0].strip(),
                    "PinName": parts[1].strip(),
                    "FunctionName": parts[2].strip()
                })
        if connections:
            netlist_data.append({"net_id": net_part.strip(), "connections": connections})
    return netlist_data

def load_selected_components(component_dir, json_filenames):
    components = []
    for filename in json_filenames:
        if not filename.endswith(".json"): filename += ".json"
        filepath = os.path.join(component_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                components.append(json.load(f))
        else:
            print(f"⚠️ 警告: 找不到文件 {filepath}")
    return components

# ---------- 4. 主执行流程 ----------
def process_hwe_bench_task(project_path, target_json_files, function_desc, module_name):
    pdf_json_dir = os.path.join(project_path, "Datasheet", "Preprocessed", "pdf_json")
    output_base = os.path.join(project_path, "Result", "deepseek-v3")
    os.makedirs(output_base, exist_ok=True)

    components = load_selected_components(pdf_json_dir, target_json_files)
    if not components:
        print("❌ 错误：未成功加载任何组件库文件。")
        return

    print(f"🚀 正在基于原理描述设计电路: {module_name} ...")
    raw_netlist = generate_netlist_with_prompt(components, function_desc)
    
    if raw_netlist:
        netlist_json = parse_netlist_to_json(raw_netlist)
        json_path = os.path.join(output_base, f"netlist_{module_name}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(netlist_json, f, ensure_ascii=False, indent=2)
        print(f"✅ 生成成功！网表已保存至: {json_path}")
        print("-" * 30 + "\n" + raw_netlist + "\n" + "-" * 30)

# ---------- 5. 配置与运行 ----------
if __name__ == "__main__":
    # 配置你的本地工程路径
    TARGET_PROJECT_DIR = r"D:\llm\Dataset\Consumer\Bathroom_Fan_OSHWLab"
    
    # 定义核心组件 (不包含电阻，电阻将由 LLM 自动生成)
    TARGET_COMPONENTS = ["1N4007.json", "IRL.json", "2N7002.json", "Atmega.json"]
    
    # 纯原理描述 (不包含具体的脚对脚连线指令)
    ABSTRACT_FUNCTION_DESC = (
        "Design a Soft-Latching Power Switch circuit for a 5V system. "
        "The module allows a physical button to trigger power-on, and an MCU to maintain or cut off the power.\n\n"
        
        "【Functional Principle】\n"
        "The circuit controls the main power rail (U5V) derived from a +5V source. It remains at zero power "
        "consumption during standby. A momentary button press initiates the power, and the system "
        "self-latches using an MCU control signal (U_PV).\n\n"
        
        "【Logical Pattern: Soft-Latch Logic】\n"
        "1. High-Side Switching: Use a P-Channel MOSFET (Q1) as the primary power switch between +5V and U5V.\n"
        "2. Manual Trigger: A button signal (BUT_S) must be able to pull the gate of Q1 low through an isolation diode (D5) "
        "to temporarily turn on the system.\n"
        "3. Self-Latching Interface: Use an N-Channel MOSFET (Q2) to allow the MCU signal (U_PV) to lock the gate of Q1 "
        "to GND, maintaining power after the button is released.\n"
        "4. Button Sensing: Implement a feedback path (BUT_SE) through a diode (D4) so the MCU can detect button "
        "presses while the system is powered, without interfering with the power-on logic.\n\n"
        
        "【Design Requirements】\n"
        "- Biasing: Include 100K Ohm resistors: one for Q1 gate pull-up (to +5V) and one for Q2 gate pull-down (to GND).\n"
        "- Isolation: Use 1N4007WS diodes to prevent logic backflow between the button, the MCU, and the MOSFET gates.\n"
        "- Signal Mapping: +5V is the input source; U5V is the switched output; U_PV, BUT_S, and BUT_SE are the logic interfaces."
    )
    
    # 执行
    process_hwe_bench_task(
        project_path=TARGET_PROJECT_DIR, 
        target_json_files=TARGET_COMPONENTS,
        function_desc=ABSTRACT_FUNCTION_DESC,
        module_name="switcher_module"
    )