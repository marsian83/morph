import os
import subprocess

def replace_extension(file_path, new_extension):
    base_path, _ = os.path.splitext(file_path)
    new_file_path = base_path + new_extension
    return new_file_path

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return result.stderr.strip()
    except Exception as e:
        return str(e)

def find_code_files(folder_path):
    cpp_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".cpp") or file.endswith(".c"):
                cpp_files.append(os.path.relpath(os.path.join(root, file), folder_path))
    return cpp_files

if __name__ == "__main__":
    code_files = find_code_files("./src")
    
    for path in code_files:
        print(path)

        path_shared = "shared/" + replace_extension(path, ".so")
        execute_command(f"g++ -shared -fPIC -o {path_shared} src/{path} -Iinclude -lstdc++")