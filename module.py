import tkinter
import string
import re
from tkinter import *
from tkinter import messagebox
import bcrypt

account_list = []

root = Tk()
root.title("Cosmos")
root.geometry("300x500")
icon = PhotoImage(file='planeticon.png')
bg = PhotoImage(file='appbg.png')
root.iconphoto(True, icon)
root.resizable(width=False, height=False)


class Window:
    def __init__(self, master):
        # App Background image
        bg_frame = Frame(master)
        bg_frame.pack()
        self.bg_image = Label(bg_frame,
                              image=bg)
        self.bg_image.pack()

        # Widget Frame
        widget_frame = Frame(master,
                             width=138,
                             height=120)
        widget_frame.place(x=75, y=350)

        # User entry box
        self.user_entry = Entry(widget_frame,
                                width=15,
                                font=("Comic Sans", 11))
        self.user_entry.place(x=7, y=18)
        self.user_label = Label(widget_frame,
                                text="Username",
                                font=("Comic Sans", 7),
                                compound='bottom')
        self.user_label.place(x=10, y=0)

        # Pass enter box
        self.pass_entry = Entry(widget_frame,
                                width=15,
                                font=("Comic Sans", 11),
                                show="*")
        self.pass_entry.place(x=7, y=60)

        self.pass_label = Label(widget_frame,
                                text="Password",
                                font=("Comic Sans", 7))
        self.pass_label.place(x=10, y=41)

        # Register Button
        self.register_button = Button(widget_frame,
                                      text="Register",
                                      font=("Comic Sans", 9),
                                      width=7,
                                      height=1,
                                      command=self.register_click)
        self.register_button.place(x=6, y=88)

        # Login Button
        self.login_button = Button(widget_frame,
                                   text="Login",
                                   font=("Comic Sans", 9),
                                   width=7,
                                   height=1,
                                   command=self.login_click)
        self.login_button.place(x=72, y=88)

    def validate_email(self, user_field):
        regex_check = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(regex_check, user_field):
            return True
        return False

    def blank_field_register_error_msg(self):
        tkinter.messagebox.showinfo(title="We've hit a snag...",
                                    message="Please fill both fields.")

    def invalid_email_error_msg(self):
        tkinter.messagebox.showinfo(title="We've hit a snag...",
                                    message="Please enter a valid email address")

    def check_pass_error_msg(self):
        tkinter.messagebox.showinfo(title="We've hit a snag...",
                                    message="Password must contain an uppercase letter, a number, and a "
                                            "punctuation character.")

    def reg_complete_msg(self):
        tkinter.messagebox.showinfo(title="Registration Complete",
                                    message="Successfully Registered.\nThank you for joining our service!")

    def register_click(self):
        while True:
            user_field = self.user_entry.get()
            password_field = self.pass_entry.get()
            punc_count = 0
            cap_count = 0
            num_count = 0
            if user_field == "" or password_field == "":
                self.blank_field_register_error_msg()
                print(account_list)
                break
            if self.validate_email(user_field) is False:
                self.invalid_email_error_msg()
                break
            for letter in password_field:
                if letter in string.punctuation:
                    punc_count += 1
                if letter.isupper() is True:
                    cap_count += 1
                if letter in "1234567890":
                    num_count += 1
            if punc_count == 0 or cap_count == 0 or num_count == 0:
                self.check_pass_error_msg()
                break
            else:
                self.reg_complete_msg()
                encode = password_field.encode('utf-8')
                hashed = bcrypt.hashpw(encode, bcrypt.gensalt(10))
                account_list.append({user_field: hashed})
                print(account_list)
                break

    def login_click(self):
        print("Clicked login button")


MyWindow = Window(root)
