motor1A =16
motor2A = 18
motor3A=22
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
def setupMotor():
    GPIO.setup(motor1A,GPIO.OUT)
    GPIO.setup(motor2A,GPIO.OUT)
    GPIO.setup(motor3A,GPIO.OUT)
def runMotor():
    print ("turning motor on")
    GPIO.output(motor1A,GPIO.HIGH)
    GPIO.output(motor2A,GPIO.LOW)
    GPIO.output(motor3A,GPIO.HIGH)
def stop():
    GPIO.output(motor3A,GPIO.LOW)
    GPIO.cleanup()
#if __name__==("__main__"):
    #setupMotor()
setupMotor()
runMotor()
time.sleep(5)
stop()
    
