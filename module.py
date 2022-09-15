import tkinter
import string
import re
from tkinter import *
from tkinter import messagebox
import bcrypt

account_list = []

root = Tk()
root.title("Cosmos")
root.geometry("300x300")
icon = PhotoImage(file='planeticon.png')
bg = PhotoImage(file='appbg.png')
entry_bg = PhotoImage(file='entrybg.png')
root.iconphoto(True, icon)
root.resizable(width=False, height=False)


class Window:
    def __init__(self, master):
        # App Background image
        bg_frame = Frame(master)
        bg_frame.pack()
        self.bg_image = Label(bg_frame,
                              image=bg,
                              cursor="dot")
        self.bg_image.pack()

        # Entry & button Frame
        entry_frame = Frame(master,
                            width=138,
                            height=100,
                            cursor="dot")
        entry_frame.place(x=82, y=180)

        self.bglabel = Label(entry_frame,
                             image=entry_bg,
                             bg="#816271")
        self.bglabel.pack()

        # User entry box
        self.user_entry = Entry(entry_frame,
                                width=17,
                                bg='#816271',
                                font=("Consolas", 10),
                                fg="#F6D6BC",
                                relief=FLAT)
        self.user_entry.place(x=9, y=9)


        # Pass enter box
        self.pass_entry = Entry(entry_frame,
                                width=17,
                                bg='#816271',
                                font=("Consolas", 10),
                                show="*",
                                fg="#F6D6BC",
                                relief=FLAT)
        self.pass_entry.place(x=9, y=37)



        # Register Button
        self.register_button = Button(entry_frame,
                                      text="Register",
                                      font=("Consolas", 9),
                                      fg=("#F6D6BC"),
                                      width=7,
                                      height=1,
                                      relief=FLAT,
                                      bg='#816271',
                                      command=self.register_click)
        self.register_button.place(x=9, y=67)

        # Login Button
        self.login_button = Button(entry_frame,
                                   text="Login",
                                   font=("Consolas", 9),
                                   fg=("#F6D6BC"),
                                   width=7,
                                   height=1,
                                   relief=FLAT,
                                   bg='#816271',
                                   command=self.login_click)
        self.login_button.place(x=73, y=67)

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
                print("Need to store this in db somehow", account_list)
                break

    def login_click(self):
        print("Needs to check db somehow")


MyWindow = Window(root)
