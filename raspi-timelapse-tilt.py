#!/usr/bin/env python
import os, sys
import time
import RPi.GPIO as GPIO
import pipan

#set pan library as p
p = pipan.PiPan()

# pan position - move to start position
limit_x_left = 60
limit_x_right = 240
x = limit_x_left
p.do_pan (int(x))

# move for every 5 photos taken
moveCount = 0

# Camera loop function
def lapseLoop():
	global moveCount
	global x
	# Create save folder name
	folderName = "/home/pi/Desktop/timelapse/timelapse_" + time.strftime("%Y%m%d%H%M")
	# Check for folder before creating
	#if not os.path.isdir(folderName):
	os.mkdir(folderName)
	# Start file number increment
	fileCount = 1
	# Loop of infinitely
	while True:
		# Create save folder name
		fileName = time.strftime("%H%M")+"_"+str(fileCount)+".jpg"
		print (fileName)
		# Capture the image using raspistill.
		settings = "-w 1920 -h 1080 -q 85 -sh 50 -ex verylong -awb auto -mm average"
		os.system("raspistill " + str(settings) + " -o " + str(folderName) + "/" + str(fileName))

		# File number increment
		fileCount += 1
		moveCount += 1

		if (moveCount == 5):
			moveCount = 0
			p.do_pan (int(x))
			x += 1
			print "moved"

		# Wait 15 seconds before next capture
		time.sleep(15)


lapseLoop()