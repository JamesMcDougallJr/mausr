#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
import motor.py
import ultrasonic.py
GPIO.setmode(GPIO.BOARD)
setup()
if distance() < 10:
    stop()







GPIO.cleanup()
