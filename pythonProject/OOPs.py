# class Dog:
#     # class attribute
#     attr1 = "mammal"
#     legs = 4
#     # Instance attribute
#     def __init__(self, name,age):
#         self.peru = name
#         self.age = age
#
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger",9)
#
# Tommy = Dog("Tommy",8)
#
#
# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Rodger has {} legs.".format(Rodger.__class__.legs))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))
#
# # Accessing instance attributes
# print("My name is {}".format(Rodger.peru))
# print("My name is {}".format(Tommy.peru))
# print("Tommy's age is a {}".format(Tommy.age))
# print("Rodger's age is a {}".format(Rodger.age))












#creating a class
# class Car:
#     attr1 = "4 wheeler"
#     attr2 = "Luxury vehicle"
#creating a constructor/initializing object variables

    # def __init__(self,Brand,Cost):
    #     self.Brand = Brand
    #     self.Cost = Cost
    #     # pass
def speak(self):
        print("My name is {}".format(self.Brand))
# creating instances of this class
# swift = Car()
# swift.Brand = "Maruti"
# swift.Cost = 2000
# swift.power =  "100BHP"
# Mayback = Car()
# Mayback.Brand = "Mercedes"
# Mayback.Cost = 10000
# #Accessing class variables
# print("Mayback is a type of {}".format(Mayback.__class__.attr2))
# print("Swift is a {}".format(swift.__class__.attr1))
# #Accessing object variables
#
# print("Mayback is a brand of {}".format(Mayback.Brand))
# print("swift is a brand of {}.".format(swift.Brand))
# print("swift's cost is {}".format(swift.Cost))
# print("swift has a power of {}.".format(swift.power))
# #Accessing class method
# Mayback.speak()
# class Dog:
    # attribute
    # attr1 = "mammal"
    # attr2 = "dog"
    #
    # # Constructor method
    # def __init__(self, name, place):
    #     self.name = name
    #     self.place = place
    #
    # def fun(self):
    #     print("I'm a",self.name, "&", self.attr1)
    #     print("I live in",self.place,)


# Driver code
# Object instantiation
# Rodger = Dog("dog1", "madurai")
# Tommy = Dog("dog2", "madurai2")
# # Tommy.native = "jharkhand"
#
# # Accessing class attributes
# # and method through objects
# print(Rodger.attr1)
# Rodger.fun()
# Tommy.fun()
# print("Tommy's native is {}".format(Tommy.place))
class Newton:
    breed = "man"

    def __init__(self,course,place,fav):
        self.Course = course
        self.Place = place
        self.fav = None
        print("constructor method is called")
    def eating(self):
        print("person of",self.Place,"is eating his",self.fav)
kesavan = Newton("FSD","madurai","pasta")
Jack = Newton("DS","Mumbai","pulio")
kesavan.native = "India"
Jack.native = "USA"
print(id(kesavan))
print(id(Jack))
print(kesavan.Course)
kesavan.fav = "Halwa"
Jack.fav = "Mysorepak"
kesavan.eating()
Jack.eating()
#Accessing class attributes with the instance of the class
print("Kesavan is a breed of {}".format(kesavan.__class__.breed))
print("Jack is a breed of {}".format(Jack.__class__.breed))
print("Kesavan is of {}".format(kesavan.native))
print("Jack is of {}".format(Jack.Place))