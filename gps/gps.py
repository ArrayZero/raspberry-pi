
from GPSController import *
import time
import datetime




try:
	print "starting gps contoller"
	gpscontrol = GpsController()
	gpscontrol.start()

	#wait for controllers to startup and gps fix
	time.sleep(3)
	#create data file
	datafile = open("data.csv", "w")

	#create datadrawer object
	datadrawer = DataDrawer()

	#loop
	while(true):
	    #get framecount
	    framecount = vidcontrol.getFrameCount()
	    
	    #wait for a bit as the gps data is a little behind + it allows the processor to have a rest!
	    time.sleep(0.1)

	    #get gps data
	    lat = gpscontrol.fix.latitude
	    lon = gpscontrol.fix.longitude
	    utc = gpscontrol.utc
	    speed = gpscontrol.fix.speed
	    speedMPH = speed * GpsUtils.MPS_TO_MPH
	    
	    #write data
	    dataString = str(framecount) + "," + str(speedMPH) + "," + str(lat) + "," + str(lon) + "," + "\n"
	    datafile.write(dataString)
	    datadrawer.newDataFrame(int(framecount), speedMPH, lat, lon)

finally:

    #shutdown gps controller
    gpscontrol.stopController()
    gpscontrol.join()
    print "stopped gps controllder"
    
    #close data file
    print "closing data file"
    datafile.close()