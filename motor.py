motor1A =16
motor2A = 18
motor3A=22


def runMotor():
    GPIO.output(motor1A,GPIO.HIGH)
    GPIO.output(motor2A,GPIO.LOW)
    GPIO.output(motor3A,GPIO.HIGH)


def stop():
    
    GPIO.output(motor3A,GPIO.LOW)


