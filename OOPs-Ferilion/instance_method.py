'''Create a class called Rectangle with an instance method calculate_area() that calculates and returns
the area of the rectangle given its length and width.'''

class Rectangle:
    def __init__(self,l,w):
        self.l =l
        self.w = w
    def calculate_area(self):
        area = self.l*self.w
        return area
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

rectangle = Rectangle(l,w)
area = rectangle.calculate_area()
print (str(area),"m2")