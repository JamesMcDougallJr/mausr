#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
from motor import runall, stop, setupMotor, Aforward, Bforward, Abackwards, Bbackwards, right, left
from ultrasonic import setup, distance, destroy, loop
GPIO.setmode(GPIO.BOARD)
if __name__==("__main__"):
    setup()
    setupMotor()

while True:
    loop() #returns 0 if there is an object within 10cm
    if loop()==0:
        stop()
        right()
        time.sleep(5)
        stop()
    runall()


