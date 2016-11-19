from twilio.rest import TwilioRestClient
from gpiozero import MotionSensor

pir = MotionSensor(4) #Function used by sensor

ACCOUNT_SID = ""; #User inserted Account ID
AUTH_TOKEN = ""; #User inserted Authentication Token 
                 #Both found on twilio account page

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) #Used to send message with Twilio

while True:
    if pir.motion_detected:    #If motion is detected
        client.messages.create(
            to="", #Phone number you want to text
            from_="+19493976957", #Phone number given by Twilio
            body="Test", #Message you want to text
        )
