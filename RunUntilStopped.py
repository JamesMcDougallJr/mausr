"""if measureRotations()==0:
            stop()
            allBack()
            time.sleep(1)
            left()
            time.sleep(.5)     """
import RPi.GPIO as GPIO
import time
from motor import stop
clk = 13
dt = 19
counter = 0
def measureRotations():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    counter=0
    clkLastState = GPIO.input(clk)
    runall()
    #stoppedCounter=0
    time.sleep(2)
    while True:
        time1=time.time()
        time2=time.time()
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        counterCheck=counter
        if clkState != clkLastState:
            if dtState != clkState:
                counter+= 1
                print(counter)
                time2=time.time()
        if counterCheck ==counter:
            
            print('counter hasnt changed')
        clkLastState = clkState
        
bin1 = 16 #purple the left motor
bin2 = 18 #Yellow
bpwm = 7 #right top PWM
apwm = 40 #orange right bottom pwm
ain2 = 38 #right motor when looking from behind
ain1 = 36

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
    GPIO.output(ain2,GPIO.LOW)
    GPIO.output(ain1,GPIO.HIGH)
    GPIO.output(bin1,GPIO.LOW)
    GPIO.output(bin2,GPIO.HIGH)
if __name__==('__main__'):
    setupMotor()
    same=0
    try:
        measureRotations()
    except KeyboardInterrupt:
        stop()
    
