#!/usr/bin/env/python
import RPI.GPIO as GPIO
import time
trig=11
echo =12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
def distance():
    GPIO.output(trig,0)
    time.sleep(0.000002)
    GPIO.output(trig,1)
    time.sleep(0.00001)
    GPIO.output(trig,0)

while GPIO.input(ECHO)==0:
    a=0
    time-
