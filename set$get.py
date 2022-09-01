class Student:
    def  setName(self,name):
        self.name= name
    def  getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks= marks
    def getMarks(self):
        return self.marks

n = int(input("Enter Number a Students:- "))
students=[ ]
for i in range(n):
    s = Student()
    name = input("Enter Student Name:- ")
    marks = int(input("Enter Student Marks:- "))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
for s in students:
    print("Hi",s.getName())
    print("Your Marks Are", s.getMarks())
    print()