import psutil
import time
import schedule

#list of proceess
#create log file of output
#print cration time of logfile
#schdeule logfile creation every miniute
def logcreation(FileName = "ProcessAutomationPractice1.log"):
    fd=open(FileName,"w")
    seprator="-"*70
    
    fd.write(seprator+"\n")
    fd.write("Process Automation Log"+ "\n")
    fd.write(seprator+"\n")

    fd.write("CONTENT OF LOG FILE"+ "\n")
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
    schedule.every(1).minutes.do(logcreation)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()