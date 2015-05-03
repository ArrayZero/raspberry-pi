#!/usr/bin/env python
#
# 12/23/13  ajkoren
#
# Test pi-pan
#

import time
import os, sys
import pipan
import sys


print "pi-pan pan/tilt demo with Pi-Light"
print pipan.__file__

p = pipan.PiPan()

p.neutral_pan()
p.neutral_tilt()

x = 148
y = 140
p.do_tilt (int(y))
p.do_pan (int(x))

while True:
    try:
        x = int(raw_input ("Enter x: "))
    except ValueError:
        print "Please enter a valid number "
        continue

    try:
        y = int(raw_input ("Enter y: "))
    except ValueError:
        print "Not valid number "

    print "Using: x = ", x, "y = ", y

    if int(x) > 0:
        p.do_pan (int(x))
    if int(y) > 0:
        p.do_tilt (int(y))

