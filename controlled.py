#!/usr/bin/env/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
bin1 = 16 #purple the left motor
bin2 = 18 #Yellow
bpwm = 7 #right top PWM
apwm = 40 #orange right bottom pwm
ain2 = 38 #right motor when looking from behind
ain1 = 36
clk = 13
clk2=35
dt2=33
dt = 19
brakeLED=37
  
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setwarnings(False)
    GPIO.setup(brakeLED,GPIO.OUT)
    GPIO.setup(bin1,GPIO.OUT)
    GPIO.setup(bin2,GPIO.OUT)
    GPIO.setup(bpwm,GPIO.OUT)
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
setup()
setupMotor()
runall()
rightCounter=0
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
counter=0
counter2=0
clkLastState = GPIO.input(clk)
clkLastState2 = GPIO.input(clk2)
while True:
    try:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter+= 1
                print(counter)
                
        clkLastState = clkState
        clkState2=GPIO.input(clk2)
        dtState2=GPIO.input(dt2)
        if clkLastState2 !=clkLastState:
            if clkLastState2 != clkState2:
                if dtState2 != clkState2:
                    counter2+=1
                    print(counter2)
        clkLastState2=clkState2
            
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()



