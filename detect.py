#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
from motor import run, stop, setupMotor
from ultrasonic import setup, distance, destroy, loop
GPIO.setmode(GPIO.BOARD)
if __name__==("__main__"):
    setup()
    setupMotor()
run()
distance()
loop()
time.sleep(10)
    



