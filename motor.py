import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

motor1A =16
motor2A = 18
motor3A=22

GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor3A,GPIO.OUT)
while True:
    
    GPIO.output(motor1A,GPIO.HIGH)
    GPIO.output(motor2A,GPIO.LOW)
    GPIO.output(motor3A,GPIO.HIGH)

sleep(2)


GPIO.output(motor3A,GPIO.LOW)

GPIO.cleanup()
