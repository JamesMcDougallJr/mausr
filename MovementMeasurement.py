import serial
ser=serial.Serial('/dev/ttyACM0',9600)
while True:
    if(ser.inWaiting()>0):
        myData=ser.readline()
        print(myData)
