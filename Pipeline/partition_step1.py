import os
import re
import json
from openai import OpenAI

# --- Configuration Area ---
api_key = os.getenv("")

client = OpenAI(api_key=api_key, base_url="")

def read_txt_file(file_path):
    """Read TXT file content"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise RuntimeError(f"Could not read file: {file_path}, Error: {e}")

def clean_raw_output(raw_output):
    """Clean model output to ensure JSON format is correct"""
    raw_output = raw_output.encode('utf-8').decode('utf-8-sig')
    raw_output = re.sub(r"^```(json)?", "", raw_output.strip(), flags=re.IGNORECASE)
    raw_output = re.sub(r"```$", "", raw_output.strip())
    match = re.search(r"(\{.*\})", raw_output, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_output.strip()

def build_prompt(txt_content):
    """Build Prompt"""
    system_message = (
        "You are an expert embedded hardware systems architect. "
        "Your core task is to design a COMPLETE, FULLY FUNCTIONAL, and PRACTICALLY USABLE circuit architecture strictly based on the provided product description. "
        "Ensuring no essential sub-systems are missing.\n\n"
        "[Execution Constraints]\n"
        "1. Your output MUST be in English only. Do NOT use any other characters like Chinese or French.\n"
        "2. Return ONLY valid JSON. No markdown fences, no commentary, no preamble.\n"
        "3. The JSON schema must exactly match the required format.\n"
        "4. Generate ONLY 3 to 6 essential modules in total to represent the complete circuit."
    )

    user_prompt = f"""
Analyze the product description and extract functional modules.

Product description:
{txt_content}

Return ONLY this JSON format:
{{
  "Functional Modules": [
    {{
      "Module Name": "XXX",
      "Function Description": "XXX",
      "Signal Sources": "XXX",
      "Signal Destinations": "XXX",
      "Implementation Logic": "XXX"
    }}
  ]
}}
""".strip()

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt}
    ]

def call_deepseek(messages):
    """Call DeepSeek API"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat", 
            messages=messages,
            temperature=0.1,
            top_p=0.95,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"DeepSeek API call failed: {e}")

def process_single_project(project_path):
    """Process single project directory"""
    target_filename = "introduce.txt"
    input_file = os.path.join(project_path, target_filename)

    if not os.path.exists(input_file):
        print(f"Error: Cannot find {target_filename} in path {project_path}")
        return

    output_dir = os.path.join(project_path, "output/result/deepseek-v3")
    os.makedirs(output_dir, exist_ok=True)
    output_json_path = os.path.join(output_dir, "1module_info.json")
    output_txt_path = os.path.join(output_dir, "1module_info.txt")

    print(f"Processing project: {os.path.basename(project_path)}")
    
    txt_content = read_txt_file(input_file)
    messages = build_prompt(txt_content)
    
    print("Waiting for model response...")
    raw_text = call_deepseek(messages)
    
    cleaned_text = clean_raw_output(raw_text)
    
    with open(output_txt_path, "w", encoding="utf-8") as raw_log:
        raw_log.write(raw_text)

    try:
        json_data = json.loads(cleaned_text)
        with open(output_json_path, "w", encoding="utf-8") as jf:
            json.dump(json_data, jf, indent=2, ensure_ascii=False)
        print(f"Success! Results saved to: {output_dir}")
    except Exception as e:
        print(f"Warning: JSON parsing failed. Raw output saved to TXT. Error: {e}")

def main():
    TARGET_PROJECT_DIR = r"D:\llm\Bathroom Fan" 
    
    if os.path.exists(TARGET_PROJECT_DIR):
        process_single_project(TARGET_PROJECT_DIR)
    else:
        print(f"Error: Path does not exist: {TARGET_PROJECT_DIR}")

if __name__ == "__main__":
    main()
