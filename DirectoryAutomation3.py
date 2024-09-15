#  FINAL APPLICATION
import sys
import os
import time
#time
#Absulate path cheak

def DirectoryWatcher(DireName):
    #os.walk method provride use 3 values as default
    #if we want only filename the we only call it by using another loop
    

#Absulate path cheak

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName=os.path.abspath(Dirname)

    exist =os.path.isdir(DirName)

    if (exist ==True):
    
        for foldername, subfoldername,filename in os.walk(DirName):
            for name in filename:
                print(name)
    else:
        print("There is no such Directory")
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
            starttime=time.time()
            DirectoryWatcher(sys.argv[1])
            endtime=time.time()

            print("time required to execute the script is :",endtime-starttime)
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

# python DirectoryAutomation.py study
# sys.argv[0]  == > DirectroyAutomation.py
# sys.argv[1]  == > study
#   len(sys.argv) ==2