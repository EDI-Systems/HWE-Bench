import os
import re
import json
from pathlib import Path

def sanitize_filename_for_os(filename):
    """
    Only used for generating physical filenames.
    Replaces illegal characters to prevent OS-level crashes.
    Internal JSON data remains unmodified.
    """
    return re.sub(r'[<>:"/\\|?*]', '_', str(filename))

def parse_component_text(text_content):
    """Parse component text data, preserving all original characters"""
    component = {
        "ComponentID": "",
        "ComponentType": "",
        "Description": "",
        "KeyParameters": {},  # New dictionary field to store parameters
        "Pins": []
    }
    
    # 1. Extract basic info
    if id_match := re.search(r'Component ID:\s*(.+)', text_content):
        component["ComponentID"] = id_match.group(1).strip()
    
    if type_match := re.search(r'Component Type:\s*(.+)', text_content):
        component["ComponentType"] = type_match.group(1).strip()
    
    # Modified: Description ends before Key Parameters OR Pinout Table
    if desc_match := re.search(r'Description:\s*(.+?)(?=Key Parameters:|Pinout Table:|$)', text_content, re.DOTALL):
        component["Description"] = desc_match.group(1).strip()

    # 2. Extract Key Parameters (New Section)
    if params_match := re.search(r'Key Parameters:\s*(.+?)(?=Pinout Table:|$)', text_content, re.DOTALL):
        params_text = params_match.group(1).strip()
        for line in params_text.split('\n'):
            line = line.strip()
            # Look for bullet points starting with '-'
            if line.startswith('-'):
                # Split only by the first colon to keep values intact
                parts = line[1:].split(':', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    component["KeyParameters"][key] = value

    # 3. Extract Pinout Table
    if table_section := re.search(r'Pinout Table:\s*(.+?)(?=Notes:|\Z)', text_content, re.DOTALL):
        table_text = table_section.group(1).strip()
        
        for row in table_text.split('\n'):
            if '|' not in row:
                continue
            
            cols = [col.strip() for col in row.split('|')]
            
            if cols[0] == "": cols.pop(0)
            if cols and cols[-1] == "": cols.pop()
            
            if len(cols) >= 6:
                if "---" in cols[0] or "Pin Number" in cols[0]:
                    continue
                
                pin_data = {
                    "PinNumber": cols[0],
                    "PinName": cols[1],
                    "Functions": [{
                        "FunctionName": cols[2],
                        "FunctionDescription": cols[3]
                    }],
                    "PinType": cols[4],
                    "ElectricalType": cols[5]
                }
                component["Pins"].append(pin_data)
    
    return component

def process_file(input_path, output_dir):
    """Process single file, maintain data originality"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
            component_data = parse_component_text(content)
        
        if not component_data["ComponentID"]:
            return False
        
        safe_name = sanitize_filename_for_os(component_data['ComponentID'])
        output_path = Path(output_dir) / f"{safe_name}.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(component_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"  ! Processing failed: {os.path.basename(input_path)} -> {str(e)}")
        return False

def batch_process_all_subdirs(root_dir):
    """
    Directory structure: root_dir / Category / Subproject / output / pdf / pdf_txt
    """
    total_files = total_success = 0
    
    if not os.path.exists(root_dir):
        print(f"Error: Root directory does not exist {root_dir}")
        return

    for category in os.listdir(root_dir):
        cat_path = os.path.join(root_dir, category)
        if not os.path.isdir(cat_path): continue
        
        print(f"\n[Category] {category}")
        
        for sub_proj in os.listdir(cat_path):
            proj_path = os.path.join(cat_path, sub_proj)
            if not os.path.isdir(proj_path): continue
            
            input_dir = os.path.join(proj_path, 'output', 'pdf', 'pdf_txt')
            output_dir = os.path.join(proj_path, 'output', 'pdf', 'pdf_json')
            
            success = 0
            count = 0
            if os.path.exists(input_dir):
                for file in os.listdir(input_dir):
                    if file.lower().endswith('.txt'):
                        count += 1
                        if process_file(os.path.join(input_dir, file), output_dir):
                            success += 1
            
            total_files += count
            total_success += success
            if count > 0:
                print(f"  └─ {sub_proj}: Completed {success}/{count}")

    print(f"\n{'='*30}\nAll processing completed! Total: {total_success}/{total_files}")

if __name__ == "__main__":
    # Change to your root directory path
    root_directory = "D:/llm/test" 
    batch_process_all_subdirs(root_directory)
