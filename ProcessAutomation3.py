import psutil
#create log file of output

def CreateLog(FileName="Marvellous.log"):
    fd=open(FileName,"w")
    seprator="-"*70
    
    fd.write(seprator+"\n")
    fd.write("Marvellous Process Log"+ "\n")
    fd.write(seprator+"\n")

    fd.write("CONTENT OF LOG FILE"+ "\n")
    fd.write(seprator+"\n")
    fd.close()


def main():
    CreateLog()
if __name__ == "__main__":
    main()