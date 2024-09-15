import sys
import os
import time

def copy_files_with_extension(source_dir, dest_dir, file_extension):
    # Ensure source directory is absolute
    source_dir = os.path.abspath(source_dir)

    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print("Source directory does not exist")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy files with the specified extension from source to destination directory
    for foldername, subfolders, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.lower().endswith(file_extension.lower()):
                src_file = os.path.join(foldername, filename)
                dest_file = os.path.join(dest_dir, filename)
                
                with open(src_file, 'rb') as src, open(dest_file, 'wb') as dest:
                    dest.write(src.read())
                    
                print(f"Copied {src_file} to {dest_file}")

def print_help():
    """
    Print help information.
    """
    print("This script is used to copy files with a specific extension from one directory to another.")

def print_usage():
    """
    Print usage information.
    """
    print("Usage of the script:")
    print('python DirectoryCopyExt.py "source_directory" "destination_directory" ".extension"')

def main():
    print("--------------------------------------")
    print("------- Directory Copier ------")
    print("--------------------------------------")

    if len(sys.argv) == 4:
        if sys.argv[1].lower() == "--h":
            print_help()
            exit()

        if sys.argv[1].lower() == "--u":
            print_usage()
            exit()
    
        try:
            source_dir = sys.argv[1]
            dest_dir = sys.argv[2]
            file_extension = sys.argv[3]
            
            # Function call
            start_time = time.time()
            copy_files_with_extension(source_dir, dest_dir, file_extension)
            end_time = time.time()

            print("Time required to execute the script is:", end_time - start_time, "seconds")
        except ValueError as e:
            print("Invalid type of arguments:", e)
        except Exception as e:
            print("Failed to perform the task due to:", e)
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get usage of the application")
    
    print("---------------------------------------------")
    print("------- Thank you for using our script ---------")
    print("---------------------------------------------")

if __name__ == "__main__":
    main()
