import sys

#use command-line argument
#use exception handling

def addition(no1,no2):
    ans = no1 +no2
    return ans
def main():

    print("Script of : "+sys.argv[0])

    if (len(sys.argv)==2):
        if (sys.argv[1]== "--h" or sys.argv[1] == "--H"):
            print("This program is addition of 2 arguments")
            exit()
        if (sys.argv[1] == "--u" or sys.argv[1]== "--U"):
            print("usage : Addition of 2 intigral arguments")
            print("Please provide 2 arguments")
            exit()
        else:
            print("Invalid Arguments")
            print("Enter --h or --H for information about program")
            print("Enter --u or --U for Usage of program")
            exit()

    if (len(sys.argv)==3):
        try:
            res=addition(int(sys.argv[1]),int(sys.argv[2]))
            print(res)
        
        except ValueError as obj1:
            print("Invalid Arguments, Please enter intigral arguments")

        except Exception as obj2:
            print("Invalid to perform due to ",obj2)

    else:
        print("Invalid Arguments")
        print("Enter --h or --H for information about program")
        print("Enter --u or --U for Usage of program")
        



   
if __name__ =="__main__":
    main()
