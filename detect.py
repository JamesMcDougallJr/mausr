#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
from motor import stop, allBack, right, left
from ultrasonic import destroy
#from speedcontrol import forward,reverse,stop
bin1 = 16 #purple the left motor
bin2 = 18 #Yellow
bpwm  = 7 #right top PWM
apwm  = 40 #orange right bottom pwm
ain2 = 38 #right motor when looking from behind
ain1 = 36
slow = 20
med = 50
fast = 100
trig=11 #orange
echo=12 #white
def setup():
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
def distance():

    GPIO.output(trig,GPIO.LOW)
    time.sleep(.5)
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig,GPIO.LOW)
    time1=time.time()
    time2=time.time()
    while GPIO.input(echo)==0:
        time1=time.time()
    while GPIO.input(echo)==1:
        time2=time.time()
    pulse_duration=time2-time1    
    return pulse_duration * 17150
def loop():
    while True:
       dis=distance()
       print(dis,'cm','')
       if dis <10.0:
           if dis < 1.0:
               pass
           else:
               return 0
       time.sleep(0.1)
def setupMotor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ain1,GPIO.OUT)
    GPIO.setup(ain2,GPIO.OUT)

    GPIO.setup(bin1,GPIO.OUT)
    GPIO.setup(bin2,GPIO.OUT)
    
    GPIO.setup(apwm,GPIO.OUT)
    GPIO.setup(bpwm,GPIO.OUT)

    GPIO.output(bpwm,GPIO.HIGH)
    GPIO.output(apwm,GPIO.HIGH)
#run the motor
def runall():
    GPIO.output(ain2,GPIO.LOW)
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(bin1,GPIO.LOW)
    GPIO.output(bin2,GPIO.HIGH)

    
GPIO.setmode(GPIO.BOARD)
setup()
setupMotor()
time.sleep(10)
runall()
rightCounter=0
while True:
    try:
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




