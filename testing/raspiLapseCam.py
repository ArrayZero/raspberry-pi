#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.OUT)

prev_input = 1

# camera loop function
def lapseLoop():
	d = datetime.now()
	initYear = "%04d" % (d.year)
	initMonth = "%02d" % (d.month)
	initDate = "%02d" % (d.day)
	initHour = "%02d" % (d.hour)
	initMins = "%02d" % (d.minute)

	# new foldername
	folderToSave = "timeLapse/timelapse_" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)
	# check for folder before creating
	if not os.path.isdir(folderToSave):
		os.mkdir(folderToSave)
	# Set the initial serial for saved images to 1
	fileSerial = 1
	# Run a WHILE Loop of infinitely
	while True:
		d = datetime.now()
		# Set FileSerialNumber to 000X using four digits
		fileSerialNumber = "%04d" % (fileSerial)
		# Capture the CURRENT time (not start time as set above) to insert into each capture image filename
		hour = "%02d" % (d.hour)
		mins = "%02d" % (d.minute)
		# Define the size of the image you wish to capture.
		imgWidth = 1920 # Max = 2592
		imgHeight = 1080 # Max = 1944
		print " ====================================== Saving file at " + hour + ":" + mins
		#show light for picture status
		GPIO.output(4,GPIO.HIGH)
		# Capture the image using raspistill.
		os.system("raspistill -w " + str(imgWidth) + " -h " + str(imgHeight) + " -o " + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +  ".jpg  -sh 40 -awb auto -mm average -v")
		#shut light off after picture taken
		GPIO.output(4,GPIO.LOW)
		# Increment the fileSerial
		fileSerial += 1
		# Wait 15 seconds before next capture
		time.sleep(15)

# throw light on so we know the script is running
GPIO.output(4,GPIO.HIGH)
# check for button press to start
while True:
	input = GPIO.input(3)
	if ((not prev_input) and input):
		lapseLoop()
	prev_input = input
	time.sleep(0.05)
