
import psutil
import time
#create log file of output
#add creation time of log file

def CreateLog(FileName="Marvellous.log"):
    fd=open(FileName,"w")
    seprator="-"*70
    
    fd.write(seprator+"\n")
    fd.write("Marvellous Process Log"+ "\n")
    fd.write("Marvellous Process Log"+time.ctime()+ "\n")
    fd.write(seprator+"\n")

    Arr =GetProcessInfo()
    
    for data in Arr:
        fd.write("%s \n"%data)

    fd.write(seprator+"\n")

    fd.close()

def GetProcessInfo():
    listprocess =[]
    for proc in psutil.process_iter(['pid','name','username']):
        listprocess.append(proc.info)

    return listprocess


def main():
    CreateLog()
if __name__ == "__main__":
    main()
