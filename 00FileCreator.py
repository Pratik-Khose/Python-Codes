import os
import json

def create_py_files_from_json(json_file):
    # Load file names from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    file_names = data.get('file_names', [])

    # Create .py files in the same folder as the script
    current_folder = os.getcwd()

    for name in file_names:
        file_path = os.path.join(current_folder, name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as py_file:
                py_file.write(f"# This is the {name} file\n")
            print(f"Created: {file_path}")
        else:
            print(f"Skipped (already exists): {file_path}")

if __name__ == "__main__":
    json_file = "file_names.json"  # Path to your JSON file

    create_py_files_from_json(json_file)
