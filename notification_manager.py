import smtplib
from twilio.rest import Client
import sheety
import requests
import os

TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = os.environ["TWILIO_VIRTUAL_NUMBER"]
TWILIO_VERIFIED_NUMBER = os.environ["TWILIO_VERIFIED_NUMBER"]

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        endpoint_url = f"/{sheety.SHEETY_USERNAME}/{sheety.PROJECT}/{sheety.SHEET}"
        url = sheety.base_url + endpoint_url
        response = requests.get(url=url, auth=sheety.BASIC_AUTH_PARAMS)
        data = response.json()
        self.user_data = data[sheety.SHEET]

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

    def send_email(self, mail):
        emails = [row["email"] for row in self.user_data]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{mail}".encode('utf-8'))

