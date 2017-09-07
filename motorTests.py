

import time
import RPi.GPIO as GPIO
from motor import setupMotor,stop,left,right
#PWMforward()
ain2 = 38 #right motor when looking from behind
ain1 = 36
apwm = 40 #orange right bottom pwm
bin1 = 16 #purple the left motor
bin2 = 18 #Yellow
bpwm = 7 #right top PWM
def runall():
    
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(ain2,GPIO.LOW)
    GPIO.output(bin2,GPIO.LOW)
    GPIO.output(bin1,GPIO.HIGH)


setupMotor()
GPIO.output(ain1,GPIO.HIGH)
GPIO.output(ain2,GPIO.LOW)
time.sleep(5)
stop()
runall()
time.sleep(3)
right()
time.sleep
stop()
