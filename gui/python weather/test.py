#test.py

import  pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('12866',units="imperial")
yahoo_result = pywapi.get_weather_from_yahoo('12866',units="imperial")


print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + u"\N{DEGREE SIGN}F now in Saratoga Springs, NY.\n"

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + u"\N{DEGREE SIGN}F now in Saratoga Springs, NY.\n"

