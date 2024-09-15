import os
import hashlib
from sys import argv, exit

def hashfile(path, blocksize=1024): #blocksize =1024 is defalut argument with size 1024b or 1 Kb 
    afile = open(path, 'rb') #rb = open and read file in binary mode with path of file
    hasher = hashlib.md5()  #hashlib.md() inbuild funcition or argument form hashlib module
    
    buf = afile.read(blocksize) # it will read data from blockchain that can be updated or default which is 1024b
   
    while len(buf) > 0: #while loop is used for reading the first 1024b data agian and again until it get 0
        hasher.update(buf) #it will update our file object when we read 1024b data's per Bit
        buf = afile.read(blocksize) # read all data and size after updating every bit from line9
    afile.close()  # close the file
    return hasher.hexdigest() #after updating file convert its hashcode into hexa

def DisplayChecksum(path): #it will cheak the given path is absolute or not,if not then convert it into absolute
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : " + dirName)
            for filen in fileList: # we are intresred in files so use another loop for file
                filepath = os.path.join(dirName, filen)#fucntion call of hashfile
                file_hash = hashfile(filepath)
                print(filepath) #int will display path and hashcode
                print(file_hash)
                print(' ')
    else:
        print("Invalid Path")

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar------")

    print("Application name: " + argv[0])

    if len(argv) != 2:
        print("Error: invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse a specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        arr = DisplayChecksum(argv[1])  # Corrected DisplayCheaksum to DisplayChecksum
    
    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: invalid input", E)

if __name__ == "__main__":
    main()
