trig=11 #orange
echo =12 #white
trig2=37
echo2=35
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
def setup():
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
def distance():
    GPIO.output(trig,False)
    time.sleep(.5)
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
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
def destroy():
    GPIO.cleanup()
if __name__==("__main__"):
    setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
