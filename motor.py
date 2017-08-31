import RPi.GPIO as GPIO
import time
ain1 = 16 #purple the left motor
ain2 = 18 #Yellow
stby = 22
PWA  = 7
PWB  = 40 #orange
bin2 = 38 #right motor when looking from behind
bin1 = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#setup
def setupMotor():
    
    GPIO.setup(ain1,GPIO.OUT)
    GPIO.setup(ain2,GPIO.OUT)
    GPIO.setup(stby,GPIO.OUT)
    GPIO.setup(PWA,GPIO.OUT)

    GPIO.setup(bin1,GPIO.OUT)
    GPIO.setup(bin2,GPIO.OUT)
    GPIO.setup(PWB,GPIO.OUT)
    GPIO.output(PWA,GPIO.HIGH)
    GPIO.output(PWB,GPIO.HIGH)
 
#run the motor
def runall():
    
    GPIO.output(stby,GPIO.HIGH)
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(ain2,GPIO.LOW)

    GPIO.output(bin1,GPIO.HIGH)
    GPIO.output(bin2,GPIO.LOW)
def Aforward():
    GPIO.output(stby,GPIO.HIGH)
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(ain2,GPIO.LOW)
def Bforward():
    GPIO.output(stby,GPIO.HIGH)
    GPIO.output(bin1,GPIO.HIGH)
    GPIO.output(bin2,GPIO.LOW)

def stop():
    GPIO.output(stby,GPIO.LOW)
    
def Bbackwards():
    GPIO.output(bin2,GPIO.HIGH)
    GPIO.output(bin1,GPIO.LOW)
def Abackwards():
    GPIO.output(ain2,GPIO.HIGH)
    GPIO.output(ain1,GPIO.LOW)
def left():
    Bbackwards()
    Aforward()
def right():
    Bforward()
    Abackwards()


setupMotor()
#runall()
#time.sleep(15)
#Bbackwards()
#Abackwards()
#time.sleep(15)
#right()
#time.sleep(10)
#left()
#time.sleep(10)
stop()
                                                                                                                                                                                                                                                                     
