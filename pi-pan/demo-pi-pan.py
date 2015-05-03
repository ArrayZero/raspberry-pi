#!/usr/bin/env python
#
# Copyright (c) 2013 OpenElectrons.com
# Pi-Pan isntallation script.
# for more information about Pi-Pan,  please visit:
# http://www.openelectrons.com/Pi-Pan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# History:
# Date      Author      Comments
# 08/22/13  Deepak      Initial authoring.
#

import time
import os, sys
import pipan

print "pi-pan pan/tilt demo"

p = pipan.PiPan()

sleep_time = 0.5

x = 128
y = 140

limit_y_bottom = 80
limit_y_top = 180
limit_y_level = 140
limit_x_left = 60
limit_x_right = 240

p.do_tilt (int(y))
p.do_pan (int(x))

def head_up_down(y):
    # move head down
    while y > limit_y_bottom:
        p.do_tilt (int(y))
        time.sleep(sleep_time)
        y -= 2

    # move head up
    while y < limit_y_top:
        p.do_tilt (int(y))
        time.sleep(sleep_time)
        y += 2

    # level the head to look in front
    while y > limit_y_level:
        p.do_tilt (int(y))
        time.sleep(sleep_time)
        y -= 2


while 1:
    # move head to right
    while x < limit_x_right:
        p.do_pan (int(x))
        time.sleep(sleep_time)
        x += 2

    head_up_down(y)

    # move head to left
    while x > limit_x_left:
        p.do_pan (int(x))
        time.sleep(sleep_time)
        x -= 2

    head_up_down(y)

