
trig=11
echo =12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.setup(motor1A,GPIO.OUT)
    GPIO.setup(motor2A,GPIO.OUT)
    GPIO.setup(motor3A,GPIO.OUT)
def distance():
    GPIO.output(trig,0)
    time.sleep(0.000002)
    GPIO.output(trig,1)
    time.sleep(0.00001)
    GPIO.output(trig,0)
    while GPIO.input(echo)==0:
        a=0
        time1=time.time()
    while GPIO.input(echo)==1:
        a=1
        time2=time.time()
    during=time2-time1
    return during * 340/2*100
def loop():
    while True:
        dis=distance()
        print (dis,'cm')
        print ('')
        time.sleep(0.3)
def destroy():
    GPIO.cleanup()
if __name__==("__main__"):
    setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
