import smtplib
import os
from email.message import EmailMessage

sender = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_APP_PASSWORD")
receiver = input("Enter receiver email: ")

if not sender or not password:
    print("Set EMAIL_ADDRESS and EMAIL_APP_PASSWORD first.")
else:
    msg = EmailMessage()
    msg["Subject"] = "Python Internship Project"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Hello! This is a test email from Python.")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Email error:", e)
