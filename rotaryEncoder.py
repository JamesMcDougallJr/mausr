import RPi.GPIO as GPIO
import time

dt=29
clk=31
sw=33

globalCounter =0

flag=0
Last_RoB_Status=0
Current_RoB_Status=0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dt,GPIO.IN)
    GPIO.setup(clk,GPIO.IN)
    GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    rotaryClear()
def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter
    Last_RoB_Status=GPIO.input(clk)
    while(not GPIO.input(dt)):
        Current_RoB_Status=GPIO.input(clk)
        flag=1
    if flag==1:
        flag=0
        if (Last_RoB_Status==0) and (Current_RoB_Status==1):
            globalCounter+=1
            print('globalCOunter=%d')%globalCounter
        if (Last_RoB_Status==1) and (Current_RoB_Status==0):
            globalCounter-=1
            print('globalCounter=%d')%globalCounter
def clear(ev=None):
    globalCounter=0
    print('globalCounter=%d')%globalCounter
    time.sleep(1)
def rotaryClear():
    GPIO.add_event_detect(sw,GPIO.FALLING,callback=clear)
def loop():
    global globalCounter
    while True:
        rotaryDeal()
        print('globalCounter=%d') % globalCounter 
def destroy():
    GPIO.cleanup()
if __name__==('__main__'):
    setup()
    try:
        loop()
    except KeyboardInterrupt:
       destroy()
