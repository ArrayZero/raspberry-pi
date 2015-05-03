#!/usr/bin/env python
#
# Copyright (c) 2014 OpenElectrons.com
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
# Date      Author         Comments
# 08/22/13  Deepak         Initial authoring.
# 08/04/14  Michael Giles  Doxygen
#
# this is driver for the Openelectrons.com PiPan  
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import time

# servo definitions (for current board).
S4 = 0
S5 = 1
S0 = 2
S1 = 3
S2 = 4
S3 = 5
#

## PiPan: this class provides functions for PiPan servo controller
#  for read and write operations.
class PiPan:
    
    ServoBlaster = 0
    y = 0

    ## Initialize the class by opening servoblaster
    #  @param self The object pointer.
    def __init__(self):
        global ServoBlaster
        try:
            ServoBlaster = open('/dev/servoblaster', 'w')
        except (IOError):
            print "*** ERROR ***"
            print "Unable to open the device, check that servod is running"
            print "To start servod, run: sudo /etc/init.d/servoblaster.sh start"
            exit()

    ## Writes a pwm value one of the servo controller pins
    #  @param self The object pointer.
    #  @param pin The servo number at which to write.
    #  @param angle The angle to write to the desired pin.
    def pwm(self, pin, angle):
        #print "servo[" + str(pin) + "][" + str(angle) + "]"
        ServoBlaster.write(str(pin)+'=' + str(int(angle)) + '\n')
        ServoBlaster.flush()

    ## Brings the pan servo to neutral position
    #  @param self The object pointer.
    def neutral_pan(self):
        self.pwm (S4, int(150))

    ## Brings the tilt servo to neutral position
    #  @param self The object pointer.
    def neutral_tilt(self):
        self.pwm (S5, int(150))

    ## Writes pan movement value between 50 and 250
    #  @param self The object pointer.
    def do_pan(self, x):
        if ( x > 250 ):
            x = 250
        if ( x < 50 ):
            x = 50
        self.pwm (S4, int(x))

    # Writes the tilt movement value between 80 and 220
    #  @param self The object pointer.
    def do_tilt(self, y):
        # limit tilt between 80 and 220
        if ( y > 220 ):
            y = 220
        if ( y < 80 ):
            y = 80
        self.pwm (S5, int(y))


