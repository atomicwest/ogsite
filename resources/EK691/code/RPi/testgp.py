#! /usr/bin/python

import RPi.GPIO as GPIO
import os
import numpy as np
import time

print GPIO.VERSION

#choose the GPIO pin as input

GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)

#initiate count and output variables
counter = 0
outv = 0

#initiate infinite loop for data collection
while True:
	counter += 1
	#initialize scaling parameter
	scaling = counter + (-1^(np.random.randint(5)))*(np.random.randint(5))*0.1

	if (GPIO.input(04)):
		#print "output on Pin 7 detected"
		#print "111111111111111111111111111111111111111111111111111111"
		outv = 8 + int((-1^(np.random.randint(5)))*counter/(scaling+1))
		print outv
	else: 
		#print "no output on Pin 7"
		#print "000000"
		outv = 1 + int((-1^(np.random.randint(5)))*counter/(scaling+1))
		print outv

	time.sleep(0.25)
