'''what is Constructor Overloading and

Constructor overloading is a concept in
object-oriented programming where a class can
have multiple constructors with different
parameter lists. This allows objects to be created in various ways,
 depending on the parameters passed during instantiation.
1.Create a class called Point with a constructor
 that can be initialized with either two
 coordinates (x, y) or no coordinates
 (default to (0, 0))'''
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
#creating a Point with default coordinates(0,0)
point1 = Point()
print(f"Point 1: ({point1.x},{point1.y})")
#creating a point with specified co-ordinates(3,4)
point2 = Point(3,6)
print(f"Point 2: ({point2.x},{point2.y})")

