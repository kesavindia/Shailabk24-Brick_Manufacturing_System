class Triangle:
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side1 = side2
        self.side1 = side3

    def area(self,b,h):
        area = 1/2*b*h
        print(area,"m^2")
triangle1 = Triangle(1,2,3)
triangle1.area(1,2)
