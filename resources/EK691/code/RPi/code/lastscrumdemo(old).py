#! /usr/bin/python

import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *

import numpy as np
import datetime
import time

import RPi.GPIO as GPIO

from twilio.rest import TwilioRestClient
from time import gmtime, strftime

#initialize the Twilio API
client = TwilioRestClient(account = 'ACdcfe2835ebc3cc5a64b326abe1d5f4d0', 
	token = '0dfd8f8b7d00c2f282156422e7a625fd')

#initialize inputs from RPi and circuit board
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)

#initialize credentials for Plotly API
py.sign_in('atomicwest', 'e8q2zycckg')

#embed streaming plot
#tls.embed('streaming-demos','6')

tls.set_credentials_file(username='atomicwest', api_key='e8q2zycckg')
tls.set_credentials_file(stream_ids=["gc1co66vqa", "dddgcrbmrk", "l0arxz77g6",
	 "uigxym0iqj", "1337subfep"])

stream_ids = tls.get_credentials_file()['stream_ids']

print stream_ids

#acquire stream id from list
stream_id = stream_ids[0]

#make instance of stream id object
stream = Stream(
	token = stream_id,
	maxpoints = 50
)

#initialize streaming plot trace, embed unique stream_id
trace1 = Scatter(
	x = [],
	y = [],
	mode = 'lines+markers',
	#embedding 1 stream ID per trace
	stream=stream
)

data = Data([trace1])

layout = Layout(title='Breathing Monitor')

#initialize figure object
fig = Figure(data=data, layout=layout)

#send figure to Plotly while initializing streaming plot
unique_url = py.plot(fig, filename='demostream')

#instance of stream link object with the same stream id as the stream obj
snt = py.Stream(stream_id)
snt.open()

counter = 0
shapeparam = 9
numpts = 100

#initialize parameter for IR digital output
outv = 0
calc = []
summsg = ""

#time delay for stream


while True:
	counter += 1
	repcount = counter % 400 #every 20 sec
	state = GPIO.input(04)

	#x and y are scalar
	x = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')
	#y = (np.cos(shapeparam*counter/50.)*np.cos(counter/50.)+np.random.randn(1))[0]
	
	#initialize a scaling parameter for the output
	#scaling = counter + int((-1^(np.random.randint(5))*(np.random.randint(5))*0.1))

	if state:
		outv = 8
		#outv = 8 + int((-1^(np.random.randint(5)))*counter/scaling)
	else:
		outv = 0
		#outv = 0 + int((-1^(np.random.randint(5)))*counter/scaling)

	y = outv 	
	calc.append(outv)
	
	#write to Plotly stream
	snt.write(dict(x=x, y=y))

	#plot time.sleep was here
	
	#no-breathing condition
	
	#if counter > 400:
		#currsum = sum(calc[(len(calc) - 325):(len(calc) - 1)])

		#if currsum == 0:
			#client.messages.create(to='+17073155745', from_='+17073108595',
				#body = "ALERT: BABY NOT BREATHING")
		#4 minute cycle to override above cycle
		#time.sleep(250) 

	#send text for periodic messages
	if repcount == 0:
		#calculate data, 
		avgb = np.average(calc)
		avgb = abs(avgb)
		#savgb = str(avgb)
		savgb = format(avgb, '.2f')
		ltime = 0.05*counter
		sltime = str(ltime)

		#std tells how far apart one value is to the group data
		#variance --> small variance = cdata close to mean
		#proxy for how regular and deep breathing is
		dev1 = np.std(calc) 
		var1 = np.var(calc)
		DVr1 = dev1/var1

		sdev = str(dev1)
		svar = str(var1)
		sDVr = str(DVr1)

		#scalar = scaling*counter
		#sscalar = str(scalar)		

	
		currsum = sum(calc[(len(calc) - 200):(len(calc) - 1)])
		print currsum
		if currsum == 0:
			summsg = "ALERT: CHILD NOT BREATHING"
		else: 
			summsg = "Your child is breathing well"

		#4 minute cycle to override above cycle
		#time.sleep(250)
		
		outmsg = "Average: " + savgb + " breaths per " + sltime + " seconds\n" + summsg

		#client.messages.create(to='+17073155745', from_='+17073108595',
		#	body = outmsg)
		#4 minute cycle to override above cycle
		#time.sleep(250) 

		#format, write to file 
		ctime1 = strftime("%Y-%m-%d %H:%M:%S" , gmtime())
		ctime2 = ctime1.replace(" ", "")
		ctime2 = ctime2.replace(":", "_")
		#fh = open(ctime2, "w")
		#fh.write("Date: " + ctime1[0:10] + " \n")
		#fh.write("Current time: " + ctime1[12:19] +" \n")
		#fh.write("Average: " + savgb + " breaths per " + sltime + " seconds\n")
		#fh.write("Breath Deviation to Variance ratio: " + sDVr + " \n")
		#fh.write("Scaling factor: " + sscalar + " \n") 
		#fh.write("-----------------------------\n")
		#fh.write(summsg)
		#fh.close() 

	#plot point every 50ms
	time.sleep(0.05)
	

#close stream
snt.close()

#embed streaming plot
tls.embed('streaming-demos','12')

