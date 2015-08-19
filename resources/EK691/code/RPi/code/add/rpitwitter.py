#!/usr/bin/env python
#######################################################################
# # Birdie Tweet
# Takes a picture of a bird when it is at the bird feeder and tweets it to Twitter.
#
# This program requires python2 and twython
# # Author: Mark Reimer
# Date: August 3, 2014
#######################################################################
from twython import Twython
from subprocess import call
import time
import random
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)
# GPIO4 is pin 7

# Twitter Token
APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# How much time in seconds to sleep before looking for another bird
SLEEP_DURATION = 30

# Twitter messages to use when tweeting
messages = []
messages.append("The early bird gets the fresh seeds. #birds #birdwatching")
messages.append("This bird just took a selfie. #birds #birdwatching")
messages.append("Thanks for visiting the tweeting bird feeder. #birds #birdwatching")
messages.append("Another happy bird served. #bird #birds #birdwatching")
messages.append("Who ruffled her feathers? #bird #birds #birdwatching")
messages.append("Show me your birdie. #birds #birdwatching #bird")
messages.append("A #bird on the feeder is worth two tweets. #bird #birds #birdwatching")
messages.append("Free as a bird. #birdwatching #birds #bird")
messages.append("Intelligence without ambition is a bird without wings. -Salvador Dali#birdwatching")

# wait for proximity sensor
while True:
	if (GPIO.input(04)):
		try:
			# Take a picture. I mounted the camera upside down with the ribbon cable going up. So I use the optionto vertically flip the image.
			call("/opt/vc/bin/raspistill -e jpg --vflip -w 320 -h 320 -q 100 -o /tmp/snapshot.jpg", shell=True)
			# Sign in to Twitter 
			twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
			# Post a status update with a picture
			photo = open('/tmp/snapshot.jpg', 'rb')
			r = random.randint(0, len(messages)-1)
			#if statement for selecting different conditions based on input data
			message = messages[r]
			twitter.update_status_with_media(status=message, media=photo)
		except:
			print("Unexpected error:")
			# Sleep so that multiple pictures aren't taken of the same bird
			time.sleep(SLEEP_DURATION)
	else:
		time.sleep(0.25)
