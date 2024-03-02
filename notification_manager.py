from twilio.rest import Client

TWILIO_SID = "ACa83063af422c6d83d324a8056a9d6164"
TWILIO_AUTH_TOKEN = "92989bf95cef8ff3a7facaf70581104a"
TWILIO_VIRTUAL_NUMBER = "+16813203129"
TWILIO_VERIFIED_NUMBER = "+447498290179"




class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)



