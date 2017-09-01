#!/usr/bin/env python
import os
import time

# Camera loop function
def lapseLoop():
	# Create save folder name
	folderName = "/media/TIME-LAPSE/timelapse_" + time.strftime("%Y%m%d%H%M")
	# Check for folder before creating
	#if not os.path.isdir(folderName):
	os.mkdir(folderName)
	# Start file number increment
	fileCount = 1
	# Loop of infinitely
	while True:
		# Create save folder name
		fileName = time.strftime("%H%M")+"_"+str(fileCount)+".jpg"
		# Capture the image using raspistill.
		#settings = "-w 1920 -h 1080 -q 85 -sh 50 -awb auto -mm average"
		settings = "-w 1920 -h 1080 -q 85 -sh 50 -ex verylong -awb auto -mm average"
		os.system("raspistill " + str(settings) + " -o " + str(folderName) + "/" + str(fileName))
		# File number increment
		fileCount += 1
		# Wait 15 seconds before next capture
		time.sleep(10)


# Check for button press to start
while True:
	lapseLoop()
