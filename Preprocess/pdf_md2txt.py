import os
import glob
from openai import OpenAI

# Initialize LLM
api_key = os.getenv("")
client = OpenAI(api_key=api_key, base_url="")


def read_md_files_with_limit(directory, max_chars_per_file=7000):
    """Read all md files in the directory and limit character count"""
    md_contents = []
    if not os.path.exists(directory):
        return []

    for file_path in glob.glob(os.path.join(directory, "*.md")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                truncated_content = content[:max_chars_per_file]
                md_contents.append((os.path.basename(file_path), truncated_content))
        except Exception as e:
            print(f"Failed to read file {file_path}: {e}")

    return md_contents


def process_md_files(input_directory, output_directory, template_prompt):
    """General processing function"""
    if not os.path.isdir(input_directory):
        return

    md_contents_list = read_md_files_with_limit(input_directory)
    
    if not md_contents_list:
        return

    os.makedirs(output_directory, exist_ok=True)
    print(f" Processing: {input_directory}")

    for file_name, md_content in md_contents_list:
        output_file_path = os.path.join(output_directory, os.path.splitext(file_name)[0] + ".txt")
        
        # Optional: Skip if file already exists to prevent duplicate processing/billing
        if os.path.exists(output_file_path):
            # print(f"  - Skipping {file_name} (Exists)") 
            continue 

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a professional electronics engineering assistant "
                    "specialized in parsing and summarizing technical documentation "
                    "for electronic components and chips."
                )
            },
            {
                "role": "user",
                "content": template_prompt.format(md_content=md_content)
            }
        ]

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False,
                temperature=0.1,
                top_p=0.95
            )

            result = response.choices[0].message.content.strip()

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(result)

            print(f"  Saved {output_file_path}")
        
        except Exception as e:
            print(f"  Error processing {file_name}: {e}")


def main():
    root_base_dir = "D:/llm/unpdf"

    pdf_template_prompt = (
        "Please analyze the following technical documentation and:\n\n"
        "1. Summarize the component's functionality in one paragraph\n"
        "2. Identify the specific type of this component and extract the 5-10 most critical electrical/physical parameters relevant to its category (e.g., for an MCU: Core, Clock Speed, Flash/RAM; for an LDO: Input Voltage, Max Output Current, Dropout Voltage). List them clearly.\n"
        "3. Extract all pin information and generate a pinout table\n\n"
        "Content:\n{md_content}\n\n"
        "Required output format:\n"
        "Component ID:\n"
        "Component Type:\n"
        "Description:\n<Insert functional summary here>\n\n"
        "Key Parameters:\n"
        "- <Parameter Name>: <Value / Range / Condition>\n"
        "- <Parameter Name>: <Value / Range / Condition>\n"
        "...\n\n"
        "Pinout Table:\n| Pin Number | Pin Name | Function | Description | Pin Type | Electrical Type |\n"
        "| ----- | -------- | -------- | ----------- | -------- | --------------- |\n"
        "<Insert pinout data in table format above>\n"
        "Requirements:\n"
        "1. Parameters MUST be specific to the component's domain.\n"
        "2. Extract ALL pin numbers, names, functions and descriptions (must be complete)\n"
        "3. Maintain strict table format - no omissions\n"
        "4. Output must be in English only\n"
        "5. Only include structured data"
    )

    print(f" Starting batch process in: {root_base_dir}")

    # First level: Iterate through Categories (e.g., MCU, Power...)
    for category_name in os.listdir(root_base_dir):
        category_path = os.path.join(root_base_dir, category_name)
        
        if not os.path.isdir(category_path):
            continue

        # Second level: Iterate through Projects
        for project_name in os.listdir(category_path):
            project_path = os.path.join(category_path, project_name)
            
            if not os.path.isdir(project_path):
                continue

            # -------------------------------------------------
            # Key path matching: root/Category/projectA/output/pdf/pdf_md
            # -------------------------------------------------
            
            # Input directory
            pdf_input_dir = os.path.join(project_path, "output", "pdf", "pdf_md")
            
            # Output directory (generated txt placed under ../pdf_txt)
            pdf_output_dir = os.path.join(project_path, "output", "pdf", "pdf_txt")

            # Check if input directory exists, execute if it does
            if os.path.exists(pdf_input_dir):
                process_md_files(pdf_input_dir, pdf_output_dir, pdf_template_prompt)

    print("\n All processing complete.")


if __name__ == "__main__":
    main()
