motor1A =16
motor2A = 18
motor3A=22
import RPi.GPIO as GPIO
def setupMotor():
    GPIO.setup(motor1A,GPIO.OUT)
    GPIO.setup(motor2A,GPIO.OUT)
    GPIO.setup(motor3A,GPIO.OUT)
def runMotor():
    GPIO.output(motor1A,GPIO.HIGH)
    GPIO.output(motor2A,GPIO.LOW)
    GPIO.output(motor3A,GPIO.HIGH)


def stop():
    
    GPIO.output(motor3A,GPIO.LOW)


