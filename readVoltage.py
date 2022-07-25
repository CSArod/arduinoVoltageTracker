import time #because we want to put a delay in
import serial #so we can read from the serialport we need
from vpython import * #visual python library can display voltage visually 

arduinoData = serial.Serial('com4',115200)

time.sleep(1) #sets a delay so when we do our loop we dont get junk

while True:
    while arduinoData.in_waiting == 0:
        pass #will read until there is data and then when there is we will exit
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8') #need to turn byte val into str
    dataPacket = int(dataPacket.strip('\r\n')) 

    potVal = dataPacket
    vol = (5./1023.)*potVal #we do this simple eq to get our voltage output
    vol = round(vol,1)

    print(vol) #outputs voltage to console
   
