import sys
import os

# Directory wathcher
# Directory presend or not
# Directory path is absolute or not

def DirectoryWatcher(DirName):
    flag = os.path.isabs(DirName)

    if (flag == False):
        print("path is not ansolute path")

        DirName=os.path.abspath(DirName)
        print("converted absolute path is : ",DirName)

    exists =os.path.isdir(DirName)
    if exists == True:
        for foldername,subfoldername,filename in os.walk(DirName):
            for name in filename:
                print(name)


    else :
        print("No Such Directory Present in System")



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