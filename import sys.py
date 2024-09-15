import sys

def addition(a, b):
    return a + b

def main():
    print("--------------------------------------")
    print("------------- Automation to perform addition ------")
    print("---------------------------------------")

    if len(sys.argv) == 2:
        # It will give us information about the script
        if sys.argv[1].lower() == "--h":
            print("This script is used for the addition of 2 different integer values.")
            exit()

        # It will give us how the script works
        elif sys.argv[1].lower() == "--u":
            print("Usage of the script:")
            print("Name_of_File First_argument Second_argument")
            print("Note: Both arguments should be in integer format.")
            exit()

        # It will advise us if we input a wrong value
        else:
            print("Invalid option")
            print("Use --h option to get help and use --u option to get usage of the application.")
            exit()

    elif len(sys.argv) == 3:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            ret = addition(num1, num2)
            print("Addition is:", ret)
        except ValueError:
            print("Both arguments must be integers.")
            print("Use --h option to get help and use --u option to get usage of the application.")
    else:
        print("Invalid number of arguments.")
        print("Use --h option to get help and use --u option to get usage of the application.")

if __name__ == "__main__":
    main()
