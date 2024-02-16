'''Write a class method get_square()
in a class called MathUtils that takes a number as
 an argument and returns its square using cls.'''

class MathUtils:
    @classmethod
    def get_square(cls,num):
        return num*num
square = MathUtils.get_square(5)
print(square)


