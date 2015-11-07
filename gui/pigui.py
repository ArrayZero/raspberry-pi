#testgui.py
# import gui lib
from Tkinter import *
import tkFont
import time

import  pywapi
import string

import ystockquote


def setTextboxText(self,listString):
	# delete everything in a text box and replace with the text
	self.delete("0.0",END)
	self.insert(END,listString, 'big')


# create window
root = Tk()
# window settings
root.title("STATUS")
# background color
root.configure(background='black')
# sized window
root.geometry("800x400")
# fullscreen window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
# gui init
app = Frame(root)
app.grid()

# get date & time set for init
dateNow = time.strftime("Today: %A %d. %B %Y\n")
timeNow = time.strftime("%I:%M:%S %p")

start_time = time.time()

minute_update = 60
stock_update = 300


# current weather text
weather_now = ''

def display_weather(self):
	global weather_now
	global minute_update
	self.delete("0.0", END)
	self.insert(END, weather_now, 'big')
	if(minute_update == 60):
		minute_update = 0
		try:
			weather_com_result = pywapi.get_weather_from_weather_com('12866', units="imperial")
			weatherCondition = string.lower(weather_com_result['current_conditions']['text'])
			weatherTemp = weather_com_result['current_conditions']['temperature']
			if (weatherCondition and weatherTemp):
				weather_new = "Weather: " + weatherCondition + " and " + weatherTemp + u"\N{DEGREE SIGN}F"
				if(weather_new != weather_now):
					weather_now = weather_new
			else:
				weather_now = "Weather data not available...\n"
			setTextboxText(self, weather_now)
		except:
			pass
	else:
		minute_update += 1
		# print 'minute counter: ' + str(minute_update)


def display_stocks(self):
	global stock_update
	if(stock_update == 300):
		stock_update = 0
		try:
			stock_text = "AAPL:  " + ystockquote.get_today_open('AAPL') + "\n"
			stock_text += "GOOGL: " + ystockquote.get_today_open('GOOGL') + "\n"
			stock_text += "NKE:   " + ystockquote.get_today_open('NKE') + "\n"
			stock_text += "NFLX:  " + ystockquote.get_today_open('NFLX') + "\n"
			stock_text += "GPRO:  " + ystockquote.get_today_open('GPRO') + "\n"
			stock_text += "TSLA:  " + ystockquote.get_today_open('TSLA')
			setTextboxText(self, stock_text)
		except:
			pass
	else:
		stock_update += 1


customFont = tkFont.Font(family="Cambria", size=30)
helv36 = tkFont.Font(family="Helvetica", size=36, weight="bold")

time_text = Text(root)
time_text.configure(bg='#000000', state=NORMAL, highlightthickness=0)
time_text.tag_configure('big', justify=RIGHT, foreground='#ffffff', background="#000000", font=("Helvetica", 30, "bold"))
time_text.insert(END, timeNow, 'big')
time_text.place(x=610, y=355, height=45, width=180)


date_text = Text(root) # state normal = default makes text area editable diabale after setting contents
date_text.configure(bg='#000000', state=NORMAL, highlightthickness=0)
date_text.tag_configure('big', foreground='#ffffff', background="#000000", font=("Helvetica",36,"bold"))
date_text.insert(END, dateNow, 'big')
date_text.configure(state=DISABLED)
date_text.place(x=10, y=10, height=50, width=900)


weather_text = Text(root) # state normal = default makes text area editable diabale after setting contents
weather_text.configure(bg='#000000', state=NORMAL, highlightthickness=0)
weather_text.tag_configure('big', foreground='#ffffff', background="#000000", font=("Helvetica", 36, "bold"))
weather_text.insert(END, 'Getting weather...', 'big')
weather_text.place(x=10, y=10, height=50, width=800)
display_weather(weather_text)

stocks = Text(root)
stocks.configure(bg='#000000', state=NORMAL, highlightthickness=0)
stocks.tag_configure('big', foreground='#ffffff', background="#000000", font=("Helvetica", 26, "bold"))
stocks.insert(END, 'Getting stocks...', 'big')
stocks.place(x=10, y=150, height=300, width=400)
display_stocks(stocks)

root.focus_set()# <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())


def updates():
	timeNow = time.strftime("%I:%M:%S %p")
	setTextboxText(time_text, timeNow)
	display_weather(weather_text)
	display_stocks(stocks)
	root.after(1000, updates)

root.after(1000, updates)
# start event loop
root.mainloop()