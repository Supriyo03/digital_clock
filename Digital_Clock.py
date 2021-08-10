from tkinter import *
from tkinter.ttk import *
from time import strftime

# Creating tkinter Window
root = Tk()
root.title("Supriyo_Digital_Clock")

# This function is used to display time on the label
def time():
    string = strftime('%I:%M:%S %p') # '%H:%M:%S %p' for 24 hours format
    Label.config(text = string)
    Label.after(1000,time)

# Styling the label widget so that clock will look more attractive
Label = Label(root, font = ("ds-digital",80), background = 'black', foreground = "cyan")
Label.pack(anchor = 'center')
Label.grid(row=2,column=2,pady=15,padx=50)

time()

root.mainloop()