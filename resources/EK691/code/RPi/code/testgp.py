#! /usr/bin/python

import RPi.GPIO as GPIO
import os
import numpy as np
import time

from time import gmtime, strftime

#choose the GPIO pin as input

GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)

#initiate count and output variables
counter = 0
outv = 0
calc = []
summsg = ""

#initiate infinite loop for data collection and store in calc
while True:
	counter += 1
	repcount = counter % 20
	#initialize scaling parameter
	scaling = counter + (-1^(np.random.randint(5)))*(np.random.randint(5))*0.1

	if (GPIO.input(04)):
		#print "output on Pin 7 detected"
		#print "111111111111111111111111111111111111111111111111111111"
		outv = 8 + int((-1^(np.random.randint(5)))*counter/(scaling+1))
		print outv
	else: 
		#print "no output on Pin 7"
		#print "0000000"
		outv = 1 + int((-1^(np.random.randint(5)))*counter/(scaling+1))
		print outv

	calc.append(outv)

	if repcount == 0:
		#calculate data, 
		avgb = np.average(outv)
		avgb = abs(avgb)
		savgb = str(avgb)
		ltime = 0.25*counter
		sltime = str(ltime)

		#std tells how far apart one value is to the group data
		#variance --> small variance = cdata close to mean
		#proxy for how regular and deep breathing is
		dev1 = np.std(outv) 
		var1 = np.var(outv)
		#DVr1 = dev1/var1

		sdev = str(dev1)
		svar = str(var1)
		#sDVr = str(DVr1)

		scalar = scaling*counter
		sscalar = str(scalar)		

		if svar > sdev:
			summsg = "Take your child to the doctor"
		else: 
			summsg = "Your child is breathing well"

		#format, write to file 
		ctime1 = strftime("%Y-%m-%d %H:%M:%S" , gmtime())
		ctime2 = ctime1.replace(" ", "")
		ctime2 = ctime2.replace(":", "_")
		fh = open(ctime2, "w")
		fh.write("Date: " + ctime1[0:10] + " \n")
		fh.write("Current time: " + ctime1[12:19] +" \n")
		fh.write("Average: " + savgb + " breaths per " + sltime + " seconds\n")
		fh.write("Breath Deviation to Variance ratio: " + sdev+"/"+svar + " \n")
		fh.write("Scaling factor: " + sscalar + " \n") 
		fh.write("-----------------------------\n")
		fh.write(summsg)
		fh.close() 

	time.sleep(0.25)
