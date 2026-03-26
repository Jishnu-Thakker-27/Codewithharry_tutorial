import os

def print_directory_contents(path):
    try:
        entries = os.listdir(path)  # returns names in the directory
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return
    except OSError as e:
        print(f"Error: {e}")
        return

    print(f"Contents of directory '{path}':")
    for name in entries:
        print(name)

if __name__ == "__main__":
    dir_path = input("Enter directory path (or leave empty for current dir): ").strip()
    if not dir_path:
        dir_path = "/"  # current directory
    print_directory_contents(dir_path)
