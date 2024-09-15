import sys
import os
import time

def CopyFiles(source_dir, dest_dir):
    # Ensure source directory is absolute
    source_dir = os.path.abspath(source_dir)

    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print("Source directory does not exist")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy files from source to destination directory
    for foldername, subfolders, filenames in os.walk(source_dir):
        for filename in filenames:
            src_file = os.path.join(foldername, filename)
            dest_file = os.path.join(dest_dir, filename)
            
            with open(src_file, 'rb') as src, open(dest_file, 'wb') as dest:
                dest.write(src.read())
                
            print(f"Copied {src_file} to {dest_file}")

def main():
    print("--------------------------------------")
    print("------- Directory Copier ------")
    print("--------------------------------------")

    if len(sys.argv) == 3:
        if sys.argv[1].lower() == "--h":
            print("This script is used to copy files from one directory to another.")
            exit()

        if sys.argv[1].lower() == "--u":
            print("Usage of the script:")
            print("python script.py source_directory destination_directory")
            exit()
    
        try:
            source_dir = sys.argv[1]
            dest_dir = sys.argv[2]
            
            # Function call
            start_time = time.time()
            CopyFiles(source_dir, dest_dir)
            end_time = time.time()

            print("Time required to execute the script is:", end_time - start_time, "seconds")
        except ValueError as e:
            print("Invalid type of arguments:", e)
        except Exception as e:
            print("Failed to perform the task due to:", e)

    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get usage of the application")
    
    # Footer
    print("---------------------------------------------")
    print("------- Thank you for using our script ---------")
    print("---------------------------------------------")

if __name__ == "__main__":
    main()
