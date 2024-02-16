'''Create a class Person with an instance method
 get_age() that takes the birth year as input
 and calculates the age using the current year
 and self.'''
class Person:
    def __init__(self,name):
        self.name = name

    def get_age(self, birth_year, current_year):
        age = current_year - birth_year
        print(f"{self.name}'s age:", age)

# Create Person objects and call the method
kesavan = Person("Kesavan")
madhu = Person("Madhu")
kesavan.get_age(1983, 2024)
madhu.get_age(1990, 2024)

