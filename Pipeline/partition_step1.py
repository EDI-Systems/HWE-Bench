import os
import re
import json
from openai import OpenAI

def load_api_config(config_path="api_config.json"):
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise RuntimeError(f"Error: Configuration file '{config_path}' not found.")
    except json.JSONDecodeError:
        raise RuntimeError(f"Error: Failed to parse '{config_path}'.")

api_config = load_api_config("api_config.json")
client = OpenAI(api_key=api_config.get("api_key", ""), base_url=api_config.get("base_url", ""))

def read_txt_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise RuntimeError(f"Could not read file: {file_path}, Error: {e}")

def clean_raw_output(raw_output):
    raw_output = raw_output.encode('utf-8').decode('utf-8-sig')
    raw_output = re.sub(r"^```(json)?", "", raw_output.strip(), flags=re.IGNORECASE)
    raw_output = re.sub(r"```$", "", raw_output.strip())
    match = re.search(r"(\{.*\})", raw_output, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_output.strip()

def build_prompt(txt_content):
    system_message = (
        "You are an expert embedded hardware systems architect. "
        "Your core task is to design a COMPLETE, FULLY FUNCTIONAL, and PRACTICALLY USABLE circuit architecture strictly based on the provided product description. "
        "Ensuring no essential sub-systems are missing.\n\n"
        "[Execution Constraints]\n"
        "1. Your output MUST be in English only. Do NOT use any other characters.\n"
        "2. Return ONLY valid JSON. No markdown fences, no commentary, no preamble.\n"
        "3. The JSON schema must exactly match the required format.\n"
        "4. Generate ONLY 3 to 6 essential modules in total to represent the complete circuit."
    )
    user_prompt = f"Analyze the product description and extract functional modules.\n\nProduct description:\n{txt_content}\n\nReturn ONLY this JSON format:\n{{\n  \"Functional Modules\": [\n    {{\n      \"Module Name\": \"XXX\",\n      \"Function Description\": \"XXX\",\n      \"Signal Sources\": \"XXX\",\n      \"Signal Destinations\": \"XXX\",\n      \"Implementation Logic\": \"XXX\"\n    }}\n  ]\n}}"
    return [{"role": "system", "content": system_message}, {"role": "user", "content": user_prompt}]

def call_deepseek(messages):
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
        raise RuntimeError(f"API call failed: {e}")

def process_single_project(project_path):
    target_filename = "introduce.txt"
    input_file = os.path.join(project_path, target_filename)

    if not os.path.exists(input_file):
        print(f"Error: Cannot find {target_filename} in path {project_path}")
        return

    output_dir = os.path.join(project_path, "Result", "deepseek-v3")
    os.makedirs(output_dir, exist_ok=True)
    output_json_path = os.path.join(output_dir, "partition_step1.json")

    print(f"Processing project: {os.path.basename(project_path)}")
    txt_content = read_txt_file(input_file)
    messages = build_prompt(txt_content)
    
    print("Waiting for model response...")
    raw_text = call_deepseek(messages)
    cleaned_text = clean_raw_output(raw_text)
    
    try:
        json_data = json.loads(cleaned_text)
        with open(output_json_path, "w", encoding="utf-8") as jf:
            json.dump(json_data, jf, indent=2, ensure_ascii=False)
        print(f"Success! Results saved to: {output_json_path}")
    except Exception as e:
        print(f"Error: JSON parsing failed. {e}")

def main():
    TARGET_PROJECT_DIR = r"D:\llm\Bathroom Fan" 
    if os.path.exists(TARGET_PROJECT_DIR):
        process_single_project(TARGET_PROJECT_DIR)
    else:
        print(f"Error: Path does not exist: {TARGET_PROJECT_DIR}")

if __name__ == "__main__":
    main()