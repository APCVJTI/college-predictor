import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")


def send_email(
    receiver_email: str,
    subject: str,
    body: str
):

    message = MIMEMultipart("alternative")

    message["From"] = f"College Predictor Team <{EMAIL_ADDRESS}>"
    message["To"] = receiver_email
    message["Subject"] = subject

    plain_text = """
Welcome to College Predictor!

If your email client cannot display HTML,
please open this email in another email application.

Regards,
College Predictor Team
"""

    message.attach(
        MIMEText(plain_text, "plain")
    )

    message.attach(
        MIMEText(body, "html")
    )

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD
        )

        server.send_message(message)