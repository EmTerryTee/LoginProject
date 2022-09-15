import tkinter
import string
import re
from tkinter import *
from tkinter import messagebox
import bcrypt

win = Tk()
win.title("Test Window")
win.geometry("300x300")

widgetframe = Frame(win,
                    bd = 10,
                    relief=FLAT,
                    background="black"
                    )


widgetframe.place(x=120,y=100)

text = Canvas(widgetframe, height=100, width=100)
text.create_text((20,20), text="Hello douchebag")
text.pack()

entry = Entry(widgetframe)
entry.place(x=0, y=27)

mainloop()
