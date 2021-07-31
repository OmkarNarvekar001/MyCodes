class Student():
  student = {}
  def __init__(self,  rollno, name, java, cpp, python):
    self.rollno = rollno
    self.name = name
    self.java = java
    self.cpp = cpp
    self.python = python
    self.dictionary()

  def dictionary(self):
    lis = []
    lis.append(self.name)
    lis.append(self.java)
    lis.append(self.cpp)
    lis.append(self.python)
    self.student[self.rollno] = lis
