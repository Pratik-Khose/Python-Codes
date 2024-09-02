import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox

def create_py_files_from_json(json_file, target_folder):
    # Load file names from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Extract file names from the JSON data
    file_names = data.get('problem_names', [])

    # Ensure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Create .py files in the specified target folder
    for name in file_names:
        # Ensure file name ends with .py
        if not name.endswith('.py'):
            name += '.py'
        file_path = os.path.join(target_folder, name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as py_file:
                py_file.write(f"# This is the {name} file\n")
            print(f"Created: {file_path}")
        else:
            print(f"Skipped (already exists): {file_path}")

def browse_json_file():
    filename = filedialog.askopenfilename(
        title="Select JSON File",
        filetypes=[("JSON Files", "*.json")]
    )
    json_entry.delete(0, tk.END)
    json_entry.insert(0, filename)

def browse_target_folder():
    foldername = filedialog.askdirectory(
        title="Select Target Folder"
    )
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, foldername)

def run_creation():
    json_file = json_entry.get()
    target_folder = folder_entry.get()

    if not json_file or not target_folder:
        messagebox.showerror("Input Error", "Please specify both JSON file and target folder.")
        return

    try:
        create_py_files_from_json(json_file, target_folder)
        messagebox.showinfo("Success", "Files have been created successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("File Creator")

# Create and place widgets
tk.Label(root, text="JSON File:").grid(row=0, column=0, padx=10, pady=10)
json_entry = tk.Entry(root, width=50)
json_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=browse_json_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Target Folder:").grid(row=1, column=0, padx=10, pady=10)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=browse_target_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Create Files", command=run_creation).grid(row=2, column=1, padx=10, pady=20)

# Run the application
root.mainloop()
