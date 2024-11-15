import os
import shutil

def organize_images(source_dir):
    # Define target folders
    raw_folder = os.path.join(source_dir, 'raw')
    jpeg_folder = os.path.join(source_dir, 'jpeg')

    # Supported extensions
    raw_extensions = ['.cr2', '.nef', '.arw', '.rw2', '.orf']  # Add more as needed
    jpeg_extensions = ['.jpg', '.jpeg']

    # Create folders if they don't exist
    os.makedirs(raw_folder, exist_ok=True)
    os.makedirs(jpeg_folder, exist_ok=True)

    # Iterate through files in the source directory
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        # Move files based on extension
        if ext in raw_extensions:
            shutil.move(file_path, os.path.join(raw_folder, file_name))
            print(f"Moved RAW file: {file_name} to {raw_folder}")
        elif ext in jpeg_extensions:
            shutil.move(file_path, os.path.join(jpeg_folder, file_name))
            print(f"Moved JPEG file: {file_name} to {jpeg_folder}")

if __name__ == '__main__':
    source_directory = input("Enter the directory to organize: ").strip()
    if os.path.isdir(source_directory):
        organize_images(source_directory)
    else:
        print("Invalid directory. Please provide a valid path.")
