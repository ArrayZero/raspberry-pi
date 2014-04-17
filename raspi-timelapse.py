#!/usr/bin/env python
import os
import time
import RPi.GPIO as GPIO
# Setup gpio for button & light
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
# Button set
prev_input = 1
# Camera loop function
def lapseLoop():
	# Create save folder name
	folderName = "timelapse/timelapse_" + time.strftime("%Y%m%d%H%M")
	GPIO.output(4,GPIO.LOW)
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
		# Show light for picture status
		GPIO.output(4,GPIO.HIGH)
		# Capture the image using raspistill.
		#settings = "-w 1920 -h 1080 -q 85 -sh 50 -awb auto -mm average"
		settings = "-w 1920 -h 1080 -q 85 -sh 50 -ex verylong -awb auto -mm average"
		os.system("raspistill " + str(settings) + " -o " + str(folderName) + "/" + str(fileName))
		# Shut light off after picture taken
		GPIO.output(4,GPIO.LOW)
		# File number increment
		fileCount += 1
		# Wait 15 seconds before next capture
		time.sleep(15)
# Throw light on so we know the script is running
GPIO.output(4,GPIO.HIGH)
# Check for button press to start
while True:
	input = GPIO.input(3)
	if ((not prev_input) and input):
		lapseLoop()
	prev_input = input
	time.sleep(0.05)
