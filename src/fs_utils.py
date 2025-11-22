import shutil
import os


def copy_contents(src_path, dest_path):
    # delete all the contents of the destination directory to ensure a clean copy:
    shutil.rmtree(dest_path, ignore_errors=True)
    # create a new empty destination directory:
    os.makedirs(dest_path, exist_ok=True)
    # copy all files and subdirectories, nested files, etc:
    all_files = os.listdir(src_path)
    for file in all_files:
        # get the full path:
        full_src_path = os.path.join(src_path, file)
        full_dest_path = os.path.join(dest_path, file)
        # if it is a file, just copy it and log it:
        if os.path.isfile(full_src_path):
            shutil.copy(full_src_path, full_dest_path)
            print(f"  - {file} (file) copied.")
        # otherwise, create the directory in the destination path and add its contents to the file list to be copied:
        elif os.path.isdir(full_src_path):
            # create the directory in the destination path
            dest_dir_path = os.path.join(dest_path, file)
            os.makedirs(dest_dir_path, exist_ok=True)
            print(f"  - {file}/ (directory) created.")

            # get all files in the directory:
            more_files = os.listdir(full_src_path)
            print(f"    - {len(more_files)} items found in directory '{file}/'.")
            # add them to the list of all files to be copied:
            all_files.extend([os.path.join(file, f) for f in more_files])
            print(all_files)
