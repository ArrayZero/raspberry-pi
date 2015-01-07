import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(3, gpio.OUT)
gpio.output(3,0)

try:
  while True:
    #gpio.output(7, gpio.input(2))
    if( gpio.input(2) == 0 ):
      print('down')
      gpio.output(3,1)
    else:
      gpio.output(3,0)
except KeyboardInterrupt:
  gpio.cleanup()
