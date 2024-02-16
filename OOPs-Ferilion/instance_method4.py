'''Create a class Student with an instance method is_passed()
 that checks if the student's grade is greater than or equal to
 50 and returns True if passed, otherwise False.'''

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def is_passed(self):
        return self.grade >=50
student1 = Student("Kesava",75)
if student1.is_passed():
    print(f"{student1.name} has passed.")
else:
    print(f"{student1.name} hasn't passed.")
