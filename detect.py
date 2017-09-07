#luu/usr/bin/env/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
import serial
#ser=serial.Serial('/dev/ttyACM0',9600)
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
#clk = 13
#dt = 19
brakeLED=37
GPIO.setup(ain1,GPIO.OUT)
GPIO.setup(ain2,GPIO.OUT)
GPIO.setup(apwm,GPIO.OUT)

def measureRotations(counter,lastState):
    GPIO.setmode(GPIO.BOARD)
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)
    if clkState != lastState:
        if dtState != clkState:
            counter+=1
            print(counter)
    lastState = clkState
    tup=(counter,lastState)
    return tup    
def setup():
    GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setwarnings(False)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.setup(brakeLED,GPIO.OUT)
    GPIO.setup(bin1,GPIO.OUT)
    GPIO.setup(bin2,GPIO.OUT)
    GPIO.setup(bpwm,GPIO.OUT)
def brakesOn():
    pulse= GPIO.PWM(brakeLED,50)
    pulse.start(0)
    for dc in range(0,101,1):
        pulse.ChangeDutyCycle(dc)
        time.sleep(0.01)
    pulse.stop()
def brakesOff():
    pulse=GPIO.PWM(brakeLED,50)
    pulse.start(0)
    for dc in range(100,-1,-5):
        pulse.ChangeDutyCycle(dc)
        time.sleep(0.01)
    pulse.stop()

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
    Aforward()
    Bforward()
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
    GPIO.cleanup()
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
setup()
setupMotor()
runall()
rightCounter=0
GPIO.setmode(GPIO.BOARD)
stuckTime2=time.time()
stuckTime1=time.time()
while True:
    
    try:
        if stuckTime2-stuckTime1 > 10:
            allBack()
            time.sleep(2)
        stuckTime1=time.time()
        if loop()==0:
            
            stuckTime2=time.time()
            
            if rightCounter >=5:
                rightCounter=0
                allBack()
		time.sleep(1)
		left()
                time.sleep(0.1)
            brakesOn()
            brakesOff()
            right()
	    time.sleep(0.1)
            rightCounter+=1
        runall()
    except KeyboardInterrupt:
        
        stop()



