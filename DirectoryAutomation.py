import sys
import os

def DirectoryWatcher(DireName):
    for foldername, subfoldername,filename in os.walk(DirName):
        for name in filename:
            print(name)
def main():
    print("--------------------------------------")
    print("-------Directory Wathcher------")
    print("--------------------------------------")


    
    if(len(sys.argv) ==2):


        #it will give us information about script
        if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("this scipt is used prform Directory Treversal")
            exit()
        
        #it will give us how script work
        if (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage of the script:")
            print("Name_of_FIle Name_of_Directory")
            exit()
    
        try:
        # Function call
            DirectoryWatcher(sys.argv[1])

        except ValueError as obj1:
            print("Invalid type of arguments")
        
        except Exception as obj2:
            print("Inavalid to perform the task due to ", obj2)

    else:
        print("Invalid option")
        print("Use --h option to ge the help and use -- u option to get usage of applicaton")
    
    #footer
    print("----------------------------------")
    print("--------------Thankyou for using our script")
    print("------------Rushikesh Waghmare----------")
if __name__ == "__main__":
    main()