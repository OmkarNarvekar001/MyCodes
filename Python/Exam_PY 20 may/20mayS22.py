# Problem stat 6 of 20 may batch
# Create a “Library” module having class Book containing book id, name, author and cost.
# Write a python program to access the given module, save all the details as a dictionary {bid:[name, author, cost]}
# and show a command-line menu through which following can be performed
# a. Add a new book
# b. Update cost of any book
# c. Delete a book
# d. Display details of all the books.
# e. Compare which book is costlier by using operator overloading


books = {}
class Book:
    def __init__(self, id, name, author, price, quantitiy):
        self.id = id
        self.name = name
        self.author = author
        self.price = price
        self.quantity = quantitiy

    def __ge__(self, mrp):
        if (self.price >= mrp.price):
            return "Book1's price is greater than equal to Book2's price"
        else:
            return "Book2's price is greater than  Book1's price"

    def update_book(self, name):
        for i in books:
            if books[i].name == name:
                name_new = input("Enter updated name for book: ")
                price_new = int(input("Enter updated price: "))
                books[i].name = name_new
                books[i].price = price_new
                print(f"{books[i].name} is updated")
                break
        return

def add_new_book():
    global books
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    i = len(books) + 1
    books[i]=Book(i, name, author, price, quantity)


def delete_book():
    global books
    print_book()

    name1 = input("Enter title of book to delete: ")
    x=-1
    for i in books:
        if books[i].name == name1:
            x=i
    if x in books:
        del books[x]
        print("book deleted")
    else:
        print("invalid")


def print_book():
    # print(books)
    for i in books:
        print("Name: "+books[i].name)
        print("Author: "+books[i].author)
        print("Price: "+str(books[i].price))
        print("Quantity: "+str(books[i].quantity))
        print()

def costlier():
    print_book()

    name1 = input("Enter title of first book : ")
    name2 = input("Enter title of second book : ")
    ob1, ob2 = "", ""

    for i in (books):
        if books[i].name == name1:
            ob1 = Book(books[i].id, books[i].name,books[i].author, books[i].price, books[i].quantity)
        if books[i].name == name2:
            ob2 = Book(books[i].id, books[i].name,books[i].author, books[i].price, books[i].quantity)

            break
    print(ob1 >= ob2)


choice = 0
while choice != 10:
    print()
    print("1. Add a new book")
    print("2. Update cost of a book")
    print("3. Delete a book")
    print("4. Display details of all books")
    print("5. Compare books using operator overlaoding")
    print("6. To exit")
    choice = int(input("Enter you choice: "))
    print("-----------------------------------------")

    if choice == 1:
        add_new_book()

    elif choice == 2:

        name = input("Enter title of book to update: ")
        for i in books:
            if books[i].name == name:
                ob1 = Book(books[i].id, books[i].name,
                       books[i].author, books[i].price, books[i].quantity)

        ob1.update_book(name)

    elif choice == 3:
        delete_book()

    elif choice == 4:
        print_book()

    elif choice == 5:
        costlier()

    elif choice == 6:
        print("Thank you")
        break
    else:
        print("Invalid number try again")


# Problem stat 18 of 20 may
# Write a python command-line menu program to generate following five different built-in exceptions and print appropriate message while handling them.
# a. TypeError
# b. ValueError
# c. ImportError
# d. ZeroDivisionError
# e. NameError

# def main():
#     while True:
#         print("Menu")
#         print("*******")
#         print("1.Type Error ")
#         print("2.Value Error ")
#         print("3.Import Error ")
#         print("4.Zero Division ")
#         print("5.Name Error ")
#         print("6.Exit ")
#         print("*******")
#
#
#         ch = int(input("Enter your choice: "))
#
#         if ch == 1:
#             print("For Type Error")
#
#             try:
#                 x = int(input("Please enter a number: "))
#                 print("Adding string to x")
#                 print(x+"abc")
#                 print("No error detected")
#             except TypeError:
#                 print("Type error detected")
#
#
#
#         elif ch == 2:
#             print("For Value Error")
#             try:
#                 x = int(input("Please enter a number: "))
#                 print("No error detected")
#
#             except ValueError:
#                 print("Value error detected")
#
#
#         elif ch == 3:
#             print("For Import Error")
#             try:
#                 import sqlite3
#                 print("sqlite3 Imported sucessfully")
#                 import numpie
#                 print("numpy Imported sucessfully")
#             except ImportError :
#                 print("Import Error detected")
#
#         elif ch == 4:
#             print("For Zero Division")
#             try:
#                 a = int(input("Enter a: "))
#                 b = int(input("Enter b: "))
#                 c = a / b
#                 print("a/b = ", c)
#             except ZeroDivisionError:
#                 print("Zero Division Error detected")
#
#
#         elif ch == 5:
#             print("For Name Error")
#
#             def err():
#                 try:
#                     print("Define A")
#                     A = "hello"
#                     return B
#                 except NameError:
#                     return "Name error detected"
#
#             print(err())
#
#
#         elif ch == 6:
#             print("EXIT")
#             break
#
# if __name__ == "__main__":
#     main()


# Problem stat 13 of 20 may
# Write a python program to create the given GUI for sign application. The program should accept username and password and
# verify the correctness as per given conditions. If they do not met the conditions, generate appropriate error message using proper Error handling mechanism else show sign in successful through popup dialog.
# a. Username should have only characters (A-Z,a-z) and can have only underscore as special character.
# b. Password should not be more than 8 characters long.


