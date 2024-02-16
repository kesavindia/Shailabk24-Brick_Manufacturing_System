"""Create a class Employee with a constructor that can be
 initialized with either the employee's name and salary or
 just the name (salary defaults to 0)."""
class Employee:
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary
# Creating an Employee with only name (default salary to 0)
employee1 = Employee("Tom")
# Creating an Employee with name and salary
employee2 = Employee("Kesavan",100000)
print(f"{employee1.name}'s salary:{employee1.salary}")
print(f"{employee2.name}'s salary:{employee2.salary}")
