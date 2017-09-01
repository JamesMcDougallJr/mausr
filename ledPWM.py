import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)

pulse= GPIO.PWM(32,50)
pulse.start(0)
try:
    while True:
        for dc in range(0,101,5):
            pulse.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100,-1,-5):
            pulse.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
pulse.stop()
GPIO.cleanup()
