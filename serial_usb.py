# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:49:15 2020

@author: papitto
"""
#from binascii import hexlify - step needed in python2
import serial
import serial.tools.list_ports as port_list
ports = list(port_list.comports()) # search for the devices
for p in ports: print (p)

#once you find the port  
#in my case it is "/dev/ttyUSB0"
ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)


if(ser.isOpen() == False): #open the serial port only if NOT open yet
    ser.open()
    print("connected to: " + ser.portstr)


#try to get some inputs
ser.flushInput() #erase all info in the box about previous button-presses
count=1


while count==1:
    for line in ser.read():
        #hex = hexlify(line) - step needed in python2
        #num=int(hex, 16)  - step needed in python2
        num=num-4 # change "4" according to the button box you have (my button box counts from 5; 5-4 = index, 6-4 = middle,...)
        print(num) #print the button pressed
        #print(str(count) + str(': ') + chr(line) )
        count= count+1
ser.close()
