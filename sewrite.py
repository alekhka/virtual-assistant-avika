#!/usr/bin/env python
          
import time
import serial
import sys
  
ser = serial.Serial(
              
               port='/dev/ttyS0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )

arg = sys.argv[1]         
      
if arg == '1':
    print "arg is", arg
    ser.write('1')
    time.sleep(0.5)
    
elif arg == '2':
    print "arg is", arg
    ser.write('2')
    time.sleep(0.5)
    
elif arg == '3':
    print "arg is", arg
    ser.write('3')
    time.sleep(0.5)
else:
    print "arg error"
    

    
