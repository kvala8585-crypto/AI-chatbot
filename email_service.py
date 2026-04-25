
import smtplib
from email.mime.text import MIMEText

def send_email(to_email, message):


    print(f"Email sent to {to_email} with message: {message}")