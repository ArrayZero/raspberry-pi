#testgui.py
# import gui lib
from Tkinter import *
import tkFont
import time

import  pywapi
import string

import ystockquote

Sapple  = "AAPL:  " + ystockquote.get_today_open('AAPL') + "\n"
Sgoogle = "GOOGL: " + ystockquote.get_today_open('GOOGL') + "\n"
Snike   = "NKE:   " + ystockquote.get_today_open('NKE') + "\n"
Snflx   = "NFLX:   " + ystockquote.get_today_open('NFLX') + "\n"
Sgopro  = "GPRO:  " + ystockquote.get_today_open('GPRO') + "\n"
Stesla  = "TSLA:  " + ystockquote.get_today_open('TSLA')


#get date & time set for init
dateNow = time.strftime("%A %d. %B %Y\n")
timeNow = time.strftime("%I:%M%p")

#get weather set for init
weather_com_result = pywapi.get_weather_from_weather_com('12866',units="imperial")
WeatherNow = "It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + u"\N{DEGREE SIGN}F"



#create window
root = Tk()
# window settings
root.title("STATUS")


#background color
root.configure(background='black')


#sized window
root.geometry("800x400")

#fullscreen window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))



app = Frame(root)
app.grid()

customFont = tkFont.Font(family="Cambria", size=30)
helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold" )


time = Text(root)
time.configure(bg='#000000',state=NORMAL, highlightthickness = 0)
time.tag_configure('big', justify = RIGHT, foreground='#ffffff', background="black", font=("Helvetica",30,"bold" ))
time.insert(END, timeNow, 'big')
time.place(x = 500, y = 355, height=45, width=160)


text = Text(root) #state normal = default makes text area editable diabale after setting contents
text.configure(bg='#000000',state=NORMAL, highlightthickness = 0)
text.tag_configure('big', foreground='#ffffff', background="black", font=("Helvetica",30,"bold" ))
text.insert(END, dateNow, 'big')
text.insert(END, WeatherNow, 'big')
text.configure(state=DISABLED)
# text.pack()
text.place(x = 10, y = 10, height=200, width=800)

stocks = Text(root)
stocks.configure(bg='#000000',state=NORMAL, highlightthickness = 0)
stocks.tag_configure('big', foreground='#ffffff', background="black", font=("Helvetica",30))
stocks.insert(END, Sapple, 'big')
stocks.insert(END, Sgoogle, 'big')
stocks.insert(END, Snflx, 'big')
stocks.insert(END, Snike, 'big')
stocks.insert(END, Sgopro, 'big')
stocks.insert(END, Stesla, 'big')
stocks.place(x = 10, y = 150, height=300, width=400)



# button1 = Button(app, text = "this is a button")
# button1.grid()

# button2 = Button(app, text = "this is button 2")
# button2.grid()


root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())


#start event loop
root.mainloop();
