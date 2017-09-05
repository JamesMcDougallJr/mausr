#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
#from motor import stop, allBack, right, left
#from speedcontrol import forward,reverse,stop
bin1 = 16 #purple the left motor
bin2 = 18 #Yellow
bpwm = 7 #right top PWM
apwm = 40 #orange right bottom pwm
ain2 = 38 #right motor when looking from behind
ain1 = 36
slow = 20
med  = 50
fast = 100
trig=11 #orange
echo=12 #white
clk = 13
dt = 19
def measureRotations(counter,lastState):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != lastState:
        if dtState != clkState:
            lastState = clkState
        counter+=1
    print(counter)
    return (counter,lastState)
    
    
def setup():
    GPIO.setwarnings(False)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def distance():
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(trig,GPIO.LOW)
    time.sleep(0.4)
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
       #print(dis,'cm','')
       if dis <10.0:
           if dis < 1.0:
               pass
           else:
               return 0
       time.sleep(0.01)
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
def Aforward():
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(ain2,GPIO.LOW)
def Bforward():
    GPIO.output(bin1,GPIO.HIGH)
    GPIO.output(bin2,GPIO.LOW)

def stop():
    GPIO.output(bin1,GPIO.LOW)
    GPIO.output(bin2,GPIO.LOW)
    GPIO.output(ain1,GPIO.LOW)
    GPIO.output(ain2,GPIO.LOW)
    
def Bbackwards():
    GPIO.output(bin2,GPIO.HIGH)
    GPIO.output(bin1,GPIO.LOW)
def Abackwards():
    GPIO.output(ain2,GPIO.HIGH)
    GPIO.output(ain1,GPIO.LOW)
def allBack():
    Bbackwards()
    Abackwards()
def left():
    Bbackwards()
    Aforward()
def right():
    Bforward()
    Abackwards()
    
GPIO.setmode(GPIO.BOARD)
setup()
setupMotor()
time.sleep(2)
runall()
rightCounter=0
counter=0
laststate = GPIO.input(clk)
rotationState=0
LastrotationState=GPIO.input(clk)
while True:
    GPIO.setmode(GPIO.BOARD)
    try:
        [rotationCounter,rotationstate]=measureRotations(counter,laststate)
        if rotationstate==LastrotationState:
            lastrotationState=rotationState            
            allBack()
            time.sleep(1)
            left()
            time.sleep(.5)
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
        GPIO.cleanup()



