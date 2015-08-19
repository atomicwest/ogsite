#! /usr/bin/python

import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *

import numpy as np
import datetime
import time

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
unique_url = py.plot(fig, filename='stream1')

#instance of stream link object with the same stream id as the stream obj
snt = py.Stream(stream_id)
snt.open()


counter = 0
shapeparam = 9
numpts = 100

#time delay for stream


while True:
	counter += 1
	
	#x and y are scalar
	x = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')
	y = (np.cos(shapeparam*counter/50.)*np.cos(counter/50.)+np.random.randn(1))[0]

	#write to Plotly stream
	snt.write(dict(x=x, y=y))

	#plot point every 70ms
	time.sleep(0.07)

#close stream
snt.close()

#embed streaming plot
tls.embed('streaming-demos','12')

