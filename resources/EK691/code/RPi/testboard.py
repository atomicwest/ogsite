#! /usr/bin/python

import RPi.GPIO as GPIO
import sys
import time
import os

print GPIO.VERSION

#set GPIO numbering to BCM and choose input port
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

#initiate timed loop for demo
tcount = 0 
while tcount < 10:
	#if the input to GPIO4/port 7 is true
	if GPIO.input(4): 
		print 'Object Detected'
	else: 
		print 'No input'
	tcount += 1
