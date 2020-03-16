#!/usr/bin/env python3

import serial, io, re, sys


# for i in range(2):
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)  # open serial port
arduino_data = ser.readline()
temp = arduino_data.decode(encoding='utf8')
temp = temp.replace("\n",'')
temp = temp.replace("\r",'')

# if i == 1:
# temp = "".join(('"',temp,'"'))
print(temp)
# sys.stdout.write("\b%s" % temp)
# print(arduino_data)
ser.close()

# while True:
#     arduino_data = ser.readline()

#     temp = arduino_data.decode(encoding='utf8')
#     temp = temp.replace("\n","")
#     print(temp)
