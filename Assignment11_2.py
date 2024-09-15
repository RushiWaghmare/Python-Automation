import sys 
from sys import argv, exit
import hashlib
import os
import time

def hashfile(path, blocksize=1024): 
    afile = open(path, 'rb') 
    hasher = hashlib.md5() 
    
    buf = afile.read(blocksize) 
   
    while len(buf) > 0:
        hasher.update(buf) 
        buf = afile.read(blocksize) 
    afile.close() 
    return hasher.hexdigest() 

def FindDuplicate(path):

    flag = os.path.isabs(path)

    if (flag == False):
        print("path is not ansolute path")
        path=os.path.abspath(path)
        print("converted absolute path is : ",path)

    exists =os.path.isdir(path)
    dups = {}

    if exists == True:
        for dirName,subdirName,Filelist in os.walk(path):
            for filelen in Filelist:
                File_path= os.path.join(dirName,filelen)
                File_hash=hashfile(File_path)
                if File_hash in dups:
                    dups[File_hash].append(File_path)
                else:
                    dups[File_hash]=[File_path]
                
        return dups
    else:
        print("invalid path")
        return{}
        
def writelog(dups):

    log_file=open('Log.txt','w')
    for file_list in dups.values():
        if  len(file_list)> 1:
            log_file.write("Duplicate files %s:\n"%(time.ctime()))
            for file_path in file_list:
                log_file.write(file_path + '\n')
            log_file.write('\n')
    log_file.close

    
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

                arr={}
                arr = FindDuplicate(sys.argv[1])
                writelog(arr)

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