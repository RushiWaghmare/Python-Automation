import sys 
import hashlib
import os
import time
import smtplib
import sched
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

def hashfile(path, blocksize=1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def delete_duplicate_files(path, log_file_name):
    files_seen = {}
    total_files_scanned = 0
    duplicate_files_found = 0

    flag = os.path.isabs(path)

    if not flag:
        path = os.path.abspath(path)

    if not os.path.isdir(path):
        print("No Such Directory Present in System")
        return total_files_scanned, duplicate_files_found

    log = open(log_file_name, 'a')
    for dirName, subdirName, Filelist in os.walk(path):
        for file in Filelist:
            File_path = os.path.join(dirName, file)
            File_hash = hashfile(File_path)
            total_files_scanned += 1

            if File_hash in files_seen:
                os.remove(File_path)
                log.write(f"Deleted duplicate file: {File_path}\n")
                duplicate_files_found += 1
            else:
                files_seen[File_hash] = File_path

    log.close()
    return total_files_scanned, duplicate_files_found

def send_log(email, log_file_name, start_time, total_files_scanned, duplicate_files_found):
    end_time = time.time()
    mail_content = f"""
    Duplicate File Removal Report:
    
    Start Time: {start_time}
    End Time: {end_time}
    Total Files Scanned: {total_files_scanned}
    Total Duplicate Files Found: {duplicate_files_found}
    """
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = "slooth45@gmail.com"  
    msg['To'] = email
    msg['Subject'] = 'Duplicate File Removal Report'
    msg.attach(MIMEText(mail_content, 'plain'))

    # Attach the log file
    file=open(log_file_name, 'rb') 
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={log_file_name}')
        msg.attach(part)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("slooth45@gmail.com", "rushiW@123") 
    server.send_message(msg)
    server.quit()

def main():
    print("Application name: " + sys.argv[0])

    if len(sys.argv) == 2:
        if sys.argv[1] in ["--h", "--H"]:
            print("This program is Directory Watcher")
            sys.exit()
        if sys.argv[1] in ["--u", "--U"]:
            print("usage : print deleted file name for Directory")
            print("Please provide Directory name")
            sys.exit()
        else:
            try:
                starttime = time.time()
                res = delete_duplicate_files(sys.argv[1], "Marvellous/log.txt")
                endtime = time.time()
                print("Time required for execution of Program is : ", endtime - starttime)
            except ValueError as obj1:
                print("Invalid Arguments, Please enter Valid Directory Name")
            except Exception as obj2:
                print("Invalid to perform due to ", obj2)

    elif len(sys.argv) == 4:
        directory = sys.argv[1]
        interval = int(sys.argv[2])
        email = sys.argv[3]

        scheduler = sched.scheduler(time.time, time.sleep)
        
        def scheduled_task():
            starttime = time.time()
            total_files_scanned, duplicate_files_found = delete_duplicate_files(directory, "Marvellous/log.txt")
            send_log(email, "Marvellous/log.txt", starttime, total_files_scanned, duplicate_files_found)
            scheduler.enter(interval * 60, 1, scheduled_task)
        
        scheduler.enter(0, 1, scheduled_task)
        scheduler.run()

    else:
        print("Invalid Arguments")
        print("Enter --h or --H for information about program")
        print("Enter --u or --U for Usage of program")

if __name__ == "__main__":
    main()
