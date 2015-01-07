#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

while True:
	os.system("raspistill -f ")
	time.sleep(5)
