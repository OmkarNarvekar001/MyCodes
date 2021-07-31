from tkinter import *
from tkinter import messagebox
import numpy as np
cal = Tk()
cal.geometry("312x324")
cal.resizable(0, 0)
cal.title("Calculator")

def click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def rec():
    global expression
    result=str(np.reciprocal(float(expression)))
    input_text.set(result)
    expression = ""

def aclear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
    except (SyntaxError,ValueError):
        messagebox.showinfo("Error", "Please Enter Valid Syntax")

    input_text.set(result)
    expression = ""


expression = ""

input_text = StringVar()

input_frame = Frame(cal, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

btns_frame = Frame(cal, width=312, height=272, bg="grey")

btns_frame.pack()


seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: click(7)).grid(row=0, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: click(8)).grid(row=0, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: click(9)).grid(row=0, column=2, padx=1, pady=1)

raiseto = Button(btns_frame, text="**", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: click("**")).grid(row=0, column=3, padx=1, pady=1)


four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: click(4)).grid(row=1, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: click(5)).grid(row=1, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: click(6)).grid(row=1, column=2, padx=1, pady=1)

modulus = Button(btns_frame, text="%", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                 command=lambda: click("%")).grid(row=1, column=3, padx=1, pady=1)

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: click(1)).grid(row=2, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: click(2)).grid(row=2, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: click(3)).grid(row=2, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: click("+")).grid(row=2, column=3, padx=1, pady=1)


zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: click(0)).grid(row=3, column=0, padx=1, pady=1)

clear = Button(btns_frame, text="Clear", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: aclear()).grid(row=3, column=1, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: equal()).grid(row=3, column=2, padx=1, pady=1)

reciprocal = Button(btns_frame, text="1/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: rec()).grid(row=3, column=3, padx=1, pady=1)

cal.mainloop()