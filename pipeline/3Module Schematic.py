import os
import json
import re
from openai import OpenAI

# ---------- Init LLM ----------
api_key = os.getenv("")

client = OpenAI(api_key=api_key, base_url="")

# ---------- File reading ----------
def read_json_file(path):
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to parse JSON file {path}: {e}")

# ---------- Load component library ----------
def load_all_components(component_dir):
    components = []
    if not os.path.isdir(component_dir):
        print(f"Warning: Component directory not found: {component_dir}")
        return components

    for file in sorted(os.listdir(component_dir)):
        if file.endswith(".json"):
            try:
                with open(os.path.join(component_dir, file), "r", encoding="utf-8") as f:
                    comp = json.load(f)
                    components.append(comp)
            except Exception as e:
                print(f"Warning: Skipping component file {file} due to error: {e}")
    return components

def clean_netlist_text(text: str) -> str:
    """
    Clean netlist text:
    1. Standardize format to 'netX: '
    2. Logic cleaning: Discard nets with fewer than 2 pins.
    3. Output pure text.
    """
    cleaned = []
    for line in text.splitlines():
        line_stripped = line.strip()
        
        if not line_stripped:
            continue
            
        if "===" in line_stripped and "Module" in line_stripped:
            cleaned.append("\n" + line_stripped)
            continue
            
        m = re.match(r"^[-\*\s]*(net\d+)[-\*\s:]*(.*)$", line_stripped, re.IGNORECASE)
        
        if m:
            net_id = m.group(1).lower()
            conns_str = m.group(2)
            
            valid_conns = []
            for conn in conns_str.split(","):
                conn = conn.strip()
                if not conn:
                    continue
                
                parts = [p.strip() for p in conn.split("|") if p.strip() != ""]
                if len(parts) >= 3:
                    valid_conns.append(conn)
            
            if len(valid_conns) >= 2:
                standardized_line = f"{net_id}: " + ", ".join(valid_conns)
                cleaned.append(standardized_line)
                
    return "\n".join(cleaned).strip()

# ---------- LLM Call ----------
def generate_netlist(module_json, components):
    system_prompt = (
        "You are a professional embedded circuit design expert. "
        "Generate a complete, standardized electrical connection Netlist for the module based on the input module JSON and component library.\n"
        "[Requirements]\n"
        "1. Format: netX: ComponentID|PinName|FunctionName|,ComponentID|PinName|FunctionName|...\n"
        "2. No cross-module connections.\n"
        "3. PIN ACCURACY: The PinName and FunctionName MUST EXACTLY match the definitions in the provided component library.\n"
        "4. All recommended component pins must appear.\n"
        "5. Sequential net numbering (net1, net2, ...).\n"
        "6. RESOURCE EXCLUSIVITY: A physical pin can only be assigned to ONE net.\n"
        "7. PROTOCOL INTEGRITY: Interface signals must be complete and paired.\n"
        "8. Output pure text Netlist only, no markdown/comments.\n"
    )

    user_prompt = {
        "module": module_json,
        "component_library": components
    }

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(user_prompt, ensure_ascii=False)}
    ]

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.1,
            top_p=0.95
        )
        result = response.choices[0].message.content.strip()

        if result.startswith("```"):
            result = "\n".join(line for line in result.splitlines() if not line.strip().startswith("```"))

        return result

    except Exception as e:
        module_name = module_json.get('Module Name', 'Unknown')
        print(f"Error generating netlist for module {module_name}: {e}")
        return ""

# ---------- Netlist Parser ----------
def parse_netlist_to_json(netlist_text: str):
    result = {}
    current_module = None

    for raw in netlist_text.splitlines():
        line = raw.strip()
        if not line:
            continue

        if line.startswith("=== Module:") and line.endswith("==="):
            current_module = line.replace("=== Module:", "").replace("===", "").strip()
            result[current_module] = []
            continue

        m = re.match(r"^(net\d+):\s*(.*)$", line)
        if not m or not current_module:
            continue

        net_name = m.group(1)
        connections_str = m.group(2)
        connections = []

        for conn in connections_str.split(","):
            conn = conn.strip()
            if not conn:
                continue

            parts = [p.strip() for p in conn.split("|") if p.strip() != ""]
            if len(parts) >= 3:
                connections.append({
                    "ComponentID": parts[0],
                    "PinName": parts[1],
                    "FunctionName": parts[2],
                })

        result[current_module].append({
            "net_id": net_name,
            "Connections": connections
        })

    return result

# ---------- Main Logic ----------
def process_single_project_netlist(project_path):
    output_base = os.path.join(project_path, "output", "result", "deepseek-v3")
    
    module_file = os.path.join(output_base, "2component_select.json")
    component_dir = os.path.join(project_path, "output", "pdf", "pdf_json")
    output_txt_path = os.path.join(output_base, "3module_netlist.txt")
    output_json_path = os.path.join(output_base, "3module_netlist.json")

    if not os.path.isfile(module_file):
        print(f"Error: Component selection file not found {module_file}")
        return
    
    if not os.path.isdir(component_dir):
        print(f"Error: Component library directory not found {component_dir}")
        return

    print(f"Generating netlist for project: {os.path.basename(project_path)}")

    modules_data = read_json_file(module_file)
    components = load_all_components(component_dir)

    if not components:
        print("Warning: No components loaded. Stopping.")
        return

    all_netlist_text = []
    processed_modules = 0
    modules_list = modules_data.get("Functional Modules", [])

    for module in modules_list:
        print(f"  - Processing module: {module.get('Module Name', 'Unknown')}")
        netlist = generate_netlist(module, components)
        if netlist:
            all_netlist_text.append(f"=== Module: {module['Module Name']} ===\n{netlist}\n")
            processed_modules += 1

    if all_netlist_text:
        netlist_text = "\n".join(all_netlist_text)
        netlist_text = clean_netlist_text(netlist_text)

        os.makedirs(os.path.dirname(output_txt_path), exist_ok=True)
        
        with open(output_txt_path, "w", encoding="utf-8") as f:
            f.write(netlist_text)

        netlist_json = parse_netlist_to_json(netlist_text)
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(netlist_json, f, ensure_ascii=False, indent=2)

        print(f"\nDone! Processed {processed_modules}/{len(modules_list)} modules.")
        print(f"Results saved to: {output_base}")
    else:
        print("Error: Failed to generate any netlist content.")

if __name__ == "__main__":
    TARGET_PROJECT_DIR = r"D:\llm\Bathroom Fan"

    if os.path.exists(TARGET_PROJECT_DIR):
        process_single_project_netlist(TARGET_PROJECT_DIR)
    else:
        print(f"Error: Path does not exist: {TARGET_PROJECT_DIR}")
