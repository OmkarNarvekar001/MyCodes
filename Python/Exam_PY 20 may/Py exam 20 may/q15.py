import tkinter 
from tkinter import* 
import sqlite3 
try: 
    con=sqlite3.connect('contact.db') 
    con.execute("create table contacts(cname,cno)") 
    con.commit() 
except sqlite3.OperationalError: 
    pass 
 
contacts_list = [] 
 
def addNewContact(): 
    window = tkinter.Tk() 
    window.title("Contacts Directory") 
    window.geometry("600x400") 