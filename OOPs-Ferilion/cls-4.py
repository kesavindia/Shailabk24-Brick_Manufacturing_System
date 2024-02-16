'''Create a class Employee with an instance method
get_employee_info() that prints the name and salary of an employee
 using self.'''
class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_employee_info(self):
        print(f"Name :{self.name}")
        print(f"Salary :{self.salary}")

kesavan = Employee('K7',100000)
kesavan.get_employee_info()

