# 1. Create a class Student with the following:

# . Data members: name, roll_no, marks
# · A constructor to initialize the values
# . Member functions:
# display_details () -> to display student information
# calculate_grade () -> to return grade based on marks:
# . ≥90-> A
# . ≥75-> B
# . <50 -> Fail

# Create at least 3 student objects. Call both functions for each object


class Student():
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll_no.: {self.roll}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks < 50:
            print("You failed")
        else: 
            print("Grade C")
        
student1 = Student("Nidhi",3,99)
student1.display_details()
student1.calculate_grade()
print("\n")

student2 = Student("ridhi",5,23)
student2.display_details()
student2.calculate_grade()
print("\n")


student3 = Student("sidhi",6,52)
student3.display_details()
student3.calculate_grade()
print("\n")

