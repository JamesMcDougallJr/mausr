import RPi.GPIO as GPIO
import time
ain1=16 #purple
ain2=18 #Yellow
stby=22
PWA=7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#setup
def setupMotor():
    
    GPIO.setup(ain1,GPIO.OUT)
    GPIO.setup(ain2,GPIO.OUT)
    GPIO.setup(stby,GPIO.OUT)
    GPIO.setup(PWA,GPIO.OUT)
#run the motor
def run():
    
    GPIO.output(stby,GPIO.HIGH)
    GPIO.output(PWA,GPIO.HIGH)

    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(ain2,GPIO.LOW)
def stop():
    GPIO.output(ain1,GPIO.LOW)


setupMotor()
run()
time.sleep(10)
stop()
                                                                                                                                                                                                                                                                     
