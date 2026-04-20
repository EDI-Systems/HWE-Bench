import os
import json
from openai import OpenAI

# ---------- 1. 初始化 LLM ----------
api_key = os.getenv("ZHIZENGZENG_API_KEY")
if not api_key:
    raise ValueError("❌ 环境变量 ZHIZENGZENG_API_KEY 未设置。")
client = OpenAI(api_key=api_key, base_url="https://api.zhizengzeng.com/v1")

# ---------- 2. 核心生成逻辑 (功能意图 + 数据驱动) ----------
def generate_netlist_with_prompt(components, function_desc):
    """
    系统提示词强化了对 'Target Function' 的服从性，
    要求模型必须根据功能描述推理出正确的电路拓扑。
    """
    system_prompt = (
        "You are an Expert Electronic Hardware Engineer. Your task is to generate a complete "
        "Netlist topology based on the provided Component JSONs and the specified Target Function.\n\n"
        
        "【Core Directives】\n"
        "1. Functional Compliance: Your design MUST strictly fulfill the 'Target Function' constraints. "
        "Analyze the pins of the core ICs to ensure the topology (e.g., Buck, Boost, LDO) matches the functional intent.\n"
        "2. Auto-Supplement Passives (CRITICAL): You MUST autonomously introduce essential passive components "
        "(Resistors, Capacitors, Inductors, Diodes) required for the core ICs to function correctly.\n"
        "   - Calculate or estimate reasonable passive values (e.g., for feedback dividers or RC filters) "
        "to satisfy the Target Function's voltage/current requirements.\n"
        "   - Create standard ComponentIDs: `<Type>_<Value>_<InstanceNumber>` (e.g., `R_10K_1`, `C_22uF_1`).\n"
        "   - Assume passives have pin names `1` and `2`.\n\n"
        
        "【Formatting Rules】\n"
        "1. Output Structure: Use exactly `<NetName>: ComponentID|PinName|FunctionName|,ComponentID|PinName|FunctionName|...`\n"
        "2. Net Naming Conventions: Use industry-standard names (e.g., `NET_VIN`, `NET_VOUT`, `NET_GND`).\n"
        "3. Output purity: Output ONLY the raw netlist string. NO markdown, NO code blocks, NO conversational text."
    )

    user_prompt_content = (
        "【Target Function / Module Description】\n"
        f"{function_desc}\n\n"

        "【Design Task】\n"
        "Generate the complete internal and external connection netlist for the circuit module based on the components below.\n\n"
        
        "【Available Component Library (JSON)】\n"
        f"{json.dumps(components, ensure_ascii=False, indent=2)}"
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt_content}
            ],
            temperature=0.1
        )
        result = response.choices[0].message.content.strip()
        # 清除可能存在的 Markdown 代码块标记
        if result.startswith("```"):
            result = "\n".join(line for line in result.splitlines() if not line.strip().startswith("```"))
        return result
    except Exception as e:
        print(f"❌ 调用 LLM 失败: {e}")
        return ""

# ---------- 3. 网表解析器 (将文本解析为 JSON 结构) ----------
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

# ---------- 4. 加载与执行逻辑 ----------
def load_selected_components(component_dir, json_filenames):
    components = []
    for filename in json_filenames:
        if not filename.endswith(".json"): filename += ".json"
        filepath = os.path.join(component_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                components.append(json.load(f))
    return components

def process_hwe_bench_module(project_path, target_json_files, function_desc, module_name="generated_module"):
    pdf_json_dir = os.path.join(project_path, "Datasheet", "Preprocessed", "pdf_json")
    output_base = os.path.join(project_path, "Result", "deepseek-v3")
    os.makedirs(output_base, exist_ok=True)

    components = load_selected_components(pdf_json_dir, target_json_files)
    if not components:
        print("❌ 错误：未成功加载组件库文件。")
        return

    print(f"🚀 正在基于功能描述生成网表: netlist_{module_name}.json ...")
    raw_text = generate_netlist_with_prompt(components, function_desc)
    
    if raw_text:
        # 解析并保存为 JSON
        netlist_json = parse_netlist_to_json(raw_text)
        json_path = os.path.join(output_base, f"netlist_{module_name}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(netlist_json, f, ensure_ascii=False, indent=2)
            
        print(f"✅ 处理完成！网表已保存至: {json_path}")

# ---------- 5. 主程序入口 ----------
if __name__ == "__main__":
    # 配置工程路径
    TARGET_PROJECT_DIR = r"D:\llm\Dataset\Consumer\E-Ink wireless display_OSHWLab"
    
    # 1. 核心元件
    TARGET_COMPONENTS = ["TPS62088.json"]
    
    # 2. 模块功能描述 (直接写在 Prompt 里)
    FUNCTION_DESC = (
        "Design a high-efficiency Step-Down (Buck) converter module using the TPS6208833 IC. "
        "The goal is to convert a single-cell Li-ion battery input (VBAT+) into a stable 3.3V DC output (VCC3_3).\n\n"
        "Requirements:\n"
        "1. Topology: Implement a synchronous buck converter structure. Place a suitable power inductor between the Switch (SW) node and the output net.\n"
        "2. Filtering: Supplement the necessary input and output decoupling capacitors to ensure stable operation and low output ripple based on standard application requirements.\n"
        "3. Feedback: This IC is a fixed 3.3V output version; the feedback (FB) path should be configured accordingly to maintain the 3.3V regulation.\n"
        "4. Control: The device should be enabled by default. Implement a logic-high enable circuit by connecting a pull-up resistor from the input supply to the EN pin.\n"
        "5. Grounding: All power and analog ground pins of the IC must be tied to a common system ground (NET_GND)."
    )
    
    # 执行生成
    process_hwe_bench_module(
        project_path=TARGET_PROJECT_DIR, 
        target_json_files=TARGET_COMPONENTS,
        function_desc=FUNCTION_DESC,
        module_name="battery_module"
    )