# from tkinter import *
# import re
# import tkinter.messagebox
#
#
# def validate_only_alpha_and_underscore(char):
#     return re.fullmatch(r'^[a-zA-Z_]*$', char) != None
#
#
# def onClick():
#     uname = username.get()
#     pswd = password.get()
#
#     if not len(uname) > 0:
#         show_popup("Error", "Enter username")
#     elif not len(pswd) > 0:
#         show_popup("Error", "Enter password")
#     elif not validate_only_alpha_and_underscore(uname):
#         show_popup("Incorrect username",
#                    "Username can only contain alphabets or '_'")
#     elif len(pswd) > 8:
#         show_popup("Incorrect password",
#                    "Password length should be less than 8")
#     else:
#         show_popup("Success", f"{uname} was logged in!")
#
#
# def show_popup(title, message):
#     tkinter.messagebox.showinfo(title,  message)
#
#
# tk_window = Tk()
# tk_window.geometry('400x150')
# tk_window.title('Sign in application using Python tkinter')
#
# Label(tk_window, text="Sign in application using Python tkinter").grid(
#     row=0, column=1)
#
# username_label = Label(tk_window, text="User Name").grid(row=1, column=0)
# username = StringVar()
# username_entry = Entry(tk_window, textvariable=username).grid(row=1, column=1)
#
# password_label = Label(tk_window, text="Password").grid(row=2, column=0)
# password = StringVar()
# password_entry = Entry(tk_window, textvariable=password,
#                        show='*').grid(row=2, column=1)
#
# login_button = Button(tk_window, command=onClick,
#                       text="Login").grid(row=4, column=1)
#
# tk_window.mainloop()


# Problem stat 9 of 20 may
# Create a “stationary” database using sqlite3 containing a table “product” having product id, name, unit price and category (notebooks, pencil, pen).
# Write a python program to show a command-line menu through which data can be added to the database and data can be read and displayed from the database.

# import sqlite3
# print("Database connection successful")
# stationarycount = 1
# def insertIntoDB(id, name, category, price):
#     conn = sqlite3.connect("test.db")
#     conn.execute(
#         f"Insert into stationary (id, name, category, price) values({id}, '{name}', '{category}', {price})",
#     )
#     conn.commit()
#     print("Row Inserted successfully")
#     conn.close()
#
#
# def add_new_stationary():
#     global stationarycount
#     name = input("Enter company name: ")
#     category = input("Enter category name: ")
#     price = int(input("Enter price: "))
#     id = stationarycount
#     insertIntoDB(id, name, category, price)
#     stationarycount += 1
#
#
#
# def print_stationary():
#     conn = sqlite3.connect("test.db")
#     cur = conn.execute("Select * from stationary")
#     for row in cur:
#         print(f"Stationary id number: {row[0]}")
#         print(f"Stationary Company name: {row[1]}")
#         print(f"Stationary Category: {row[2]}")
#         print(f"Stationary price: {row[3]}")
#         print("")
#
#
# choice = 0
# while choice != 3:
#     print()
#     print("1. Add stationary")
#     print("2. Print all stationaries")
#     print("3. to exit")
#     choice = int(input("Enter your choice: "))
#     print("-----------------------------------------")
#
#     if choice == 1:
#         add_new_stationary()
#     elif choice == 2:
#         print_stationary()
#     elif choice == 3:
#         print("Thank you!!!")
#     else:
#         print("Invalid number try again")


# Problem stat 5 of 20 may
# Create a class Vehicle having vehicle no, name, and company as data members. Create two subclasses Car and Bike from
# the vehicle class having price as the data member. Write a python program to access the
# given classes, save all the details as a list { vehicle no, name, company and price } and
# show a command-line menu through which following can be performed. Include appropriate constructors.
# a. Add a new Car and Bike objects
# b. Update price of any Car or Bike
# c. Delete a Car or Bike
# d. Display details of all Car and Bike.

# list1 = []
#
# class Vehicle:
#     def _init_(self, veh_no, name, company, price):
#         self.veh_no = veh_no
#         self.name = name
#         self.company = company
#         self.price = price
#
# def add_car_bike():
#     name = input("Enter Vehicle name: ")
#     veh_no = int(input("Enter Vehicle no: "))
#     company = input("Enter company of car: ")
#     price = int(input("Enter price: "))
#     list1.append(Vehicle(veh_no, name, company, price))
#
#
# def display():
#     ac = int(input("Enter the Vehicle no to be displayed: "))
#     for x in list1:
#         if x.veh_no == ac:
#             print(f" Vehicle Name: {x.name}\n")
#             print(f" Vehicle No: {x.veh_no}\n")
#             print(f" Company: {x.company}\n")
#             print(f" Price: {x.price}\n")
#
#
# def update():
#     ac = int(input("Enter the Vehicle no of which price to be update: "))
#     for x in list1:
#         if x.veh_no == ac:
#             # self.price = pr
#             pr = int(input("Enter Updated Price: "))
#             x.price = pr
#             print("Updated price is : ", pr)
#         else:
#             print("No data found")
#
#
# def delete():
#     ac = int(input("Enter the vehicle no: "))
#     for x in list1:
#         if x.veh_no == ac:
#             list1.remove(x)
#         print("Deleted")
#
#
# class Car(Vehicle):
#     def init(self, veh_no, name, company, price):
#         Vehicle.init(self, veh_no, name, company, price)
#
#     def car(self):
#         for i in list1:
#             if i.type == "car":
#                 print("-----------------------------------------------------")
#                 print(f" Price IS:{i.price}\n")
#                 print(f" NAME IS: {i.name}\n")
#                 print(f" Company {i.company}\n")
#                 print("-----------------------------------------------------")
#
#             else:
#                 print("-----------------------------------------------------")
#                 print("No Data Found")
#                 print("-----------------------------------------------------")
#
#
# class Bike(Vehicle):
#     def init(self, veh_no, name, company, price):
#         Vehicle.init(self, veh_no, name, company, price)
#
#     def bike(self):
#         for i in list1:
#             if i.type == "Bike":
#                 print("-----------------------------------------------------")
#                 print(f" Price IS:{i.price}\n")
#                 print(f" NAME IS: {i.name}\n")
#                 print(f" Company {i.company}\n")
#                 print("-----------------------------------------------------")
#
#             else:
#                 print("-----------------------------------------------------")
#                 print("No Data Found")
#                 print("-----------------------------------------------------")
#
#
# def main():
#     while True:
#         print("1. Add new Vehicle")
#         print("2. Update price")
#         print("3. To display mentioned vehicle details")
#         print("4. Delete vehicle")
#         print("5. Quit")
#
#         ch = int(input("Enter your choice: "))
#
#         if ch == 1:
#             add_car_bike()
#
#         elif ch == 2:
#             update()
#         elif ch == 3:
#             display()
#         elif ch == 4:
#             delete()
#         elif ch == 5:
#             print(" Bye! Have a good day!")
#             break
#
#
# if __name__ == "__main__":
#     main()



