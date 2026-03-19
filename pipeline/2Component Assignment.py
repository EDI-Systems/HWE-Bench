import os
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

# ================= Configuration Area =================
MAX_WORKERS = 5   
MAX_RETRIES = 3   
# ======================================================

api_key = os.getenv("")

client = OpenAI(api_key=api_key, base_url="")

def read_json_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_all_components(component_dir):
    """Load all component JSON files in the current project directory"""
    components = []
    if not os.path.isdir(component_dir):
        print(f"Warning: Component directory does not exist: {component_dir}")
        return components

    for file in sorted(os.listdir(component_dir)):
        if file.endswith(".json"):
            try:
                with open(os.path.join(component_dir, file), "r", encoding="utf-8") as f:
                    data = json.load(f)
                    components.append(data)
            except Exception as e:
                print(f"Warning: Skipping invalid component file: {file} -> {e}")
    return components

def extract_json_from_text(text):
    """Extract JSON from LLM response"""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    pattern = r"```json\s*([\s\S]*?)\s*```"
    match = re.search(pattern, text)
    if match:
        try:
            return json.loads(match.group(1))
        except:
            pass
    
    pattern_obj = r"\{[\s\S]*\}"
    match = re.search(pattern_obj, text)
    if match:
        try:
            return json.loads(match.group(0))
        except:
            pass
            
    return None

def recommend_components_task(module, components):
    """Execute component recommendation task for a single module"""
    module_name = module.get('Module Name', 'Unknown')
    
    system_prompt = (
        "You are a professional embedded circuit design expert. Based on the current module's functional description and terminal interface definitions, "
        "analyze the complete internal electrical signal chain and recommend all critical components required for this module from the provided electronic component library.\n\n"
        "[Strict Rules]\n"
        "PIN ACCURACY: The Pin Numbers and Pin Names you output MUST EXACTLY match the definitions in the provided electronic component library. DO NOT invent, alter, or guess any pins.\n\n"
        "RESOURCE EXCLUSIVITY: A physical pin can only be assigned to ONE net. If a pin is multiplexed (e.g., GPIO/I2C/SPI), it can only perform one function in the netlist. DO NOT reuse the same pin for different nets.\n"
        "PROTOCOL INTEGRITY: Interface signals must be complete and paired. For example, UART0_TX must be paired with UART0_RX;Do not leave a single-ended protocol signal dangling unless it is a bus architecture.\n"
        "[Your Tasks]\n"
        "1. Output field 'Signal Chain': Describe the internal signal flow logically.\n"
        "2. Output field 'Recommended Components': A JSON array with ComponentID, Functional Position, Recommendation Reason, and Pin Connections.\n\n"
        "[Output Format]\n"
        "- Strictly output JSON format, no markdown markers."
    )

    user_prompt = {
        "Module Info": module,
        "Component Library": components
    }

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(user_prompt, ensure_ascii=False)}
    ]

    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=0.1,
                top_p=0.95,
                response_format={"type": "json_object"}
            )
            result_text = response.choices[0].message.content.strip()
            parsed = extract_json_from_text(result_text)

            if parsed and "Signal Chain" in parsed and "Recommended Components" in parsed:
                module["Signal Chain"] = parsed["Signal Chain"]
                module["Recommended Components"] = parsed["Recommended Components"]
                print(f"Successfully completed module: {module_name}")
                return True, module
            else:
                print(f"Warning: Parsing failed (Attempt {attempt+1}): {module_name}")
        
        except Exception as e:
            print(f"API Error (Attempt {attempt+1}): {module_name} -> {e}")
            time.sleep(2)

    return False, module

def process_single_project(project_path):
    """Process specified project folder"""
    module_file = os.path.join(project_path, "output/result/deepseek-v3/1module_info.json")
    component_dir = os.path.join(project_path, "output/pdf/pdf_json")
    output_dir = os.path.join(project_path, "output/result/deepseek-v3")
    output_path_prefix = os.path.join(output_dir, "2component_select")

    if not os.path.isfile(module_file):
        print(f"Error: Module info file not found {module_file}")
        return

    print(f"Processing project: {os.path.basename(project_path)}")
    
    try:
        data = read_json_file(module_file)
        components = load_all_components(component_dir)
    except Exception as e:
        print(f"Error: Data loading failed: {e}")
        return

    if not components:
        print("Warning: No component library files found. Stopping.")
        return

    modules_list = data.get("Functional Modules", [])
    if not modules_list:
        print("Warning: No module list found in 1module_info.json.")
        return

    updated_modules = []
    processed_count = 0
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_module = {
            executor.submit(recommend_components_task, mod, components): mod 
            for mod in modules_list
        }

        for future in as_completed(future_to_module):
            success, result_module = future.result()
            updated_modules.append(result_module)
            if success:
                processed_count += 1

    data["Functional Modules"] = updated_modules
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_path_prefix}.json", "w", encoding="utf-8") as f_json:
        json.dump(data, f_json, ensure_ascii=False, indent=2)

    txt_lines = []
    for module in updated_modules:
        if "Signal Chain" in module:
            txt_lines.append(f"=== Module: {module.get('Module Name', 'Unknown')} ===")
            txt_lines.append(f"[Signal Chain]\n{module['Signal Chain']}\n")
            txt_lines.append("[Recommended Components]")
            for comp in module.get("Recommended Components", []):
                txt_lines.append(f"- ComponentID: {comp.get('ComponentID')}")
                txt_lines.append(f"  Position: {comp.get('Functional Position')}")
                txt_lines.append(f"  Reason: {comp.get('Recommendation Reason')}")
                txt_lines.append(f"  Pins: {comp.get('Pin Connections')}\n")

    with open(f"{output_path_prefix}.txt", "w", encoding="utf-8") as f_txt:
        f_txt.write("\n".join(txt_lines))

    print(f"\nProcessing finished! Success rate: {processed_count}/{len(modules_list)}")
    print(f"Results saved to: {output_dir}")

def main():
    TARGET_PROJECT_PATH = r"D:\llm\Bathroom Fan"
    
    if os.path.exists(TARGET_PROJECT_PATH):
        process_single_project(TARGET_PROJECT_PATH)
    else:
        print(f"Error: Path does not exist: {TARGET_PROJECT_PATH}")

if __name__ == "__main__":
    main()
