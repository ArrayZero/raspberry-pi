#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18,0)

start_time = time.time()
d = datetime.now()
initYear = "%04d" % (d.year)
initMonth = "%02d" % (d.month)
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)



# camera loop function
def lapseLoop():
    GPIO.output(18,0)
    time.sleep(.5)
    GPIO.output(18,1)
    time.sleep(1)
    GPIO.output(18,0)
    time.sleep(.5)
    GPIO.output(18,1)
    time.sleep(1)
    GPIO.output(18,0)
    time.sleep(.5)
    GPIO.output(18,1)
    time.sleep(1)
    GPIO.output(18,0)
    # new foldername
    folderToSave = "/home/pi/timelapse/timelapse_" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)

    # Set the initial serial for saved images to 1
    fileSerial = 1
    
    # check for folder before creating
    if not os.path.isdir(folderToSave):
        os.mkdir(folderToSave)
    
    # Run a WHILE Loop of infinitely
    while True:
        d = datetime.now()
        # Set FileSerialNumber to 000X using four digits
        fileSerialNumber = "%04d" % (fileSerial)
        # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
        hour = "%02d" % (d.hour)
        mins = "%02d" % (d.minute)
        print " ====================================== Saving file at " + hour + ":" + mins
        #show light for picture status
        GPIO.output(18,0)
        #settings
        # Define the size of the image you wish to capture.
        # Max width = 2592
        # Max height = 1944
        settings = "-w 1920 -h 1080 -q 85 -sh 50 -awb auto -mm average -ex verylong -rot 90"
        
        # Capture the image using raspistill.
        os.system("raspistill " + settings + " -o " + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +  ".jpg")
        #shut light off after picture taken
        GPIO.output(18,1)
        time.sleep(0.5)
        # Increment the fileSerial
        fileSerial += 1
        # Wait 15 seconds before next capture
        time.sleep(15)

def startCam():
        GPIO.output(18,0)
        time.sleep(.5)
        GPIO.output(18,1)
        time.sleep(1)
        GPIO.output(18,0)
        time.sleep(.5)
        GPIO.output(18,1)
        time.sleep(1)
        GPIO.output(18,0)
        os.system("raspistill -f -t 60000 -rot 90")
        GPIO.output(18,1)
        while True:
                if(GPIO.input(23) == 0):
                        lapseLoop()
                        GPIO.output(18,1)
                        
                        
# check for button press to start
try:
        while True:
                if(GPIO.input(23) == 0):
                        startCam()
                        GPIO.output(18,1)
                        
                elif(time.time() - start_time > 120):
                        exit(0)
                        
                else:
                        GPIO.output(18,1)
                        time.sleep(0.1)
                        GPIO.output(18,0)
                        time.sleep(0.5)


except KeyboardInterrupt:
        GPIO.cleanup()
