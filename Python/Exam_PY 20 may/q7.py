from q7_module import Student

def add_new_student():
  name = input("Enter Student Name: ")
  rollno = int(input("Enter Student Rollno: "))
  java = int(input("Enter Java Marks: "))
  cpp = int(input("Enter C++ Marks: "))
  python = int(input("Enter Python Marks: "))
  Student(rollno, name, java, cpp, python)

def display():
    if(len(Student.student) == 0):
        print("Student Records Empty")
    for i in Student.student:
        print("Roll Num: {} | Name: {} | JAVA: {} | CPP: {} | PYTHON: {}\n".format(i, Student.student[i][0], Student.student[i][1], Student.student[i][2], Student.student[i][3] ))

def update_student():
  roll = int(input("Enter the roll no: "))
  for i in Student.student:
    if i == roll:
      java_m = int(input("Enter the update JAVA marks"))
      cpp_m = int(input("Enter the update CPP marks"))
      py_m = int(input("Enter the update PYTHON marks"))
      Student.student[i][1] = java_m
      Student.student[i][2] = cpp_m
      Student.student[i][3] = py_m
      print(f"Roll No. {i} marks is updated")
      break

def delete_student():
  roll = int(input("Enter the roll no to delete: "))
  for i in Student.student:
    if i == roll:
      del Student.student[i]
      print(f"Roll No. {i} marks was removed")
      break

choice = 0
while choice != 5:
    print()
    print("1. Add a New Student")
    print("2. Update marks of any student")
    print("3. Delete a Student")
    print("4. Display Student")
    print("5. to exit")
    choice = int(input("Enter you choice: "))
    print("-----------------------------------------")

    if choice == 1:
        add_new_student()
    elif choice == 2:
        update_student()
    elif choice == 3:
        delete_student()
    
    elif choice == 4:
        display()
    
    elif choice == 5:
        print("Thank you")
    else:
        print("Invalid number try again")
