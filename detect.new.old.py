#luu/usr/bin/env/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
bin1 = 16 #purple the left motor
bin2 = 18 #Yellow
bpwm = 7 #right top PWM
apwm = 40 #orange right bottom pwm
ain2 = 38 #right motor when looking from behind
ain1 = 36
slow = 20
med  = 80
fast = 100
trig=11 #orange
echo=12 #white
trig2=31
echo2=32
brakeLED=37

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.setup(brakeLED,GPIO.OUT)
    GPIO.setup(trig2,GPIO.OUT)
    GPIO.setup(echo2,GPIO.IN)
def brakesOn():
    setup()
    pulse= GPIO.PWM(brakeLED,50)
    pulse.start(0)
    for dc in range(0,101,1):
        pulse.ChangeDutyCycle(dc)
        time.sleep(0.01)
    pulse.stop()
def brakesOff():
    setup()
    pulse=GPIO.PWM(brakeLED,50)
    pulse.start(0)
    for dc in range(100,-1,-5):
        pulse.ChangeDutyCycle(dc)
        time.sleep(0.01)
    pulse.stop()

def distance():
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(trig,GPIO.LOW)
    time.sleep(0.35)
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
       if dis <20.0:
           return 0
def distance2():
    GPIO.output(trig2,GPIO.LOW)
    time.sleep(0.35)
    GPIO.output(trig2,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig2,GPIO.LOW)
    time1=time.time()
    time2=time.time()
    while GPIO.input(echo2)==0:
        time1=time.time()
    while GPIO.input(echo2)==1:
        time2=time.time()
    pulse_duration=time2-time1   
    return pulse_duration * 17150 
def loop2():
    while True:
        
       dis=distance2()
       print(dis,'cm','')
       if dis <10.0:
           return 0
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
#both motors forward
def runall():
    Aforward()
    Bforward()
#the right motor
def Aforward():
    setupMotor()
    GPIO.output(ain2,GPIO.HIGH)
    GPIO.output(ain1,GPIO.LOW)
#the left motor
def Bforward():
    setupMotor()
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(bin1,GPIO.HIGH)
    GPIO.output(bin2,GPIO.LOW)
    
def Bbackwards():  
    GPIO.output(bin2,GPIO.HIGH)
    GPIO.output(bin1,GPIO.LOW)
def Abackwards():
    GPIO.output(ain2,GPIO.LOW)
    GPIO.output(ain1,GPIO.HIGH)
#stop both motors
def stop():
    GPIO.output(bin1,GPIO.LOW)
    GPIO.output(bin2,GPIO.LOW)
    GPIO.output(ain1,GPIO.LOW)
    GPIO.output(ain2,GPIO.LOW)
    GPIO.cleanup()
#both motors rotate backwards with cool brake lights
def allBack():
    brakesOn()
    Bbackwards()
    Abackwards()
    brakesOff()
#right motor goes forwards left motor goes backwards 
def left():
    Bbackwards()
    Aforward()
#left motor goes backwards right motor goes forwards
def right():
    Bforward()
    Abackwards()
#set the rightCounter to zero
rightCounter=0
GPIO.setmode(GPIO.BOARD)
backCounter=0
while True:
    setup() #setup the ultrasonic
    setupMotor() #setup the motors for output
    runall() #run all motors to start off with
    try:
        if backCounter >3:
            backCounter=0
            left()
            time.sleep(0.5)
            runall()
        if loop()==0: #if the ultrasonic notices something within 10 cm returns 0
            stop()
            right()
            time.sleep(0.5) 
            if rightCounter >=2: #if it tries to turn right more than once, try something else
                rightCounter=0
                if loop2()==0:
                    
                    allBack()
                    backCounter+=1
                    time.sleep(0.25)
                    left()
                    time.sleep(0.5)
            time.sleep(0.25)
            rightCounter+=1
        runall()
    except KeyboardInterrupt:
        break
        stop()
        GPIO.cleanup()
