#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
from motor import runall, stop, allBack, setupMotor, Aforward, Bforward, Abackwards, Bbackwards, right, left
from ultrasonic import setup, distance, destroy, loop
GPIO.setmode(GPIO.BOARD)
if __name__==("__main__"):
    setup()
    setupMotor()
#make this into a separate file
def button():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btn,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
      input_state==False:
          return 1 #button is pressed
if button()==1 and GPIO.stby==False: #or whatever motor uses to stop
    try: #the actual running of the function
    
runall()
rightCounter=0
while True:
    try:
        loop() #returns 0 if there is an object within 10cm
        if loop()==0:
            #stop()
            if rightCounter >=5:
                rightCounter=0
                allBack()
                time.sleep(2)
            right()
            rightCounter+=1
            time.sleep(0.25)
        runall()
     except KeyboardInterrupt or (button()==0 and GPIO.stby==True):
        
        stop()
        destroy()
  

'''def right(time):
        right()
        time.sleep(.2)
        stop()'''



