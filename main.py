from gpiozero import MotionSensor
from datetime import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import numpy as np
import cv2

#need to import twilio and write necessary code

#motionDetector = MotionSensor(4)

#if motionDetector.motion_detected:
    #do some stuff here

class motionpiGUI():
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        master.title("Motion Pi")
        #Labels
        self.labelSensor = Label(frame,text="Detection Status")
        
        #Buttons
        self.buttonQuit=Button(frame,text="Quit", width =15, command=frame.quit)
        self.buttonCamera=Button(frame,text="Camera",width=15,command=self.openCam)
        #Grid
        self.buttonQuit.grid(row=1,column=2,sticky='e')
        self.buttonCamera.grid(row=1,column=1,sticky='e')
        self.labelSensor.grid(row=2,column=1,sticky='e')
    
    def openCam(self):
        #some code here to open video camera if we want to use it
        cap=cv2.VideoCapture(0)
        while(True):
            ret,frame = cap.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            if cv2.waitKey(1)& 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


root=Tk()
root.style=Style()

root.style.theme_use("clam")
root.geometry("225x225")
app=motionpiGUI(root)
root.mainloop()