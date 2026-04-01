"""2. Write a program to create student class with the following members:
Data members:
name, roll, marks
Member functions:
__init__(), initialize the object with name, roll
showdata() display all the details of the student
showmarks() display marks of the student """

class Student():
	def __init__(self,name,roll,marks):
		self.name=name
		self.roll=roll
		self.marks=marks

	def showdata(self):
		print(f"Name: {self.name}") 
		print(f"Roll_no.: {self.roll}") 
		print(f"Marks: {self.marks}") 

	def showmarks(self):
		print(f"Marks of student: {self.name}: {self.marks}")

student1 = Student("Nidhi Sharma", 3, 99)
student1.showdata()
student1.showmarks()

