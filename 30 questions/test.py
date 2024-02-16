# class Parent:
#  def show(self):
#   print("Parent class")
# class Child(Parent):
#  def show(self):
#   super().show() # Calling the method from the parent class
#  # print("Child class")
# child = Child()
# # child.show()
# class MyClass:
#     class_variable = "I am a class variable"
#
#     def __init__(self, value):
#         self.instance_variable = value
#
#     @staticmethod
#     def static_method():
#         print("This is a static method")

# # Creating an instance of MyClass
# my_instance = MyClass("Hello, world!")
#
# # Accessing instance variable
# print("Instance variable:", my_instance.instance_variable)
#
# # Accessing class variable
# print("Class variable:", MyClass.class_variable)
#
# # Calling the static method
# MyClass.static_method()
# class Circle:
#  def __init__(self, radius):
#   self._radius = radius # Protected attribute
#  @property
#  def radius(self):
#   return self._radius
#  @radius.setter
#  def radius(self, value):
#   if value > 0:
#    self._radius = value
# circle = Circle(5)
# print(circle.radius) # Using the getter
# circle.radius = 7 # Using the setter
class MyClass:
 def __init__(self):
  self._protected_var = 10
  self.__private_var = 20
obj = MyClass()
print(obj._protected_var) # Accessing protected variable (convention)
# print(obj.__private_var) # This would result in an AttributeError
print(obj._MyClass__private_var) # Accessing private variable (name mangling)