import os

def create_folders(base_dir, num_folders):
    folder_prefix = ""
    for i in range(1, num_folders + 1):
        folder_name = f"{folder_prefix}{i}"
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path)

if __name__ == "__main__":
    base_directory = r""
    num_folders = 27
    create_folders(base_directory, num_folders)
    print("Folders created successfully!")