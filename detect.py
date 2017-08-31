#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
from motor import runall, stop, allBack, setupMotor, Aforward, Bforward, Abackwards, Bbackwards, right, left
from ultrasonic import setup, distance, destroy, loop
GPIO.setmode(GPIO.BOARD)
if __name__==("__main__"):
    setup()
    setupMotor()
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
    except KeyboardInterrupt:
        stop()
        destroy()

'''def right(time):
        right()
        time.sleep(.2)
        stop()'''



