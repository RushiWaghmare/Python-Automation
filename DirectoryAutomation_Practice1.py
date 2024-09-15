import sys
import os

# Directory wathcher

def DirectoryWatcher(DirName):
    for foldername,subfoldername,filename in os.walk(DirName):
        for name in filename:
            print(name)



def main():
    print("Script of : "+sys.argv[0])

    if (len(sys.argv)==2):
        if (sys.argv[1]== "--h" or sys.argv[1] == "--H"):
            print("This program is Directory Watcher")
            exit()
        if (sys.argv[1] == "--u" or sys.argv[1]== "--U"):
            print("usage : Print Filenames from input Directory Name")
            print("Please provide Directory name")
            exit()
        else:
    
            try:
                res = DirectoryWatcher(sys.argv[1])
                print(res)
            
            except ValueError as obj1:
                print("Invalid Arguments, Please enter Valid Directory Name")

            except Exception as obj2:
                print("Invalid to perform due to ",obj2)

    else:
        print("Invalid Arguments")
        print("Enter --h or --H for information about program")
        print("Enter --u or --U for Usage of program")
        

if __name__ == "__main__":
    main()