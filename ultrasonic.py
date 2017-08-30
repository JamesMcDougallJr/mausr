trig=11 #orange
echo =12 #white
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
def setup():
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    
def distance():
    GPIO.output(trig,0)
    time.sleep(0.000002)
    GPIO.output(trig,1)
    time.sleep(0.00001)
    GPIO.output(trig,0)
    while GPIO.input(echo)==0:
        a=0
        time1=time.time()
    while GPIO.input(echo)==1:
        a=1
        time2=time.time()
    during=time2-time1
    return during * 17000
def loop():
    while True:
        dis=distance()
        print (dis,'cm')
        print ('')
        if dis < 10:
            return 0
        time.sleep(0.3)
        
        
def destroy():
    GPIO.cleanup()
#if __name__==("__main__"):
    #setup()
#setup()
#try:
    #loop()
#except KeyboardInterrupt:
    #destroy()
