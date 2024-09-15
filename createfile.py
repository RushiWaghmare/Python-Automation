import os

def main():
    print("Enter the name of file that you want to create: ")
    Fname=input()
    
    #open used for create new file as well as open current file
    open(Fname,"x") # X = create the file

if __name__ == "__main__":
    main()

