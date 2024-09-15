import sys


def addition(a,b):
    return a+b
    
def main():
    #Banner
    print("--------------------------------------")
    print("-------------Automation to perform additon------")
    print("---------------------------------------")


    
    if(len(sys.argv) ==2):


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
        #it will advise us if we input wrong value
        else:
            print("Invalid option")
            print("Use --h option to ge the help and use -- u option to get usage of applicaton")
    

    if (len(sys.argv)==3):
        ret=addition(int(sys.argv[1]),int(sys.argv[2]))
        print("Addition is : ",ret)

    else:
        print("Invalid option")
        print("Use --h option to ge the help and use -- u option to get usage of applicaton")


if __name__ == "__main__":
    main()