import serial
ser =serial.Serial('/dev/ttyACM0',9600)
string=[]
data=[]
while True:
    if(ser.inWaiting() >0):
        for y in range(len(ser.readline())):
            data[y]=ser.read(y)
                       
        for i in range(len(data)):
            
            if data[i] != type(str):
                string[var]=data[i]
                
        for x in range(len(string)):
            print(string[x])
                       
     
   
