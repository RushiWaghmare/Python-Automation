import os

def main():
    print("Enter the name of file that you want to open for writing purpose: ")
    Fname=input() 
    

    if os.path.exists(Fname):
        fobj=open(Fname,"r") # r = read the file
        print("file is opend succesfully in read mode")
        
        
        for  line in fobj:
            print(line)
    else:
        
        print("Unable to open file as file is  not present in the current directory")

    
if __name__ == "__main__":
    main()


# Absolute path : C:\Users\Rushikesh\Desktop\python\Automation
# Relative Path : Automations/Marvellous.txt