import sys


def addition(a,b):
    return a+b

def main():
    ret=addition(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition is : ",ret)

if __name__ == "__main__":
    main()