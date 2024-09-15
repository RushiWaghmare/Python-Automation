import sys
import os
#dire1 madified

def DirectoryWatcher(DirName):
    # os.walk method provides us 3 values by default
    # If we want only filename, we can call it using another loop
    for foldername, subfoldername, filename in os.walk(DirName):
        for name in filename:
            print(name)

def main():
    print("--------------------------------------")
    print("------- Directory Watcher -------")
    print("--------------------------------------")

    if len(sys.argv) == 2:
        # It will give us information about the script
        if sys.argv[1].lower() == "--h":
            print("This script is used to perform Directory Traversal")
            exit()

        # It will give us how the script works
        elif sys.argv[1].lower() == "--u":
            print("Usage of the script:")
            print("Name_of_File Name_of_Directory")
            exit()

        try:
            # Function call
            DirectoryWatcher(sys.argv[1])

        except ValueError as obj1:
            print("Invalid type of arguments")

        except Exception as obj2:
            print("Unable to perform the task due to:", obj2)

    else:
        print("Invalid option")
        print("Use --h option to get help and use --u option to get usage of the application")

    # Footer
    print("----------------------------------")
    print("---------- Thank you for using our script ----------")
    print("------------ Rushikesh Waghmare ----------")

if __name__ == "__main__":
    main()
