#!/usr/bin/env/python
#motor1A =16
#motor2A = 18
#motor3A=22
#trig=11
#echo =12
import RPi.GPIO as GPIO
import time
#from motor import runMotor, stop, setupMotor
from ultrasonic import setup, distance, destroy, loop
GPIO.setmode(GPIO.BOARD)
setup()
#setupMotor()

try:
    loop()
except KeyboardInterrupt:
    destroy()
    
#runMotor()

#GPIO.cleanup()