# Problem stat 7 of 20 may
# Create a “SEIT” module having class Student containing student roll no, name, and marks for 3 subjects (Java, C++, Python).
# Write a python program to access the given module, save all the details as a dictionary {rollno:[name, m1, m2, m3]}
# and show a command-line menu through which following can be performed
#  a. Add a new student
#  b. Update marks of any subject
#  c. Delete a student
#  d. Display details of all the students.

# MODULE
# class Student():
#   student = {}
#   def __init__(self,  rollno, name, java, cpp, python):
#     self.rollno = rollno
#     self.name = name
#     self.java = java
#     self.cpp = cpp
#     self.python = python
#     self.dictionary()
#
#   def dictionary(self):
#     lis = []
#     lis.append(self.name)
#     lis.append(self.java)
#     lis.append(self.cpp)
#     lis.append(self.python)
#     self.student[self.rollno] = lis

# Program
# from SEIT import Student
#
#
# def add_new_student():
#     name = input("Enter Student Name: ")
#     rollno = int(input("Enter Student Rollno: "))
#     java = int(input("Enter Java Marks: "))
#     cpp = int(input("Enter C++ Marks: "))
#     python = int(input("Enter Python Marks: "))
#     Student(rollno, name, java, cpp, python)
#
#
# def display():
#     if (len(Student.student) == 0):
#         print("Student Records Empty")
#     for i in Student.student:
#         print("Roll Num: {} | Name: {} | JAVA: {} | CPP: {} | PYTHON: {}\n".format(i, Student.student[i][0],
#                                                                                    Student.student[i][1],
#                                                                                    Student.student[i][2],
#                                                                                    Student.student[i][3]))
#
#
# def update_student():
#     roll = int(input("Enter the roll no: "))
#     for i in Student.student:
#         if i == roll:
#             java_m = int(input("Enter the update JAVA marks"))
#             cpp_m = int(input("Enter the update CPP marks"))
#             py_m = int(input("Enter the update PYTHON marks"))
#             Student.student[i][1] = java_m
#             Student.student[i][2] = cpp_m
#             Student.student[i][3] = py_m
#             print(f"Roll No. {i} marks is updated")
#             break
#
#
# def delete_student():
#     roll = int(input("Enter the roll no to delete: "))
#     for i in Student.student:
#         if i == roll:
#             del Student.student[i]
#             print(f"Roll No. {i} marks was removed")
#             break
#
#
# choice = 0
# while choice != 5:
#     print()
#     print("1. Add a New Student")
#     print("2. Update marks of any student")
#     print("3. Delete a Student")
#     print("4. Display Student")
#     print("5. to exit")
#     choice = int(input("Enter you choice: "))
#     print("-----------------------------------------")
#
#     if choice == 1:
#         add_new_student()
#     elif choice == 2:
#         update_student()
#     elif choice == 3:
#         delete_student()
#
#     elif choice == 4:
#         display()
#
#     elif choice == 5:
#         print("Thank you")
#     else:
#         print("Invalid number try again")


# Problem stat 19 of 20 may

# Solve the following equations to print the values of x, y
# and z:

# 1a. 3x + 2y = 1; x –y= 2
# import numpy as np
# from scipy import linalg
# A=np.array([[3,2],[1,-1]])
# B = np.array([ [1, 2] ])
# B=B.T
# X=linalg.solve(A,B)
# print("x=",int(X[0]),"and y=",int(X[1]))

# 1b. X + 3y + 10z = 10
# 2x + 12y + 7z = 18
# 5x + 8y + 3z = 30
# import numpy as np
# from scipy import linalg
# A=np.array([[1,3,10],[2, 12, 7],[5, 8, 3]])
# B=np.array([[10, 18, 30]])
# B=B.T
# X=linalg.solve(A,B)
# print("x = ",int(X[0]),"and y = ",int(X[1])," and z = ",int(X[2]))

# 2a.
# print the determinant of the given matrices:
# import numpy as np
# n_array = np.array([[-6, -8], [4, 4]])
# print("Numpy Matrix is:")
# print(n_array)
# det = np.linalg.det(n_array)
# print("\nDeterminant of given 2X2 matrix:")
# print(int(det))

# 2b.
# import numpy as np
# n_array = np.array([[3, 0, 1], [4, 1, -2], [2, -2, 1]])
# print("Numpy Matrix is:")
# print(n_array)
# det = np.linalg.det(n_array)
# print("\nDeterminant of given 2X2 matrix:")
# print(int(det))


# Problem stat 16
# Write a python program for the following:
# a. Create a parent class Circle. Initialize the constructor with the radius of the circle.
# Define the method getradius and calc_area to get the radius and area of the circle.
# b. Create a child class cylinder from the the circle class.
# Initialize the value of the height within the constructor and call the constructor of the parent class
# to initialize the radius of the cylinder. Define the method calc_area to get the area of cylinder (area = 2*pi*radius* height)
# c. Create both the circle and cylinder objects and print the areas.

