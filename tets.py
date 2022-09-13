import tkinter
import string
from tkinter import *
from tkinter import messagebox
import bcrypt

win = Tk()
win.geometry("300x500")

imageframe = Frame(win)

bg = PhotoImage(file="appbg.png")

bglabel = Label(imageframe,
                image=bg)
bglabel.pack()
imageframe.pack()
widgetframe = Frame(win,
                    width=100,
                    height=100,
                    bd=10,
                    relief=RAISED)
widgetframe.place(x=100,y=370)

mytext = Label(widgetframe,
               text="Text")
mytext.place(x=0,y=0)

myfield = Entry(widgetframe)
myfield.place(x=0,y=70)



win.mainloop()