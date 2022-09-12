import tkinter
import string
from tkinter import *
from tkinter import messagebox
import bcrypt

account_list = []
print(account_list)


def buttonclick():
    while True:
        user_field = user_entry.get()
        password_field = pass_entry.get()
        punc_count = 0
        cap_count = 0
        num_count = 0
        if user_field == "" or password_field == "":
            tkinter.messagebox.showinfo(title="We've hit a snag..."
                                        , message="Please fill both fields before logging in.")
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
            tkinter.messagebox.showinfo(title="We've hit a snag..."
                                        , message="Password must contain an uppercase letter, a number, and a "
                                                  "punctuation character.")
            break
        else:
            tkinter.messagebox.showinfo(title="Registration Complete"
                                        , message="Successfully Registered.\nThank you for joining our service!")
            encode = password_field.encode('utf-8')
            hashed = bcrypt.hashpw(encode, bcrypt.gensalt(10))
            account_list.append({user_field: hashed})
            print(account_list)
            break


window = Tk()  # Instantiate an instance of a window
window.geometry("400x600")  # Defining the windows size
window.title("Login Portal")

user_entry = Entry(window,
                   font=("Comic Sans", 12))
pass_entry = Entry(window,
                   font=("Comic Sans", 12))

icon = PhotoImage(file='projecticon.png')
window.iconphoto(True, icon)
loginButton = Button(window,
                     command=buttonclick,  # This is the function called when button is clicked
                     text="Click to register",
                     font=("Comic Sans", 12),
                     fg="#000000")

user_entry.pack()
pass_entry.pack()
loginButton.pack()

window.mainloop()  # This will display a window and act as an event listener
