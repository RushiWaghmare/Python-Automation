import sys 
from sys import argv, exit
import hashlib
import os
import time

# Directory wathcher
# Directory presend or not
# Directory path is absolute or not
# print time requred for execution of proogram
# print fildername and filename with absolute path using join method 
# display hashcode of all files
def hashfile(path, blocksize=1024): #blocksize =1024 is defalut argument with size 1024b or 1 Kb 
    afile = open(path, 'rb') #rb = open and read file in binary mode with path of file
    hasher = hashlib.md5()  #hashlib.md() inbuild funcition or argument form hashlib module
    
    buf = afile.read(blocksize) # it will read data from blockchain that can be updated or default which is 1024b
   
    while len(buf) > 0: #while loop is used for reading the first 1024b data agian and again until it get 0
        hasher.update(buf) #it will update our file object when we read 1024b data's per Bit
        buf = afile.read(blocksize) # read all data and size after updating every bit from line9
    afile.close()  # close the file
    return hasher.hexdigest() # it will conver hash code into hexadeciamal form

def DisplayCheaksum(path):
    flag = os.path.isabs(path)

    if (flag == False):
        print("path is not ansolute path")

        path=os.path.abspath(path)
        print("converted absolute path is : ",path)

    exists =os.path.isdir(path)
    if exists == True:
        for dirName,subdirName,Filelist in os.walk(path):
            for filelen in Filelist:
                File_path= os.path.join(dirName,filelen)
                File_hash=hashfile(File_path)
                print(File_path)
                print(File_hash)
                print(" ")

    else :
        print("No Such Directory Present in System")



def main():
    print("Application name: " + argv[0])


    if (len(sys.argv)==2):
        if (sys.argv[1]== "--h" or sys.argv[1] == "--H"):
            print("This program is Directory Watcher")
            exit()
        if (sys.argv[1] == "--u" or sys.argv[1]== "--U"):
            print("usage : Print Filenames from input Directory Name")
            print("Please provide Directory name")
            exit()
        else:
    
            try:
                starttime=time.time()
                res = DisplayCheaksum(sys.argv[1])
                
                endtime=time.time()
                print("Time required for execution of Program is : ",endtime-starttime)
            
            except ValueError as obj1:
                print("Invalid Arguments, Please enter Valid Directory Name")

            except Exception as obj2:
                print("Invalid to perform due to ",obj2)

    else:
        print("Invalid Arguments")
        print("Enter --h or --H for information about program")
        print("Enter --u or --U for Usage of program")
        

if __name__ == "__main__":
    main()