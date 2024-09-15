import psutil
import time
import schedule
#create log file of output
#add creation time of log file
#add shedular to recration of log file againand again

def CreateLog(FileName="Marvellous.log"):
    fd=open(FileName,"a")
    seprator="-"*70
    
    fd.write(seprator+"\n")
    fd.write("Marvellous Process Log"+ "\n")
    fd.write("Marvellous Process Log"+time.ctime()+ "\n")
    fd.write(seprator+"\n")
   
    
    Arr =GetProcessInfo()
    
    for data in Arr:        #it will add every value evry data which is in list
        fd.write("%s \n"%data)

    fd.write(seprator+"\n")

    fd.close()

def GetProcessInfo():
    listprocess =[]
    for proc in psutil.process_iter(['pid','name','username']):
        listprocess.append(proc.info)

    return listprocess


def main():
    schedule.every(1).minutes.do(CreateLog)

    while True: #it gives little break to shedular
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
