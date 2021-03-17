import smtplib
from email.mime.text import MIMEText
from CSVReader import CSVReader

from config import ACCOUNT, PASSWORD
from helper import get_mail_content
from time import sleep

# Your Account
gmail_user = ACCOUNT
gmail_password = PASSWORD


def send_mail(reciver_name, reciver_mail):
    msg = MIMEText(get_mail_content(reciver_name), "html", "utf-8")
    msg['Subject'] = "PyCon Taiwan 2021: Call for Proposals is now Open"
    msg['From'] = "JunWei Song"
    msg['To'] = reciver_mail
    msg['Cc'] = "program@pycon.tw"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':

    reviewer_list = CSVReader("list.csv")

    for name, mail in reviewer_list.get_rows():
        if name == "Name":
            continue

        send_mail(name, mail)
        print(f"Send to {name}, with {mail}")

        sleep(2)