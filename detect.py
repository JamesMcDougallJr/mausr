#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
from motor import runall, stop, allBack, setupMotor, right, left
from ultrasonic import setup, destroy, loop
from speecontrol import forward,reverse,stop
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