# import math
# class Circle:
#     def _init_(self, radius):
#         self.radius = radius
#
#     def getradius(self):
#         return self.radius
#
#     def calc_area(self):
#         return math.pi * (self.radius ** 2)
#
#
# class cylinder(Circle):
#     def _init_(self, height, radius):
#         super()._init_(radius)
#         self.height = height
#
#     def cal_area(self):
#         return 2 * math.pi * self.radius * self.height
#
#
# a = Circle(3)
# print("Area of circle is : ", a.calc_area())
# b = cylinder(4, 3)
# print("Area of cylinder is : ", b.calc_area())


# Problem stat 4 of 20 may
# Write a python program to implement a stack class. The class uses list to store all data. The class should have following methods:
# a. Constructor – to initialize the data when a new stack is created.
# b. Push – to add data element in the stack
# c. Pop – to delete data element from stack
# d. Count – to return the number of elements in the stack
# e. Display(pos = -1) – to print elements from stack given the index position. The method contains index position as default argument,
# when no position is given during call -1 is the default value which prints all the elements else print the element at the given index.
# Display appropriate user defined exception if index value is not proper.

# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#         print(self.items)
#
#     def push(self, item):
#         self.items.insert(0,item)
#         print(self.items)
#
#     def pop(self):
#         self.items.pop(0)
#         print(self.items)
#
#     def display(self, item):
#         print(self.items)
#         i=0
#         for i in range (len(self.items)):
#             if self.items[i] == item:
#                 print("the pos of",self.items[i],"is ", i+1)
#         print("Element not found")
#
#
#     def size(self):
#         print("The number of element is stack is :")
#         print(len(self.items))
#         print(self.items)
#
# st = Stack()
#
# while True:
#     print("Stack operations: ")
#     print("1]Push a number")
#     print("2]Pop a number")
#     print("3]Print the list.")
#     print("4]Count number of elements.")
#     choice = int(input("Enter your choice:"))
#     if choice == 1:
#         x = int(input("\nPush number: "))
#         st.push(x)
#         # print the stack.
#     elif choice == 2:
#         y = print("\n Last element is pop from list")
#         st.pop()
#         # print the stack.
#     elif choice == 3:
#         # print the stack
#         z = int(input("Enter the position of the element to display"))
#         st.display(z)
#     elif choice == 4:
#         print("\nNumber of elements present are: ")
#         # count of the stack.
#         st.size()
#         break
#     else:
#         print("\nWrong choice.")



# Problem stat 17 of 20 may
# Create an interface shape. Initialize the value of color within the constructor. Create a subclass Rectangle
# which inherits the propeties of the shape class. Initialize the attribute length and breadth in the constructor
# and call the parent class constructor to initialize color. Add calc_area method to get the area of the rectangle.
# Create a subclass Triangle which inherits the propeties of the shape class. Initialize the attribute length and height
# in the constructor and call the parent class constructor to initialize color. Add calc_area method to get the area of the triangle.
# With the python program to create object of rectangle and triangle and print the area of rectangle and triangle

# Creating a shape Class
# class Shape:
#     width = 0
#     height = 0
#
#     # Creating area method
#     def area(self):
#         print("Parent class Area ... ")

# Creating a Rectangle Class
# class Rectangle(Shape):
#
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     # Overridding area method
#     def area(self):
#         print("Area of the Rectangle is : ", self.width * self.height)
#
#
# # Creating a Triangle Class
# class Triangle(Shape):
#
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     # Overridding area method
#     def area(self):
#         print("Area of the Triangle is : ", (self.width * self.height) / 2)
#
#
# rectangle = Rectangle(10, 20)
# triangle = Triangle(2, 10)
#
# rectangle.area()
# triangle.area()


# Problem stat 1 of 20 may
# Write a function in Python to read lines from a text file "notes.txt". For example: If the content of the file is:
# "India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a" \
# " great market. Most of the Indians can foresee the heights that India is capable of reaching."
# a. Word_frequency to display the frequency of occurrence of any user defined word.
# b. display_words to read lines from a text file, and display those words, which are less than 4 characters.
# c. Count_words to display the total number of words in a text file.
# d. Convert_upper to convert and display the text file as uppercase character
# notes.txt:
# India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a" \
# # " great market. Most of the Indians can foresee the heights that India is capable of reaching."

# file = open("notes.txt", "rt")
# data = file.read()
# def word_frequency():
#     words = data.split()
#     user = input("Enter a string to find the frequency: ")
#     print("The frequency of {} is {}".format(user, words.count(user)))
#
# def display_words():
#     word = data.split()
#     for w in word:
#         if len(w) < 4:
#             print(w, end=" ")
#             print("")
#
# def count_words():
#     words = data.split()
#     print("Number of words in text file :", len(words))
#
# def convert_upper():
#     new = data.upper()
#     print(new)
#     choice = 0
#
# while choice != 5:
#     print("-------------------------------------------------")
#     print("\nSelect one option : ")
#     print(" 1. Find the frequency of a given word\n 2. Display the words having length less than 4 letters\n"
#           " 3. Count the total number of words in the text file\n 4. Convert the text to upper case and print\n 5. Exit")
#     print("\n-------------------------------------------------")
#     choice = int(input("Your Choice: "))
#     if choice == 1:
#         word_frequency()
#     elif choice == 2:
#         display_words()
#     elif choice == 3:
#         count_words()
#     elif choice == 4:
#         convert_upper()
#     elif choice == 5:
#         exit()
#     else:
#         print("No such input exists")


# Problem stat 2 20 may
# Write a python program to implement a Queue class. The class uses list to store all data. The class should have following methods:
# a. Constructor – to initialize the data when a new queue is created.
# b. Push – to add data element in the queue
# c. Pop – to delete data element from queue
# d. Count – to return the number of elements in the queue
# e. Display(pos = -1) – to print elements from queue given the index position. The method contains index position as
# default argument, when no position is given during call -1 is the default value which prints all the elements else
# print the element at the given index. Display appropriate user defined exception if index value is not proper.

