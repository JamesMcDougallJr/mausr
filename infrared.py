import RPi.GPIO as GPIO
IrPin=33
count=0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IrPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def cnt(ev=None):
    global count
    count+=1
    print('Received infrared. cnt= ',count)

def loop():
    while True:
        print(GPIO.input(IrPin))
        if(GPIO.input(IrPin)==0):
            print("Barrier")
    
def destroy():
    GPIO.cleanup()
    
setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
