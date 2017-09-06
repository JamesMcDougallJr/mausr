import time
import RPi.GPIO as GPIO
brakePin=37
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
def brakesOn():
    pulse= GPIO.PWM(37,50)
    pulse.start(0)
    while True:
        for dc in range(0,101,5):
            pulse.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100,-1,-5):
            pulse.ChangeDutyCycle(dc)
            time.sleep(0.1)
    pulse.stop()
def brakesOn():
    pulse= GPIO.PWM(37,50)
    pulse.start(0)
    for dc in range(0,101,5):
        pulse.ChangeDutyCycle(dc)
        time.sleep(0.1)
    pulse.stop()
def brakesOff():
    pulse=GPIO.PWM(37,50)
    pulse.start(0)
    for dc in range(100,-1,-5):
        pulse.ChangeDutyCycle(dc)
        time.sleep(0.1)
    pulse.stop()
brakesOn()
brakesOff()

