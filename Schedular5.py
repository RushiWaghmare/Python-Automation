import datetime
import time
import schedule


#user defined f^n
def Schedule_Minute():
    print("Schedular executes after each minute: ",datetime.datetime.now())

def Schedule_Hour():
    print("Schedular executes after each hour: ",datetime.datetime.now())

def Schedule_Sunday():
    print("Schedular executes after each sunday: ",datetime.datetime.now())



def main():
    print(datetime.datetime.now())

    #canonial function call
    schedule.every(1).minute.do(Schedule_Minute)
    schedule.every(1).hour.do(Schedule_Minute)
    schedule.every().sunday.do(Schedule_Minute)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()