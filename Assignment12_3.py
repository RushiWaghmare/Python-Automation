import psutil
import time
import schedule
import os
import sys 

def logcreation(FolderName):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    
    FileName= os.path.join(FolderName,"Assignment12.log")

    fd=open(FileName,"w")
    seprator="-"*70
    
    fd.write(seprator+"\n")
    fd.write("Process Automation Log"+ "\n")
    fd.write(seprator+"\n")
    fd.write("CONTENT OF LOG FILE"+time.ctime() +"\n")

    arr=DisplayProcess()
    for data in arr:
        fd.write("%s""\n"%data)
    fd.write(seprator+"\n")
    fd.close()
    
def DisplayProcess():
    listprocess=[]
    for proc in psutil.process_iter(['pid','name','username']):
        listprocess.append(proc.info)
    return listprocess

def main():
    print("Script of : "+sys.argv[0])

    if (len(sys.argv)==2):
        if (sys.argv[1]== "--h" or sys.argv[1] == "--H"):
            print("This program is Display  running process")
            exit()
        if (sys.argv[1] == "--u" or sys.argv[1]== "--U"):
            print("usage :ProcInfo.py Notepad ")
            
            exit()
        else:
    
            try:
                startTime=time.time()
                logcreation(sys.argv[1])
                endTime=time.time()
                print("Total execution time : ",endTime-startTime)
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