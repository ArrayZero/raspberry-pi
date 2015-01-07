#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

d = datetime.now()
initYear = "%04d" % (d.year)
initMonth = "%02d" % (d.month)
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

# new foldername
folderToSave = "timelapse_" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)
os.mkdir(folderToSave)
imgWidth = 1920 # Max = 2592
imgHeight = 1080 # Max = 1944

fileSerial = 1

while True:
  d = datetime.now()
  hour = "%02d" % (d.hour)
  mins = "%02d" % (d.minute)

  pictime = str(hour) + str(mins)

  if(pictime == "1900"):
    print ("Start : %s" % time.ctime())
    fileSerialNumber = "%04d" % (fileSerial)
    os.system("raspistill -w " + str(imgWidth) + " -h " + str(imgHeight) + " -o " + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +  ".jpg  -sh 40 -awb auto -mm average -v")
    fileCount += 1
  time.sleep(15)

