import RPi.GPIO as GPIO
import time
bin1 = 16 #purple the left motor
bin2 = 18 #Yellow
bpwm  = 7 #right top PWM
apwm  = 40 #orange right bottom pwm
ain2 = 38 #right motor when looking from behind
ain1 = 36
slow = 20
med = 50
fast = 100

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#setup
def setupMotor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ain1,GPIO.OUT)
    GPIO.setup(ain2,GPIO.OUT)

    GPIO.setup(bin1,GPIO.OUT)
    GPIO.setup(bin2,GPIO.OUT)
    
    GPIO.setup(apwm,GPIO.OUT)
    GPIO.setup(bpwm,GPIO.OUT)

    GPIO.output(bpwm,GPIO.HIGH)
    GPIO.output(apwm,GPIO.HIGH)
#run the motor
def runall():
    setupMotor()
    GPIO.output(ain2,GPIO.LOW)
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(bin1,GPIO.LOW)
    GPIO.output(bin2,GPIO.HIGH)
def Aforward():
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(ain2,GPIO.LOW)
def Bforward():
    GPIO.output(bin1,GPIO.HIGH)
    GPIO.output(bin2,GPIO.LOW)

def stop():
    GPIO.output(bin1,GPIO.LOW)
    GPIO.output(bin2,GPIO.LOW)
    GPIO.output(ain1,GPIO.LOW)
    GPIO.output(ain2,GPIO.LOW)
    
def Bbackwards():
    GPIO.output(bin2,GPIO.HIGH)
    GPIO.output(bin1,GPIO.LOW)
def Abackwards():
    GPIO.output(ain2,GPIO.HIGH)
    GPIO.output(ain1,GPIO.LOW)
def allBack():
    Bbackwards()
    Abackwards()
def left():
    Bbackwards()
    Aforward()
def right():
    Bforward()
    Abackwards()
"""   

rightTopPWM = GPIO.PWM(bin1,slow) #A
rightTopPWM.ChangeFrequency(100)
rightTopPWM.start(0)
rightBottomPWM = GPIO.PWM(bin2,slow) #B
rightBottomPWM.ChangeFrequency(100)
rightBottomPWM.start(0)

#PWM Parameters

def forward(speed=med):
    rightTopPWM.ChangeDutyCycle(speed)
    rightBottomPWM.ChangeDutyCycle(0)
def reverse(speed=med):
    rightTopPWM.ChangeDutyCycle(0)
    rightBottomPWM.ChangeDutyCycle(speed)
def stop():
    rightTopPWM.ChangeDutyCycle(0)
    rightBottomPWM.ChangeDutyCycle(0)
if __name__ == '__main__':
    setupMotor()
    try:
        while True:
            forward(slow)
            time.sleep(2)
            reverse(med)
            time.sleep(2)
            forward(fast)
            time.sleep(2)
            stop()
            time.sleep(2)
    except KeyboardInterrupt:
        stop()
        print("program stopped")
        GPIO.cleanup()

#setupMotor()
#runall()
#time.sleep(15)
#Bbackwards()
#Abackwards()
#time.sleep(15)
#right()
#time.sleep(10)
#left()
#time.sleep(10)
#stop()
                                                                                                                                                                                                                                                                     
"""
