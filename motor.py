import RPi.GPIO as GPIO
import time
ain1 = 16 #purple
ain2 = 18 #Yellow
stby = 22
PWA  = 7
PWB  = 40 #orange
bin2 = 38
bin1 = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#setup
def setupMotor():
    
    GPIO.setup(ain1,GPIO.OUT)
    GPIO.setup(ain2,GPIO.OUT)
    GPIO.setup(stby,GPIO.OUT)
    GPIO.setup(PWA,GPIO.OUT)

    #GPIO.setup(bin1,GPIO.OUT)
    #GPIO.setup(bin2,GPIO.OUT)
    #GPIO.setup(PWB,GPIO.OUT)
#run the motor
def run():
    
    GPIO.output(stby,GPIO.HIGH)
    GPIO.output(PWA,GPIO.HIGH)
    #GPIO.output(PWB,GPIO.HIGH)


    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(ain2,GPIO.LOW)

    #GPIO.output(bin1,GPIO.HIGH)
    #GPIO.output(bin2,GPIO.LOW)
    
def stop():
    GPIO.output(ain1,GPIO.LOW)
    #GPIO.output(bin1,GPIO.LOW)
    




#setupMotor()
#run()
#time.sleep(10)
#stop()
                                                                                                                                                                                                                                                                     
