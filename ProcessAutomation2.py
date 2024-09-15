import psutil

def DisplayProcess():
    print("List of running  processesa are: ")

    print("-------------------------------")

    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)

    print("-------------------------")

def main():
    DisplayProcess()
if __name__ == "__main__":
    main()