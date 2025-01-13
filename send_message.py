import smtplib
from dotenv import load_dotenv
import os

"""
This program sends an email to TO_EMAIL from FROM_EMAIL
PASSWORD must be a 16 digit app password
"""

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
FROM_EMAIL = os.getenv("FROM_EMAIL")
PASSWORD = os.getenv("APP_EMAIL_PW")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email(to_email, subject, message):
    auth = (FROM_EMAIL, PASSWORD)

    # Create the email content
    email_content = f"Subject: {subject}\n\n{message}"

    try:
        print(f"Sending email to {to_email}...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])
        server.sendmail(auth[0], to_email, email_content)
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your email/password.")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_email_driver():
    subject = "Job Added!"
    message = "Job added! Go check! Link: https://reg.learningstream.com/view/cal4a.aspx?ek=&ref=0&aa=0&sid1=0&sid2=0&as=70&wp=796&tz=0&ms=0&nav=0&cc=0&cat1=0&cat2=0&cat3=0&aid=TFA&rf=&pn=0"  # Email body
    send_email(TO_EMAIL, subject, message)