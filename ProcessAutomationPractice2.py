import psutil
import time
import schedule
import os
import sys 

#list of proceess
#create log file of output
#print cration time of logfile
#schdeule logfile creation every miniute
#get input form user for sheduler time
def logcreation(FolderName):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    
    FileName= os.path.join(FolderName,"Marvellous%s.log"%(time.ctime()))

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
    startTime=time.time()
    logcreation()
    endTime=time.time()
    print("Total execution time : ",endTime-startTime)
    

if __name__ == "__main__":
    main()