# class Queue:
#
#     def __init__(self):
#         self.lst = []
#
#     def push(self, x, count):
#         self.lst.append(x)
#         count += 1
#         print(f"\n{x} PUSHED\n")
#         return count
#
#     def pop(self, count):
#         if (count == 0):
#             print("\nLIST IS EMPTY\n")
#             return count
#
#         x = self.lst[0]
#         self.lst.pop(0)
#         count -= 1
#         print(f"\n{x} POPPED\n")
#         return count
#
#     def count(self, count):
#         print(f"\nTHERE ARE {count} NUMBERS PRESENT IN LIST\n")
#         return
#
#     def display(self, pos, count):
#         if (count == 0):
#             print("\nLIST IS EMPTY\n")
#             return
#
#         try:
#             if (pos == -1):
#                 print("\nQUEUE:\n")
#                 for i in range(count):
#                     print(f"\t{self.lst[i]}")
#                 print("\n")
#                 return
#
#             else:
#                 print(f"\nELEMENT AT POSITION {pos} IS {self.lst[pos]}\n")
#                 return
#
#         except IndexError:
#             print(f"\nENTER VALID INDEX.\nONLY {count} ELEMENTS ARE PRESENT IN LIST\n")
#             return
#
#
# def main():
#     choice = 0
#     queue1 = Queue()
#     count = 0
#
#     print("\nWELCOME")
#
#     while (choice != 5):
#
#         print("\nMENU:")
#         print("1. PUSH\n2. POP\n3. COUNT\n4. DISPLAY\n5. EXIT")
#         choice = int(input("\nSELECT AN OPTION: "))
#
#         if (choice == 1):
#             x = int(input("\nENTER THE NUMBER YOU WANT TO PUSH: "))
#             count = queue1.push(x, count)
#
#         elif (choice == 2):
#             count = queue1.pop(count)
#
#         elif (choice == 3):
#             queue1.count(count)
#
#         elif (choice == 4):
#             x = int(input("\nENTER THE INDEX: "))
#             queue1.display(x, count)
#
#         elif (choice == 5):
#             print("\nTHANK YOU\n")
#             break
#
#         else:
#             print("\nINVALID INPUT\n")
#
#
# if __name__ == '__main__':
#     main()


# Problem stat 3 of 20 may
# Create a “Inventory” class having product ID, name, manufacturer and price along with required constructor. Write a python
# program that saves all objects into a data file and reads from the data file and show a command-line menu through which following can be performed
# a. Add a new student
# b. Update marks of any subject
# c. Delete a student
# d. Display details of all the students.

# import pickle
# class Inventory:
#     def __init__(self, id, name, manufacturer, price):
#         self.id = id
#         self.name = name
#         self.manufacturer = manufacturer
#         self.price = price
#
# def add_new_product():
#     name = input("Enter name: ")
#     manufacturer = input("Enter manufacturer name: ")
#     with open('bank.dat', 'rb') as bank:
#         products = list(pickle.load(bank))
#     price = int(input("Enter price: "))
#     id = len(products) + 1
#     products.append(Inventory(id, name, manufacturer, price))
#     with open('bank.dat', 'wb')as bank:
#         pickle.dump(products, bank)
#         bank.close()
#
#
# def update_price():
#     display_product()
#     list1 = []
#     name = input("Enter name to update: ")
#     with open('bank.dat', 'rb') as bank:
#         list1 = pickle.load(bank)
#         bank.close()
#     for index, product in enumerate(list1):
#         if product.name == name:
#             name_new = input("Enter updated name: ")
#             price_new = int(input("Enter updated price: "))
#             list1[index] = Inventory(product.id, name_new, product.manufacturer, price_new)
#             print(f"{product.name} is updated")
#             break
#     with open('bank.dat', 'wb')as bank:
#         pickle.dump(list1, bank)
#         bank.close()
#
#
# def delete_product():
#     display_product()
#     name = input("Enter product name to delete: ")
#     p = []
#     with open('bank.dat', 'rb') as bank:
#         p = list(pickle.load(bank))
#     for product in p:
#         if product.name == name:
#             p.remove(product)
#             print(f"{product.name} was removed")
#     with open('bank.dat', 'wb')as bank:
#         pickle.dump(p, bank)
#         bank.close()
#
#
# def display_product():
#     p = []
#
#     with open('bank.dat', 'rb') as bank:
#         p = list(pickle.load(bank))
#     for counter, product in enumerate(p):
#         print(f"{counter + 1}. {product.name} by {product.manufacturer} at {product.price}")
#
# with open('bank.dat', 'wb') as bank:
#     pickle.dump([], bank)
# choice = 0
# while choice != 5:
#     print()
#     print("1. Add new product")
#     print("2. delete product")
#     print("3. display all products")
#     print("4. Update price")
#     print("5. to exit")
#     choice = int(input("Enter you choice: "))
#     print("-----------------------------------------")
#     if choice == 1:
#         add_new_product()
#     elif choice == 2:
#         delete_product()
#     elif choice == 3:
#         display_product()
#     elif choice == 4:
#         update_price()
#     elif choice == 5:
#         print("Thank you")
#     else:
#         print("Invalid number try again")


# Problem stat 10 of 20 may
# Create a “student” database using sqlite3 containing a table “Result” having student roll no, name, and marks for
# 3 subjects (Java, C++, Python). Write a python program to show a command-line menu through which data can be added to the
# database and data can be read and displayed from the database.

