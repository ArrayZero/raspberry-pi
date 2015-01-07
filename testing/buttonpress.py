# import RPi.GPIO as gpio
# gpio.setmode(gpio.BCM)
# gpio.setup(17, gpio.IN)

# running=False

# while True:
#     input = gpio.input(17)
#     if input == False:
# 	if running == True:
# 		running=False
# 	else:
# 		running=True
# 	print(running)
#         while input_value == False:
#             input_value = gpio.input(17)

import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
prev_input = 0
running=False
while True:
	input = GPIO.input(17)
	if ((not prev_input) and input):
		if running == True:
			running=False
		else:
			running=True
		print(running)
	prev_input = input
	time.sleep(0.05)