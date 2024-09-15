import sys


def addition(a,b):
    return a+b
    
def main():
    print("--------------------------------------")
    print("-------------Automation to perform additon------")
    print("---------------------------------------")


    #it will give us information about script
    if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
        print("this scipt is used for additon of 2 different integral values")
        exit()
    
    #it will give us how script work
    if (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
        print("Usage of the script:")
        print("Name_of_FIle First_argument Second_argument")
        print("Note : Both the arguments shoulbe  in the intefra format")
        exit()
    ret=addition(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition is : ",ret)

if __name__ == "__main__":
    main()