# import sqlite3
#
# try:
#     print("Hii,this is a student management command line app.")
#     con = sqlite3.connect("Student.db")
#     con.execute("create table result(roll int primary key, name text not null, java int not null, cpp int not null, python int not null)")
#     con.commit()
# except sqlite3.OperationalError:
#     pass
#
# student_list = []
#
#
# def add_student():
#     con = sqlite3.connect("Student.db")
#     print("Enter the details of the student.")
#     name = input("Enter student's name.")
#     roll = input("Enter student's roll number")
#     javam = input("Enter marks obtained in Java")
#     cppm = input("Enter marks obtained in C++")
#     pythonm = input("Enter marks obtained in Python")
#     try:
#         con.execute("INSERT INTO result Values (?,?,?,?,?)", (roll,name,javam,cppm,pythonm))
#         con.commit()
#     except Exception as e:
#         print("Enter proper values",e)
#     student_list.append([roll,name,javam,cppm,pythonm])
#     print("New student added Successfully")
#     print("*******************************************")
#
#
# def read_all():
#     con = sqlite3.connect("Student.db")
#     r_set = con.execute(""" Select * from result""")
#     i = 0
#     print("Roll_no Name Java CPP Python")
#     for b in r_set:
#         for j in range(len(b)):
#             print(b[j],end=" ")
#         i = i + 1
#         print("")
#     print("*******************************************")
#
# if __name__ == "__main__":
#     choice = 0
#     con = sqlite3.connect("Student.db")
#     while choice != 3:
#         print()
#         print("1. Add Student.")
#
#         print("2. See all students' data.")
#         print("3. Exit.")
#         choice = int(input("Enter you choice: "))
#         print("-----------------------------------------")
#
#         if choice == 1:
#             add_student()
#
#         elif choice == 2:
#             read_all()
#
#         elif choice == 3:
#             print("Thank you")
#         else:
#             print("Invalid number try again")
#     con.commit()
#     con.close()


# Problem stat 11 of 20 may
# Implement a python program to create a GUI for a calculator. The calculator should accept two numbers and
# operand (+, Modulus, Power, reciprocal) and provide the correct output to user.
# If alphabets are given as input generate appropriate error message using proper Error handling mechanism.

# from tkinter import *
# from tkinter import messagebox
# import numpy as np
# cal = Tk()
# cal.geometry("312x324")
# cal.resizable(0, 0)
# cal.title("Calculator")
#
# def click(item):
#     global expression
#     expression = expression + str(item)
#     input_text.set(expression)
#
# def rec():
#     global expression
#     result=str(np.reciprocal(float(expression)))
#     input_text.set(result)
#     expression = ""
#
# def aclear():
#     global expression
#     expression = ""
#     input_text.set("")
#
# def equal():
#     global expression
#     try:
#         result = str(eval(expression))
#     except (SyntaxError,ValueError):
#         messagebox.showinfo("Error", "Please Enter Valid Syntax")
#
#     input_text.set(result)
#     expression = ""
#
#
# expression = ""
#
# input_text = StringVar()
#
# input_frame = Frame(cal, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
#                     highlightthickness=2)
#
# input_frame.pack(side=TOP)
#
# input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
#                     justify=RIGHT)
#
# input_field.grid(row=0, column=0)
#
# input_field.pack(ipady=10)
#
# btns_frame = Frame(cal, width=312, height=272, bg="grey")
#
# btns_frame.pack()
#
#
# seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#                command=lambda: click(7)).grid(row=0, column=0, padx=1, pady=1)
#
# eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#                command=lambda: click(8)).grid(row=0, column=1, padx=1, pady=1)
#
# nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: click(9)).grid(row=0, column=2, padx=1, pady=1)
#
# raiseto = Button(btns_frame, text="**", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                   command=lambda: click("**")).grid(row=0, column=3, padx=1, pady=1)
#
#
# four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: click(4)).grid(row=1, column=0, padx=1, pady=1)
#
# five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: click(5)).grid(row=1, column=1, padx=1, pady=1)
#
# six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#              command=lambda: click(6)).grid(row=1, column=2, padx=1, pady=1)
#
# modulus = Button(btns_frame, text="%", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                  command=lambda: click("%")).grid(row=1, column=3, padx=1, pady=1)
#
# one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#              command=lambda: click(1)).grid(row=2, column=0, padx=1, pady=1)
#
# two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#              command=lambda: click(2)).grid(row=2, column=1, padx=1, pady=1)
#
# three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#                command=lambda: click(3)).grid(row=2, column=2, padx=1, pady=1)
#
# plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#               command=lambda: click("+")).grid(row=2, column=3, padx=1, pady=1)
#
#
# zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: click(0)).grid(row=3, column=0, padx=1, pady=1)
#
# clear = Button(btns_frame, text="Clear", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                command=lambda: aclear()).grid(row=3, column=1, padx=1, pady=1)
#
# equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                 command=lambda: equal()).grid(row=3, column=2, padx=1, pady=1)
#
# reciprocal = Button(btns_frame, text="1/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                 command=lambda: rec()).grid(row=3, column=3, padx=1, pady=1)
#
# cal.mainloop()


# Problem stat 12 of 20 may
# With respect to the Automobile Dataset attached. Please write a python program that reads the dataset and
# generates output for the following questions using the Panda library
# 1: From the given dataset print the first and last five rows
# 2: Clean the dataset and update the CSV file
# 3: Find the most expensive car company name
# 4: Print All Toyota Cars details
# 5: Count total cars per company
# 6: Find each company’s Highest price car
# 7: Find the average mileage of each car making company
# 8: Sort all cars by Price column

