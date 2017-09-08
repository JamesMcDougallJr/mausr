trig=11 #orange
echo=12 #white
trig2=31
echo2=32
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig2,GPIO.OUT)
    GPIO.setup(echo2,GPIO.IN)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    
def distance():
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
       print(dis,'cm','')
       if dis <10.0:
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
def destroy():
    GPIO.cleanup()

