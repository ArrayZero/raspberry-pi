#!/usr/bin/env python
#
# Copyright (c) 2014 OpenElectrons.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# History:
# Date            Author            Comments
# 01/30/14    Deepak            Initial authoring.
#
#

## @package OpenElectrons_i2c
# This is the i2c module for OpenElectrons i2c devices.

import smbus
import ctypes

## OpenElectrons_i2c: this class provides i2c functions
#  for read and write operations.
class OpenElectrons_i2c(object):

    @staticmethod
    def pi_rev():
        try:
            with open('/proc/cpuinfo','r') as cpuinfo:
                for line in cpuinfo:
                    if line.startswith('Revision'):
                        # case '3' is for some rare pi board - Deepak
                        return 1 if line.rstrip()[-1] in ['1','2','3'] else 2
        except:
            return 0

    @staticmethod
    def which_bus():
        return 1 if OpenElectrons_i2c.pi_rev() > 1 else 0

    ## Initialize the class with the i2c address of your device
    #  @param i2c_address address of your device
    def __init__(self, i2c_address):
        self.address = i2c_address
        b = OpenElectrons_i2c.which_bus()
        self.bus = smbus.SMBus(b)

    ## Write a byte to your i2c device at a given location
    #  @param self The object pointer.
    #  @param reg the register to write value at.
    #  @param value value to write.
    def writeByte(self, reg, value):
        try:
            self.bus.write_byte_data(self.address, reg, value)
        except IOError, err:
            return self.errMsg()


    def readByte(self, reg):
        try:
            result = self.bus.read_byte_data(self.address, reg)
            return (result)
        except IOError, err:
            return self.errMsg()
     
    # for read_i2c_block_data and write_i2c_block_data to work correctly,
    # ensure that i2c speed is set correctly on your pi:
    # ensure following file with contents as follows:
    #    /etc/modprobe.d/i2c.conf
    # options i2c_bcm2708 baudrate=50000
    # (without the first # and space on line above)
    #
    def readArray(self, reg, length):
        try:
            results = self.bus.read_i2c_block_data(self.address, reg, length)
            return results
        except IOError, err:
            return self.errMsg()

    def writeArray(self, reg, arr):
        try:
            self.bus.write_i2c_block_data(self.address, reg, arr)
        except IOError, err:
            return self.errMsg()


    def writeArray_byte_at_a_time(self, reg, arr):
        x=0
        for y in arr:
            self.writeByte(reg+x, y)
            x+=1
        return

    def readString(self, reg, length):
        ss = ''
        for x in range(0, length):
            ss = ''.join([ss, chr(self.readByte(reg+x))])
        return ss

    def readArray_byte_at_a_time(self, reg, length):
        ss = []
        for x in range(0, length):
            w=self.readByte(reg+x)
            ss.append(w)
        return ss

    def readInteger(self, reg):
        try:
            b0 = self.readByte(reg)
            b1 = self.readByte(reg+1)
            r = b0 + (b1<<8)
            return r
        except IOError, err:
          return self.errMsg()

    def readIntegerSigned(self, reg):
        a = self.readInteger(reg)
        signed_a = ctypes.c_int(a).value
        return signed_a

    def readLong(self, reg):
        try:
            b0 = self.readByte(reg)
            b1 = self.readByte(reg+1)
            b2 = self.readByte(reg+2)
            b3 = self.readByte(reg+3)
            r = b0 + (b1<<8) + (b2<<16) + (b3<<24)
            return r
        except IOError, err:
          return self.errMsg()

    def readLongSigned(self, reg):
        a = self.readLong(reg)
        signed_a = ctypes.c_long(a).value
        return signed_a


    ##  Read the firmware version of the i2c device
    def GetFirmwareVersion(self):
        ver = self.readString(0x00, 8)
        return ver

    ##  Read the vendor name of the i2c device
    def GetVendorName(self):
        vendor = self.readString(0x08, 8)
        return vendor

    ##  Read the i2c device id
    def GetDeviceId(self):
        device = self.readString(0x10, 8)
        return device




