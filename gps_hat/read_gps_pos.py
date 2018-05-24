#!/usr/bin/python

import pynmea2
import serial

ser = serial.Serial('/dev/ttyAMA0',115200)
ser.timeout = 1

ser.flushInput
ser.flushOutput

def parseGPS(str):
	if str.find('GGA') > 0:
		msg = pynmea2.parse(str)
		lat = float(msg.lat)/100
		lon = float(msg.lon)/100
		alt = float(msg.altitude)

		print "Timestamp: %s -- Lat: %.2f %.2s -- Lon: %.2f %.2s  -- Altitude: %.2f %s" % (msg.timestamp,lat,msg.lat_dir,lon,msg.lon_dir,alt,msg.altitude_units)

while True:
	str = ser.readline()
	parseGPS(str)