#1
# import pandas as pd
# df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
# (df.head(5))
# (df.tail(5))
#
# #2
# df = pd.read_csv("D:\\Downloads\\Automobile_data.csv", na_values={
# 'price':["?","n.a","NaN"],
# 'engine-type':["?","n.a","NaN"],
# 'horsepower':["?","n.a","NaN"],
# 'average-mileage':["?","n.a","NaN"]}) (df)
# df.to_csv("D:\\Downloads\\Automobile_data.csv")
#
# #3
# df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
# df = df [['company','price']][df.price==df['price'].max()]
# (df)
#
#
# #4
# df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
# carmanufacturers = df.groupby('company')
# toyota = carmanufacturers.get_group('toyota')
# (toyota)
#
# #5
# df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
# df['company'].value_counts()
#
# #6
# df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
# carmanufacturers = df.groupby('company')
# price = carmanufacturers ['company','price'].max()
# print(price)
#
# #7
# df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
# carmanufacturers = df.groupby('company')
# mileage = carmanufacturers ['company','average-mileage'].mean()
# print(mileage)
#
# #8
# cars = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
# cars= cars.sort_values(by=['price'], ascending=False)
# cars.head(5)


# Problem stat 15 of 20 may
# Design a GUI driven program in python that maintains a file contact_directory. The file stores the names and telephone numbers.
# The program must allow users to add new contacts from GUI to file, search a contact based on name, update number and delete a contact.

# import tkinter
# from tkinter import*
# import sqlite3
# try:
#     con=sqlite3.connect('contact.db')
#     con.execute("create table contacts(cname,cno)")
#     con.commit()
# except sqlite3.OperationalError:
#     pass
#
# contacts_list = []
#
# def addNewContact():
#     window = tkinter.Tk()
#     window.title("Contacts Directory")
#     window.geometry("600x400")
#     namelbl = tkinter.Label(window, text="Enter the contact name: ")
#     namelbl.place(x=40, y=90)
#     nametxt = tkinter.Entry(window, width=20)
#     nametxt.place(x=230, y=90)
#     numlbl = tkinter.Label(window, text="Enter the contact number: ")
#     numlbl.place(x=40, y=40)
#     numtxt = tkinter.Entry(window, width=20)
#     numtxt.place(x=230, y=40)
#     savebtn1 = tkinter.Button(window, text="Add",command=lambda: saveContact(nametxt.get(), numtxt.get()))
#     savebtn1.place(x=300, y=300)
#     window.mainloop()
#
# def saveContact(namelbl,numlbl):
#     con.execute("INSERT INTO contacts Values (?,?)",(namelbl,numlbl))
#     con.commit()
#     contacts_list.append([namelbl,numlbl])
#     print("New contact added successfully")
#
# def displayContacts():
#     window = tkinter.Tk()
#     r_set=con.execute('Select * from contacts')
#     i=0
#     for b in r_set:
#         for j in range(len(b)):
#             e = Entry(window, width=30, fg='black')
#             e.grid(row=i, column=j)
#             e.insert(END, b[j])
#         i = i + 1
#     window.title("Contact Application")
#     window.geometry("600x400")
#     window.mainloop()
#
# def updateContact():
#     window = tkinter.Tk()
#     window.title("Contact Application")
#     window.geometry("600x400")
#     nballbl = tkinter.Label(window, text="Enter the name: ")
#     nballbl.place(x=40, y=40)
#     nbaltxt = tkinter.Entry(window, width=20)
#     nbaltxt.place(x=230, y=40)
#     numlbl = tkinter.Label(window, text = "Enter the contact number:")
#     numlbl.place( x = 40, y = 170)
#     numtxt = tkinter.Entry(window, width=20)
#     numtxt.place( x=230, y= 170)
#     no=numtxt.get()
#     savebtn=tkinter.Button(window, text="Update", command=lambda:updateName(nbaltxt.get(),numtxt.get()))
#     savebtn.place(x=300, y=300)
#     window.mainloop()
#
# def updateName(nb,no):
#     con.execute('Update contacts set cno=? where cname=? ',(no,nb))
#     con.commit()
#     print("Contact updated successfully")
#
# def deleteContact():
#     window = tkinter.Tk()
#     window.title("Contact Application")
#     window.geometry("600x400")
#     nbllbl = tkinter.Label(window, text="Enter the name: ")
#     nbllbl.place(x=40, y=170)
#     nbltxt = tkinter.Entry(window, width=20)
#     nbltxt.place(x=230, y=170)
#     savebtn2=tkinter.Button(window, text="Delete",
#     command=lambda:dContact(nbltxt.get()))
#     savebtn2.place(x=300, y = 300)
#     window.mainloop()
#
# def dContact(nb):
#     con.execute('Delete from contacts where cname=? ',(nb,))
#     con.commit()
#     print("Contact deleted successfully")
#
# def displaySpecificContact():
#     window = tkinter.Tk()
#     window.title("Contact Application")
#     window.geometry("600x400")
#     nballbl1 = tkinter.Label(window, text="Enter the name: ")
#     nballbl1.place(x=40, y=40)
#     nbaltxt1 = tkinter.Entry(window, width=20)
#     nbaltxt1.place(x=230, y=40)
#     savebtn3 = tkinter.Button(window, text="Display",command=lambda: disName(nbaltxt1.get()))
#     savebtn3.place(x=300, y=300)
#     window.mainloop()
#
# def disName(nm):
#     window = tkinter.Tk()
#     r_set=con.execute(' Select * from contacts where cname=?',(nm,))
#     i=0
#     for b in r_set:
#         for j in range(len(b)):
#             e=Entry(window,width=30,fg='black')
#             e.grid(row=i,column=j)
#             e.insert(END,b[j])
#             i = i + 1
#     window.title("Contact Application")
#     window.geometry("600x400")
#     window.mainloop()
#
# def main():
#     window = tkinter.Tk()
#     savebtn = tkinter.Button(window, text="Add",height=3,width=10,
#     command=lambda:addNewContact())
#     savebtn.place(x=100, y = 200)
#     displaybtn = tkinter.Button(window, text="Display",height=3,width=10, command=
#     lambda:displayContacts())
#     displaybtn.place(x=250, y=200)
#     updatebtn = tkinter.Button(window, text="Update",height=3,width=10, command=
#     lambda:updateContact())
#     updatebtn.place(x=400, y=200)
#     deletebtn = tkinter.Button(window, text="Delete",height=3,width=10, command=
#     lambda:deleteContact())
#     deletebtn.place(x=550, y=200)
#     deletebtn = tkinter.Button(window, text="Display specific",height=3,width=15,
#     command= lambda:displaySpecificContact())
#     deletebtn.place(x=700, y=200)
#     window.title("Contact Application")
#     window.geometry("300x300")
#     window.mainloop()
#
# if __name__ == "__main__":
#         main()


