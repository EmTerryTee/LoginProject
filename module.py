import tkinter
import string
from tkinter import *
from tkinter import messagebox
import bcrypt

global account_list
account_list = []

root = Tk()
root.title("Login Portal")
root.geometry("300x500")
icon = PhotoImage(file='projecticon.png')
root.iconphoto(True, icon)
root.resizable(width=False, height=False)


class Window:
    def __init__(self, master):
        # User entry box
        self.user_entry = Entry(master,
                                font=("Comic Sans", 11))
        self.user_entry.place(x=68, y=345)
        self.user_label = Label(master,
                                text="Username",
                                font=("Comic Sans", 7))
        self.user_label.place(x=68, y=325)

        # Pass enter box
        self.pass_entry = Entry(master,
                                font=("Comic Sans", 11),
                                show="*")
        self.pass_entry.place(x=68, y=385)

        self.pass_label = Label(master,
                                text="Password",
                                font=("Comic Sans", 7))
        self.pass_label.place(x=68, y=367)

        # Register Button
        self.registerbutton = Button(master,
                                     text="Register",
                                     font=("Comic Sans", 9),
                                     command=self.register_click)
        self.registerbutton.place(x=105, y=415)

        # Login Button
        self.loginbutton = Button(master,
                                  text="Login",
                                  font=("Comic Sans", 9),
                                  command=self.login_click)
        self.loginbutton.place(x=105, y=415)

    def blackfieldmsg(self):
        tkinter.messagebox.showinfo(title="We've hit a snag..."
                                    , message="Please fill both fields before logging in.")

    def checkpassmsg(self):
        tkinter.messagebox.showinfo(title="We've hit a snag..."
                                    , message="Password must contain an uppercase letter, a number, and a "
                                              "punctuation character.")

    def regcompletemsg(self):
        tkinter.messagebox.showinfo(title="Registration Complete"
                                    , message="Successfully Registered.\nThank you for joining our service!")

    def register_click(self):
        while True:
            user_field = self.user_entry.get()
            password_field = self.pass_entry.get()
            punc_count = 0
            cap_count = 0
            num_count = 0
            if user_field == "" or password_field == "":
                self.blackfieldmsg()
                print(account_list)
                break
            for letter in password_field:
                if letter in string.punctuation:
                    punc_count += 1
                if letter.isupper() is True:
                    cap_count += 1
                if letter in "1234567890":
                    num_count += 1
            if punc_count == 0 or cap_count == 0 or num_count == 0:
                self.checkpassmsg()
                break
            else:
                self.regcompletemsg()
                encode = password_field.encode('utf-8')
                hashed = bcrypt.hashpw(encode, bcrypt.gensalt(10))
                account_list.append({user_field: hashed})
                print(account_list)
                break

    def login_click(self):
        print("Clicked login button")

MyWindow = Window(root)
