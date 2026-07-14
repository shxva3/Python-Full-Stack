""" SMTP Module
email.message
"""
import smtplib
import ssl
from email.message import EmailMessage
sender_email ="shiva98492@gmail.com"
password="ydhmnljipxllxtgi"

receiver_email ="shxva3@gmail.com"
message = EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Welcome Mail"
message.set_content("Welcome to the Codegnan")

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
