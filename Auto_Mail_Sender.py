import os
import time
import psutil
#import urllib2
import urllib.request
import urllib.error
import smtplib
import schedule
import ssl
from sys import argv
import sys
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False

def MailSender(filename, time):
    try:
        fromaddr = "slooth48@gmail.com"
        toaddr = "rushiwaghmare789@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s
        Welcome to Marvellous Infosystems.
        Please find attached document which contains Log of Running Process.
        Log file is created at: %s

        This is auto-generated mail.
        Thanks & Regards,
        Piyush Manohar Khairnar
        Marvellous Infosystem
            """ % (toaddr, time)

        Subject = """
        Marvellous Infosysytem Process log generated at: %s
        """ % (time)

        msg['Subject'] = Subject
        msg.attach(MIMEText(body, 'plain'))
        
        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(p)
        #here we have used SSL Context
        context = ssl.create_default_context()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls(context=context)
        s.login(fromaddr, "rushiW@123")
        #cbaa wtbm jsnc kykr

        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit() 

        print("Log file successfully sent through Mail")

    except Exception as E:
        print("Unable to send mail.", E)

def ProcessLog(log_dir="Marvellous"):
    listprocess =[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 8
    log_filename = "MarvellousLog{}.log".format(time.strftime("%Y%m%d_%H%M%S"))
    log_path = os.path.join(log_dir, log_filename)
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process logger: " + time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % (log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path, time.ctime())
        endTime = time.time()

        print('Took %s seconds to send main' % (endTime - startTime))
    else:
        print("There is no internet connection")

def main():
    print("---------Rushikesh Waghmare--------")
    print("Application name: " + argv[0])

    if len(argv) == 2:
        if argv[1] == "--h" or argv[1] == "--H":
            print("This program is Directory Watcher")
            exit()
        if argv[1] == "--u" or argv[1] == "--U":
            print("usage: Print Filenames from input Directory Name")
            print("Please provide Directory name")
            exit()
        else:
            try:
                schedule.every(int(argv[1])).minutes.do(ProcessLog)
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except ValueError as obj1:
                print("Invalid Arguments, Please enter Valid Directory Name")

            except Exception as obj2:
                print("Invalid to perform due to ", obj2)

    else:
        print("Invalid Arguments")
        print("Enter --h or --H for information about program")
        print("Enter --u or --U for Usage of program")

if __name__ == "__main__":
    main()
