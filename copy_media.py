import os
import shutil

def copy_files_to_desktop():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    hdd_path = "/Volumes/Hard Disk"  # Change this to your actual HDD path
    
    for root, dirs, files in os.walk(hdd_path):
        for file in files:
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(desktop_path, file)
            
            # Check if the file already exists on the desktop
            if os.path.exists(destination_file_path):
                # Check if the file has the same size
                if os.path.getsize(source_file_path) == os.path.getsize(destination_file_path):
                    print(f"File already exists and is the same size: {destination_file_path}")
                    continue
                else:
                    print(f"File exists but differs in size: {destination_file_path}, copying new version.")
                # If the file exists but differs in size, we will copy the new version
                os.remove(destination_file_path)
                continue
            try:
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Copied: {source_file_path} to {destination_file_path}")
            except Exception as e:
                print(f"Error copying {source_file_path} to {destination_file_path}: {e}")

# Function that takes as input a folder path, and creates a zipped archive of that folder on the desktop
def create_zip_archive(folder_path):
    import zipfile
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    zip_file_name = os.path.basename(folder_path) + ".zip"
    zip_file_path = os.path.join(desktop_path, zip_file_name)
    
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
        print(f"Created zip archive: {zip_file_path}")
    except Exception as e:
        print(f"Error creating zip archive: {e}")

if __name__ == "__main__":
    # copy_files_to_desktop()
    create_zip_archive("/Volumes/Hard Disk/bitmovin-master-thesis")