import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(10, GPIO.IN)

inputA = GPIO.input(17)
inputB = GPIO.input(21)
inputC = GPIO.input(22)
inputD = GPIO.input(10)

def callbackA():
	print 'button A pressed'
	return

def callbackB():
	print 'button B pressed'
	return

def callbackC():
	print 'button C pressed'
	return

def callbackD():
	print 'button D pressed'
	return


prev_inputA = 1
prev_inputB = 1
prev_inputC = 1
prev_inputD = 1

runningA=False
runningB=False
runningC=False
runningD=False


while True:
	print inputA
	if ((not prev_inputA) and inputA):
		callbackA();

	if ((not prev_inputB) and inputB):
		callbackB();

	time.sleep(0.05)