# Problem stat 20 of 20 may
# Write a python module “mynumbers” that contains a class “PyNumber”. The class stores only numeric integers as a list and has the following methods:
# a. Constructor to initialize the list
# b. Add(num) – to add num into the list
# c. High – that returns the largest value in the list
# d. Low – that returns the smallest value in the list
# e. Sort(desc=0) – that returns a list in sorted order. The method has a defaulf argument desc (if 0 : sorts in ascending order, if 1 sorts in
# descending order)
# f. Multiples(n) – that returns a list containing multiples of n.
# g. Look(num) – that returns the position of num if found in the list else -1 if num not in list
# Write another python program to access the given module and its class method using command –line menu options.

# # mynumbers.py
# list1 = []
# list2 = []
#
# class PyNumber:
#     def _init_(self, numbers):
#         self.number = numbers
#
#     def add():
#         num = int(input("Enter the number to be added: "))
#         list1.append(num)
#         print(f"{num} added successfully to the list.")
#
#     def high():
#         print("The largest value in the list is ", max(list1))
#
#     def low():
#         print("The smallest value in the list is ", min(list1))
#
#     def sort():
#         seq = int(input("Enter 0 for ascending and 1 for descending: "))
#         if seq == 0:
#             list1.sort()
#             print("The list arranged in ascending order: ", list1)
#         elif seq == 1:
#             list1.sort(reverse = True)
#             print("The list arranged in descending order: ", list1)
#         else:
#             print("Invalid input")
#
#     def multiples():
#         n = int(input("Enter number with which you want to multiply: "))
#         list2 = [i * n for i in list1]
#         print("Updated list: ", list2)
#
#     def look():
#         num = int(input("Enter the number to be searched: "))
#         if num not in list1:
#             print(f"{num} not found in list")
#         else:
#             index = list1.index(num)
#             print(f"The number {num} is found at index {index}")

## mynumbersmenu.py
# import mynumbers
# def main():
#     while True:
#         print("\n")
#         print("Menu")
#         print("1. Add number")
#         print("2. Largest value")
#         print("3. Lowest value")
#         print("4. Sort")
#         print("5. Multiples of the list ")
#         print("6. Look")
#         print("7. Exit")
#
#         ch = int(input("Enter your choice: "))
#
#         if ch == 1:
#             mynumbers.PyNumber.add()
#
#         elif ch == 2:
#             mynumbers.PyNumber.high()
#
#         elif ch == 3:
#             mynumbers.PyNumber.low()
#
#         elif ch == 4:
#             mynumbers.PyNumber.sort()
#
#         elif ch == 5:
#             mynumbers.PyNumber.multiples()
#
#         elif ch == 6:
#             mynumbers.PyNumber.look()
#
#
#         elif ch == 7:
#             print("Thankyou!")
#             break
#
# if __name__ == "__main__":
#     main()


# Problem stat 8 20 may
# Create a “library” database using sqlite3 containing a table “Book” having book id, name, author and unit price.
# Write a python program to show a command-line menu through which data can be added to the database and data can be read and displayed from the database.

# import sqlite3
# try:
#     con = sqlite3.connect('library.db')
#     con.execute("create table Book(book_id,name,author,unit_price)")
#     con.commit()
# except sqlite3.OperationalError:
#     pass
#
# books = []
#
# def add_book():
#     book_id = str(input("Enter Book id: "))
#     name = str(input("Enter Book name: "))
#     author = str(input("Enter Author Name: "))
#     unit_price = str(input("Enter Unit Price: "))
#
#     con.execute("INSERT INTO Book Values (?,?,?,?)", (book_id, name, author, unit_price))
#     con.commit()
#     books.append([book_id, name, author, unit_price])
#     print("New book added Successfully")
#
# def view_books():
#     print("Books are:\n")
#     all_books = con.execute("SELECT* from Book")
#
#     for book in all_books:
#         print(book)
#     con.commit()
#
# print("This is a database program\n")
# choice = 0
# while choice != 3:
#     print("\n *****\n")
#     print("Menu\n 1) Add \n 2) View Books\n 3) Exit")
#     choice = int(input("Choose option: "))
#     if choice == 1:
#         add_book()
#     elif choice == 2:
#         view_books()
#     elif choice == 3:
#         exit()


# Problem stat 14
# Write a python program to import Scipy package and perform the following.

# #1.a
# import numpy as np
# from scipy import linalg
# A=np.array([[3,2],[1,-1]])
# B = np.array([ [1, 2] ])
# B=B.T
# X=linalg.solve(A,B)
# print("x=",int(X[0]),"and y=",int(X[1]))
#
#
# #2
# import numpy as np
# n_array = np.array([[4, -2], [1, -3]])
# print("Numpy Matrix is:")
# print(n_array)
# det = np.linalg.inv(n_array)
# print("Inverse of given 2X2 matrix:")
# print(det)
#
# #3
# import numpy as np
# n_array = np.array([[2, -1, 0], [0, 3, -2], [1, 0, 1]])
# print("Numpy Matrix is:")
# print(n_array)
# det = np.linalg.det(n_array)
# print("\nDeterminant of given 2X2 matrix:")
# print(int(det))




