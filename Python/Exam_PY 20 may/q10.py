import sqlite3

try:
    print("Hii,this is a student management command line app.")
    con = sqlite3.connect("Student.db")
    con.execute("create table result(roll int primary key, name text not null, java int not null, cpp int not null, python int not null)")
    con.commit()
except sqlite3.OperationalError:
    pass

student_list = []


def add_student():
    con = sqlite3.connect("Student.db")
    print("Enter the details of the student.")
    name = input("Enter student's name.")
    roll = input("Enter student's roll number")
    javam = input("Enter marks obtained in Java")
    cppm = input("Enter marks obtained in C++")
    pythonm = input("Enter marks obtained in Python")
    try:
        con.execute("INSERT INTO result Values (?,?,?,?,?)", (roll,name,javam,cppm,pythonm))
        con.commit()
    except Exception as e:
        print("Enter proper values",e)
    student_list.append([roll,name,javam,cppm,pythonm])
    print("New student added Successfully")
    print("*******************************************")


def read_all():
    con = sqlite3.connect("Student.db")
    r_set = con.execute(""" Select * from result""")
    i = 0
    print("Roll_no Name Java CPP Python")
    for b in r_set:
        for j in range(len(b)):
            print(b[j],end=" ")
        i = i + 1
        print("")
    print("*******************************************")

if __name__ == "__main__":
    choice = 0
    con = sqlite3.connect("Student.db")
    while choice != 3:
        print()
        print("1. Add Student.")

        print("2. See all students' data.")
        print("3. Exit.")
        choice = int(input("Enter you choice: "))
        print("-----------------------------------------")

        if choice == 1:
            add_student()

        elif choice == 2:
            read_all()

        elif choice == 3:
            print("Thank you")
        else:
            print("Invalid number try again")
    con.commit()
    con.close()


