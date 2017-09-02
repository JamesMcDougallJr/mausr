trig=11 #orange
echo=12 #white
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    time1=time.time()
    time2=time.time()
def distance():

    GPIO.output(trig,GPIO.LOW)
    time.sleep(0.5)
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
       time.sleep(0.3)
def destroy():
    GPIO.cleanup()

