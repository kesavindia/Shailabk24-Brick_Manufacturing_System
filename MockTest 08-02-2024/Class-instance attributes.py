'''
define a class and create instance attributes, class attribute in that class
'''

class Person:
    """Represents a person."""
    # Class attribute (shared by all instances)
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances of the class
person1 = Person("Kesavan", 30)
person2 = Person("Ramkumar", 25)

# Accessing instance attributes
print(person1.name)
print(person2.age)

# Accessing the class attribute
print(person1.species)
print(Person.species)
