# sendmail.py
# author: Céaman Collins
# sends an email via gmail

import smtplib
from email.mime.text import MIMEText
from config import keys

subject = "Email Subject"
body = "This is the body of the text message"
sender = "andrewbeattycourse@gmail.com"
recipients = ["ceaman.collins@gmail.com", "g00472974@atu.ie"]
password = keys['gmail']


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)