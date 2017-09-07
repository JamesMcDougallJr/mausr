from RPi import GPIO
from time import sleep

clk = 13
dt = 19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)
def inches(counter):
        inch=counter*4/15
        print(inch)
def rotationsCount(inch):
        return inch * 15 /4
  
try:
        click=rotationsCount(12)           
        while  click != 0:
                click-=1
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                                print (counter)
                clkLastState = clkState
finally:
        GPIO.cleanup()
