from tkinter import *
import re
import tkinter.messagebox


def validate_only_alpha_and_underscore(char):
    return re.fullmatch(r'^[a-zA-Z_]*$', char) != None


def onClick():
    uname = username.get()
    pswd = password.get()

    if not len(uname) > 0:
        show_popup("Error", "Enter username")
    elif not len(pswd) > 0:
        show_popup("Error", "Enter password")
    elif not validate_only_alpha_and_underscore(uname):
        show_popup("Incorrect username",
                   "Username can only contain alphabets or '_'")
    elif len(pswd) > 8:
        show_popup("Incorrect password",
                   "Password length should be less than 8")
    else:
        show_popup("Success", f"{uname} was logged in!")


def show_popup(title, message):
    tkinter.messagebox.showinfo(title,  message)


tk_window = Tk()
tk_window.geometry('400x150')
tk_window.title('Sign in application using Python tkinter')

Label(tk_window, text="Sign in application using Python tkinter").grid(row=0, column=1)

username_label = Label(tk_window, text="User Name").grid(row=1, column=0)
username = StringVar()
username_entry = Entry(tk_window, textvariable=username).grid(row=1, column=1)

password_label = Label(tk_window, text="Password").grid(row=2, column=0)
password = StringVar()
password_entry = Entry(tk_window, textvariable=password,
                       show='*').grid(row=2, column=1)

login_button = Button(tk_window, command=onClick,
                      text="Login").grid(row=4, column=1)

tk_window.mainloop()