#!/usr/bin/python

import serial
ser = serial.Serial("/dev/ttyAMA0",115200) #ttyS0 is the port on the Pi3, it may be ttyAMA0 on the older Pi's
ser.flushInput()      #clear the input buffer
ser.flushOutput()     #clear the output buffer
ser.timeout = 5       #set the timeout on the serial port to 5 seconds
ser.write("AT\r\n")   #send the AT command
str = ser.readline()  #read a line of data from the serial port
print str             #print the response from the SIM868 chip

str = ser.readline()  #read a line of data from the serial port
print str             #print the response from the SIM868 chip
