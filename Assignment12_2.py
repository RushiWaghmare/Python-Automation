import psutil
import time
import schedule
import sys

    
def DisplayProcess(process_name):
    listprocess =[]
    for proc in psutil.process_iter(['pid','name','username']):
        if proc.info['name']== process_name:
            listprocess.append(proc.info)
            print(proc.info)
    print( listprocess)

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
                starttime=time.time()
                DisplayProcess(sys.argv[1])
                
                endtime=time.time()
                print("Time required for execution of Program is : ",endtime-starttime)
            
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