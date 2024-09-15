import os
import time
import psutil
import urllib.request
import urllib.error
import smtplib
import schedule
import ssl
import csv
from datetime import datetime
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

def MailSender(toaddr, subject, body):
    try:
        fromaddr = "slooth48@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        context = ssl.create_default_context()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls(context=context)
        s.login(fromaddr, "rushiW@123")

        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)

        s.quit() 
        print(f"Birthday wish successfully sent to {toaddr}")

    except Exception as E:
        print(f"Unable to send mail to {toaddr}.", E)

def ProcessBirthdays(csv_path):
    if csv_path:
        today = datetime.today().strftime('%m-%d')
        try:
            csvfile =open(csv_path, newline='') 
                reader = csv.reader(csvfile)
                for row in reader:
                    email, birthday = row
                    if datetime.strptime(birthday, '%Y-%m-%d').strftime('%m-%d') == today:
                        connected = is_connected()
                        if connected:
                            subject = "Happy Birthday!"
                            body = f"""
                            Hello,
                            Wishing you a very Happy Birthday!
                            Have a great day ahead!

                            Best Regards,
                            Your Team
                            """
                            MailSender(email, subject, body)
                        else:
                            print("There is no internet connection")
        except Exception as e:
            print("Error reading CSV file:", e)

def main():
    print("---------Rushikesh Waghmare--------")
    print("Application name: " + argv[0])

    if len(argv) == 2:
        csv_path = argv[1]
        if csv_path in ("--h", "--H"):
            print("This program sends birthday wishes to emails listed in a CSV file")
            exit()
        if csv_path in ("--u", "--U"):
            print("usage: Provide the CSV file path")
            exit()
        else:
            try:
                schedule.every().day.at("09:00").do(ProcessBirthdays, csv_path=csv_path)
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except ValueError as obj1:
                print("Invalid Arguments, Please provide valid CSV file path")
            except Exception as obj2:
                print("Failed to perform due to ", obj2)
    else:
        print("Invalid Arguments")
        print("Enter --h or --H for information about the program")
        print("Enter --u or --U for usage of the program")

if __name__ == "__main__":
    main()
