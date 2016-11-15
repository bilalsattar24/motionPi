from gpiozero import MotionSensor
from datetime import datetime
#need to import twilio and write necessary code

motionDetector = MotionSensor(4)

if motionDetector.motion_detected:
    #do some stuff here