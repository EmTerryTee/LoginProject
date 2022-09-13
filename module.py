import tkinter
import string
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
        bg_frame.grid(row=0, column=0)
        self.bg_image = Label(bg_frame,
                              image=bg)
        self.bg_image.grid(row=0, column=0)

        # Widget Frame
        widget_frame = Frame(master)
        widget_frame.grid(row=1, column=0)

        # User entry box
        self.user_entry = Entry(widget_frame,
                                font=("Comic Sans", 11))
        self.user_entry.grid(row=1,column=2)
        self.user_label = Label(widget_frame,
                                text="Username",
                                font=("Comic Sans", 7),
                                compound='bottom')
        self.user_label.grid(row=1,column=1)

        # Pass enter box
        self.pass_entry = Entry(widget_frame,
                                font=("Comic Sans", 11),
                                show="*")
        self.pass_entry.grid(row=2,column=2)

        self.pass_label = Label(widget_frame,
                                text="Password",
                                font=("Comic Sans", 7))
        self.pass_label.grid(row=2,column=1)

        # Register Button
        self.register_button = Button(widget_frame,
                                      text="Register",
                                      font=("Comic Sans", 9),
                                      width=9,
                                      height=1,
                                      command=self.register_click)
        self.register_button.grid(row=3,column=1)

        # Login Button
        self.login_button = Button(widget_frame,
                                   text="Login",
                                   font=("Comic Sans", 9),
                                   width=9,
                                   height=1,
                                   command=self.login_click)
        self.login_button.grid(row=3,column=2)

    def blank_field_register_msg(self):
        tkinter.messagebox.showinfo(title="We've hit a snag..."
                                    , message="Please fill both fields.")

    def check_pass_msg(self):
        tkinter.messagebox.showinfo(title="We've hit a snag..."
                                    , message="Password must contain an uppercase letter, a number, and a "
                                              "punctuation character.")

    def reg_complete_msg(self):
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
                self.blank_field_register_msg()
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
                self.check_pass_msg()
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
