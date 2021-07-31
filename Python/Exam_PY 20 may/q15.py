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

    namelbl = tkinter.Label(window, text="Enter the contact name: ")
    namelbl.place(x=40, y=90)
    nametxt = tkinter.Entry(window, width=20)
    nametxt.place(x=230, y=90)

    numlbl = tkinter.Label(window, text = "Enter the contact number: ")
    numlbl.place( x = 40, y = 40)
    numtxt = tkinter.Entry(window, width=20)
    numtxt.place( x=230, y= 40)
 
    savebtn1 = tkinter.Button(window, text="Add", command=lambda:saveContact(nametxt.get(), numtxt.get()))
    savebtn1.place(x=300, y = 300)
    window.mainloop()
 
def saveContact(namelbl,numlbl):
    con.execute("INSERT INTO contacts Values (?,?)",(namelbl,numlbl))
    con.commit()
    contacts_list.append([namelbl,numlbl])
    print("New contact added successfully")
    
def displayContacts():
    window = tkinter.Tk()
    r_set=con.execute('Select * from contacts')
    i=0
    for b in r_set:
        for j in range(len(b)):
            e=Entry(window,width=30,fg='black')
            e.grid(row=i,column=j)
            e.insert(END,b[j])
        i=i+1
    window.title("Contact Application")
    window.geometry("600x400")
    window.mainloop()
 
def updateContact():
    window = tkinter.Tk()
    
    window.title("Contact Application")
    window.geometry("600x400")
 
    nballbl = tkinter.Label(window, text="Enter the name: ")
    nballbl.place(x=40, y=40)
    nbaltxt = tkinter.Entry(window, width=20)
    nbaltxt.place(x=230, y=40)

    numlbl = tkinter.Label(window, text = "Enter the contact number:")
    numlbl.place( x = 40, y = 170)
    numtxt = tkinter.Entry(window, width=20)
    numtxt.place( x=230, y= 170)
    no=numtxt.get()
 
    savebtn=tkinter.Button(window, text="Update", command=lambda:updateName(nbaltxt.get(),numtxt.get()))
    savebtn.place(x=300, y = 300)
    window.mainloop()

def updateName(nb,no):
    con.execute('Update contacts set cno=? where cname=? ',(no,nb))
    con.commit()
    print("Contact updated successfully")

def deleteContact():
    window = tkinter.Tk()
    
    window.title("Contact Application")
    window.geometry("600x400")
 
    nbllbl = tkinter.Label(window, text="Enter the name: ")
    nbllbl.place(x=40, y=170)
    nbltxt = tkinter.Entry(window, width=20)
    nbltxt.place(x=230, y=170)
 
    savebtn2=tkinter.Button(window, text="Delete", command=lambda:dContact(nbltxt.get()))
    savebtn2.place(x=300, y = 300)
    window.mainloop()

def dContact(nb):
    con.execute('Delete from contacts where cname=? ',(nb,))
    con.commit()
    print("Contact deleted successfully")

def displaySpecificContact():
    window = tkinter.Tk()
    
    window.title("Contact Application")
    window.geometry("600x400")
 
    nballbl1 = tkinter.Label(window, text="Enter the name: ")
    nballbl1.place(x=40, y=40)
    nbaltxt1 = tkinter.Entry(window, width=20)
    nbaltxt1.place(x=230, y=40)

    savebtn3=tkinter.Button(window, text="Display", command=lambda:disName(nbaltxt1.get()))
    savebtn3.place(x=300, y = 300)
    window.mainloop()

def disName(nm):
    window = tkinter.Tk()
    r_set=con.execute(' Select * from contacts where cname=?',(nm,))
    i=0
    for b in r_set:
        for j in range(len(b)):
            e=Entry(window,width=30,fg='black')
            e.grid(row=i,column=j)
            e.insert(END,b[j])
        i=i+1
    window.title("Contact Application")
    window.geometry("600x400")
    window.mainloop()

def main():
    window = tkinter.Tk()
    savebtn = tkinter.Button(window, text="Add",height=3,width=10, command=lambda:addNewContact())
    savebtn.place(x=100, y = 200)
 
    displaybtn = tkinter.Button(window, text="Display",height=3,width=10, command= lambda:displayContacts())
    displaybtn.place(x=250, y=200)
 
    updatebtn = tkinter.Button(window, text="Update",height=3,width=10, command= lambda:updateContact())
    updatebtn.place(x=400, y=200)

    deletebtn = tkinter.Button(window, text="Delete",height=3,width=10, command= lambda:deleteContact())
    deletebtn.place(x=550, y=200)

    deletebtn = tkinter.Button(window, text="Display specific",height=3,width=15, command= lambda:displaySpecificContact())
    deletebtn.place(x=700, y=200)
 
    window.title("Contact Application")
    window.geometry("300x300")
    window.mainloop()
 
if __name__ == "__main__":
    main()