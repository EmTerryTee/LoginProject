from tkinter import font
from tkinter import *


win = Tk()
win.title("Test Window")
win.geometry("300x300")

wf = Frame(win,
           bd=10,
           relief=FLAT,
           background="black")
wf.place(x=120, y=100)

txt = Canvas(wf, height=10, width=20)
txt.create_text((20, 20), text="Hello")
txt.pack()

entry = Entry(wf)
entry.place(x=0, y=27)

cnt = 0
for i in font.families():
    if i == "Consolas":
        cnt += 1
if cnt == 0:
    print("Not found")
else:
    print("Found")
