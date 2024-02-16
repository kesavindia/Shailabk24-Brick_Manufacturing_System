'''Implement a class Rectangle with a constructor that
can be initialized with either length and width or just one
side (both sides default to 0).'''

class Rectangle:
    def __init__(self,length=0,width=0):
        self.length = length
        self.width = width
rectangle1 = Rectangle()
print(f"Rectangle 1: Length = {rectangle1.length},Width = {rectangle1.width}")
rectangle2 = Rectangle(3)
print(f"Rectangle 2: Length = {rectangle2.length},Width = {rectangle2.width}")
rectangle3 = Rectangle(5,6)
print(f"Rectangle 3: Length = {rectangle3.length},Width = {rectangle3.width}")