import datetime
import time
import schedule


#user defined f^n
def Schedule_Minute():
    print("Schedular executes after each minute: ",datetime.datetime.now())



def main():
    print(datetime.datetime.now())

    #canonial function call
    schedule.every(1).minute.do(Schedule_Minute)
    
if __name__ =="__main__":
    main()