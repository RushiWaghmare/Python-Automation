import os
def main():
    print("Enter the name of file you want to cheak: ")
    Fname=input()

    if os.path.exists(Fname):
        fobj=open(Fname,"r")
        print("file open succesfully")
        print(fobj)

    else:
        print("Cant opne file , file does not exists in currnebt directory")

if __name__ == "__main__":
    main()