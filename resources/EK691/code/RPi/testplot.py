#! /usr/bin/python

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('atomicwest', 'e8q2zycckg')

trace0 = Scatter(
	x = [5,6,7,8],
	y = [25,36,49,64]
)
trace1 =  Scatter(
	x = [1,3,5,7],
	y = [3,15,35,57]
)


data = Data([trace0, trace1])

url = py.plot(data, filename = 'testplot')
