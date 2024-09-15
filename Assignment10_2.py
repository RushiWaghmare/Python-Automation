import sys
import os
import time

def DirectoryRenamer(DirName, OldExt, NewExt):

    flag = os.path.isabs(DirName)
    if (flag == False):
        DirName=os.path.abspath(Dirname)

        
    if os.path.isdir(DirName):
        for foldername, subfolders, filenames in os.walk(DirName):
            for filename in filenames:
                if filename.lower().endswith(OldExt):
                    old_file = os.path.join(foldername, filename)
                    new_file = os.path.join(foldername, filename[:-len(OldExt)] + NewExt)
                    os.rename(old_file, new_file)
                    print(f'Renamed: {old_file} to {new_file}')
    else:
        print("There is no such Directory")

def main():
    print("--------------------------------------")
    print("-------Directory Renamer--------------")
    print("--------------------------------------")

    if len(sys.argv) == 2 and (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
        print("This script is used to rename files in a directory.")
        print("Usage: DirectoryRename.py <Directory_Name> <Old_Extension> <New_Extension>")
        exit()

    if len(sys.argv) == 2 and (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Usage of the script:")
        print("DirectoryRename.py <Directory_Name> <Old_Extension> <New_Extension>")
        exit()

    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        print("Use --h option to get the help and use --u option to get usage of the application")
        exit()
    
    try:
        DirName = sys.argv[1]
        OldExt = sys.argv[2]
        NewExt = sys.argv[3]

        if not OldExt.startswith("."):
            OldExt = "." + OldExt
        if not NewExt.startswith("."):
            NewExt = "." + NewExt

        starttime = time.time()
        DirectoryRenamer(DirName, OldExt, NewExt)
        endtime = time.time()

        print("Time required to execute the script is:", endtime - starttime)
    except ValueError as e:
        print("Invalid type of arguments:", e)
    except Exception as e:
        print("Unable to perform the task due to:", e)

    print("---------------------------------------------")
    print("-------Thank you for using our script---------")
    print("---------------------------------------------")

if __name__ == "__main__":
    main()
