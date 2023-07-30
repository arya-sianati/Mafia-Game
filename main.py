# Players Email
emails = []

# Characters
characters = []














import smtplib
import random
from email.message import EmailMessage
import time


mail = "aryamafiagame@gmail.com"
token = "ngnkhlrxiztusjub"


def rand_list(list):
    new_list = []
    for i in range(len(list)):
        a = random.randint(0, len(list)-1)
        new_list.append(list[a])
        del list[a]
    
    return new_list


emails = rand_list(emails)
characters = rand_list(characters)

time = time.strftime("%H:%M:%S", time.localtime()) + " "

def send_mails():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(mail, token)

    for i in range(len(emails)):
        msg = EmailMessage()
        msg['Subject'] = 'Mafia Game'
        msg['From'] = mail
        msg['To'] = emails[i]
        msg.set_content(time + characters[i])

        s.send_message(msg)

    s.quit()


if len(characters) == len(emails):
    send_mails()
else:
    print("The number of characters and emails are not equal.\nYou have to add a role twice if you want to have two of that.")


print("Sent")
