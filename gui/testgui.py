#testgui.py
# import gui lib
from Tkinter import *
import tkFont





#create window
root = Tk()
# window settings
root.title("my display")



# text = Text(root)

# text.insert(INSERT, "Hello.....")



#background color
root.configure(background='black')


#sized window
root.geometry("200x200")

#fullscreen window
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.overrideredirect(1)
# root.geometry("%dx%d+0+0" % (w, h))



app = Frame(root)
app.grid()

customFont = tkFont.Font(family="Helvetica", size=40)

label =  Label(app, text = "This is a label", background="black", foreground="green", font=customFont)
label.grid()


# button1 = Button(app, text = "this is a button")
# button1.grid()

# button2 = Button(app, text = "this is button 2")
# button2.grid()


root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())


#start event loop
root.mainloop();
