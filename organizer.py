import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def organize_files(directory):
    directory = os.path.abspath(os.path.expanduser(directory))
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower() if '.' in filename else 'no_extension'
            target_directory = os.path.join(directory, file_extension)
            create_directory(target_directory)
            shutil.move(file_path, os.path.join(target_directory, filename))

if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
    print(f"Files in '{directory}' have been organized.")

