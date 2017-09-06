import serial
ser=serial.Serial('/dev/ttyACM0',9600)
data=[]
badstr='\r'
while True:
    
    if(ser.inWaiting() >0):
        myData=ser.readline()
        print(str(myData))
        
        
