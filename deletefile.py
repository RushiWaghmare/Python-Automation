import os

def main():
    print("Enter the name of file that you want to delete: ")
    Fname=input() 
    

    if os.path.exists(Fname):
        os.remove(Fname)
    else:
        
        print("Unable to open file as file is  not present in the current directory")

    
if __name__ == "__main__":
    main()


# Absolute path : C:\Users\Rushikesh\Desktop\python\Automation
# Relative Path : Automations/Marvellous.txt