import os
import json
import re
from openai import OpenAI

# ---------- 1. Initialization ----------
api_key = os.getenv("")

client = OpenAI(api_key=api_key, base_url="")

# ---------- 2. File Reading Tools ----------
def read_json_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_all_components(component_dir):
    """Load all component JSON files in the library (pdf_json)"""
    components = []
    if not os.path.isdir(component_dir):
        print(f"Warning: Component directory not found: {component_dir}")
        return components
    for file in sorted(os.listdir(component_dir)):
        if file.endswith(".json"):
            try:
                with open(os.path.join(component_dir, file), "r", encoding="utf-8") as f:
                    components.append(json.load(f))
            except Exception as e:
                print(f"Error loading {file}: {e}")
    return components

def clean_netlist_text(text: str) -> str:
    """Clean output: remove Markdown fences and trailing commas"""
    if text.startswith("```"):
        text = "\n".join(line for line in text.splitlines() if not line.strip().startswith("```"))
    cleaned = [re.sub(r",\s*$", "", line) for line in text.splitlines()]
    return "\n".join(cleaned)

# ---------- 3. System Integration LLM Call ----------
def generate_system_netlist(module_info, module_netlist, components):
    """
    Generate global system netlist based on architecture, internal netlists, and component library
    """
    system_prompt = (
        "Task: Generate a unified SYSTEM-LEVEL NETLIST.\n\n"
        "Context Data:\n"
        "- 'functional_arch': Defines signals between modules.\n"
        "- 'internal_netlists': Existing pin connections inside each module.\n"
        "- 'component_library': The absolute truth for valid component pins.\n\n"
        "Execution Rules:\n"
        "1. Route Signals: Connect modules based on 'functional_arch'. Find pins from 'internal_netlists' and verify them against 'component_library'.\n"
        "2. Global Power: Merge common power/ground networks into global nets.\n"
        "3. PIN ACCURACY: The PinName and FunctionName MUST EXACTLY match the library. DO NOT invent pins.\n"
        "4. RESOURCE EXCLUSIVITY: A physical pin can only be assigned to ONE net.\n"
        "5. PROTOCOL INTEGRITY: Interface signals must be complete and paired.\n"
        "6. Continuity: Use sequential net IDs (net1, net2...).\n\n"
        "Strict Output Format:\n"
        "netX: ComponentID|PinName|FunctionName|,ComponentID|PinName|FunctionName|,.....\n"
        "- STRICTLY pure text only.\n"
        "- NO markdown fences.\n"
        "- NO explanations, NO headers, NO blank lines."
    )

    user_payload = {
        "functional_arch": module_info,
        "internal_netlists": module_netlist,
        "component_library": components
    }

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"API Error: {e}")
        return ""

# ---------- 4. Netlist Parser ----------
def parse_netlist_to_json(netlist_text: str):
    result = {"System_Netlist": []}
    for raw in netlist_text.splitlines():
        line = raw.strip()
        if not line: continue
        m = re.match(r"^(net\d+):\s*(.*)$", line)
        if not m: continue
        
        net_name, conns_str = m.group(1), m.group(2)
        connections = []
        for conn in conns_str.split(","):
            parts = [p.strip() for p in conn.split("|") if p.strip()]
            if len(parts) >= 3:
                connections.append({
                    "ComponentID": parts[0], "PinName": parts[1], "FunctionName": parts[2]
                })
        result["System_Netlist"].append({"net_id": net_name, "Connections": connections})
    return result

# ---------- 5. Main Program ----------
def main_system_integration(project_path):
    output_dir = os.path.join(project_path, "output", "result", "deepseek-v3")
    comp_dir = os.path.join(project_path, "output", "pdf", "pdf_json")
    
    info_path = os.path.join(output_dir, "1module_info.json")
    netlist_path = os.path.join(output_dir, "3module_netlist.json")
    
    final_txt = os.path.join(output_dir, "4system_netlist.txt")
    final_json = os.path.join(output_dir, "4system_netlist.json")

    if not all(os.path.exists(p) for p in [info_path, netlist_path, comp_dir]):
        print(f"Error: Missing input files in {project_path}")
        return

    print(f"Loading data for: {os.path.basename(project_path)}")
    module_info = read_json_file(info_path)
    module_netlist = read_json_file(netlist_path)
    components = load_all_components(comp_dir)

    print("LLM is integrating system-level connections with library reference...")
    raw_netlist = generate_system_netlist(module_info, module_netlist, components)

    if not raw_netlist:
        print("Error: Failed to generate netlist.")
        return

    cleaned_txt = clean_netlist_text(raw_netlist)
    system_json = parse_netlist_to_json(cleaned_txt)

    os.makedirs(output_dir, exist_ok=True)
    with open(final_txt, "w", encoding="utf-8") as f: f.write(cleaned_txt)
    with open(final_json, "w", encoding="utf-8") as f: json.dump(system_json, f, indent=2, ensure_ascii=False)

    print(f"Success! System netlist saved to {output_dir}")

if __name__ == "__main__":
    TARGET_PATH = r"D:\llm\Bathroom Fan"
    
    if os.path.exists(TARGET_PATH):
        main_system_integration(TARGET_PATH)
    else:
        print(f"Error: Path not found: {TARGET_PATH}")
