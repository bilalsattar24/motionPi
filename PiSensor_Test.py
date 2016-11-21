from twilio.rest import TwilioRestClient
from gpiozero import MotionSensor
import time

pir = MotionSensor(4) #Function used by sensor

ACCOUNT_SID = "ACb482914bfed498ebab0bc6a28d5b9baf"; #User inserted Account ID
AUTH_TOKEN = "875daa56b7b21d4dbfc3055526f7f3c6"; #User inserted Authentication Token 
                 #Both found on twilio account page

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) #Used to send message with Twilio
go = true #determines whether to send a text or not

while True:
    if pir.motion_detected:   #If motion is detected
        if go:
            sendMessage()
            go = false
            sendTime = time.time #time of last message sent

        elif time.time - sendTime < 300: #5 min
            go = True

def sendMessage(): 
    client.messages.create(
            to="", #Phone number you want to text
            from_="+19493976957", #Phone number given by Twilio
            body="Test", #Message you want to text
        )