impopy math
impopy sys

# print(math.factorial(5))
int_size = sys.getsizeof(1)
float_size = sys.getsizeof(1.0)
string = sys.getsizeof(True)

print("Size of int in bytes:", int_size)
print("Size of float in bytes:", float_size)
print("Size of string in bytes:", string)
#
# #Arithmatic operators
# print(2 + .9)
# x = 2
# y = .8
# print(math.ceil(x+y))
# print(math.floor(x+y))
#
# # Calculate the area of a triangle
# base = 10
# height = 5
# area = (base * height) / 2
# print(area)
#
# # Calculate the volume of a sphere
# radius = 5
# volume = (4 / 3) * math.pi * radius ** 3
# print(str(volume) + "cm^3")
# # Addition
# x = 1 + 2
# print(x)  # Output: 3
#
# # Subtraction
# y = 10 - 5
# print(y)  # Output: 5
#
# # Multiplication
# z = 2 * 3
# print(z)  # Output: 6
#
# # Division
# a = 12 / 4
# print(a)  # Output: 3.0
#
# # Modulus (remainder)
# b = 13 % 5
# print(b)  # Output: 3
#
# # Exponentiation (power of)
# # c = 2 ** 3
# c=pow(2,3)
# print(c)  # Output: 8
#
# # Floor division (truncated division)
# d = 23// 6
# print(d)  # Output: 3
# #Comparison operators
#
# # Equal to
# x = 1 == 2
# print(x)  # Output: False
#
# # Not equal to
# y = 10 != 5
# print(y)  # Output: True
#
# # Less than
# z = 2 < 3
# print(z)  # Output: True
#
# # Less than or equal to
# a = 12 <= 4
# print(a)  # Output: False
#
# # Greater than
# b = 13 > 5
# print(b)  # Output: True
#
# # Greater than or equal to
# c = 2 ** 3 >= 8
# print(c)  # Output: True
#
# x = 3**2 == 9
# print(x)  # Output: True
#
# # Logical operators
#
# # Logical AND
# x = True and False
# print(x)  # Output: False
#
# # Logical OR
# y = True or False
# print(y)  # Output: True
#
# # Logical NOT
# z = not False
# print(z)  # Output: True
#
# d = not -1
# print(d)
# d = not 0
# print(d)
#
# # Bitwise AND
# x = 5 & 3
# print(x)  # Output: 1
#
# # Bitwise OR
# y = 5 | 3
# print(y)  # Output: 7
#
# # Bitwise XOR
# z = 5 ^ 3
# print(z)  # Output: 6
#
# # Bitwise NOT
# a = ~5
# print(a)  # Output: -6
#
# # Bitwise left shift
# b = 5 << 1
# print(b)  # Output: 10
#
# # Bitwise right shift
# c = 5 >> 1
# print(c)  # Output: 2
#
# # Assignment
# x = 1
# print(x)  # Output: 1
#
# # Addition assignment
# x += 2
# print(x)  # Output: 3
#
# # Subtraction assignment
# x -= 1
# print(x)  # Output: 2
#
# # Multiplication assignment
# x *= 3
# print(x)  # Output: 6
#
# # Division assignment
# x /= 2
# print(x)  # Output: 3.0
#
# # Modulus assignment
# x %= 2
# print(x)  # Output: 1
#
# # Exponentiation assignment
# x **= 2
# print(x)  # Output: 9
#
# # Identity operators
# x = 1
# y = 1
# print(x is y)  # Output: True
#
# x = 1
# y = 2
# print(x is not y)  # Output: True
#
# # Membership operator
# x = 1 in [1, 2, 3]
# print(x)  # Output: True
#
# x = 4 in [1, 2, 3]
# print(x)  # Output: False
#
# a = 2 not in {1,3,4}
# print(a) # Output: True5
#
# res = math.gcd(4,8)
# print(res)
#
# n = input("Enter a number: ")
# n = float(n)
# # print(math.log10(n))
# # print(math.cos(n))
# ans = "{:.6f}".format(math.exp(n))
# print(ans)
# x = 870328453
# print(x)
# list=['John',678,20.4,'Peter']
# list1=[456,'Andrew']
# print(list)
# print(list + list1)
# Create a list
# my_list = [1, 2, 3, 4, 5]
#
# # Add an element to the list
# my_list.append(6)
#
# # Remove an element from the list
# my_list.remove(3)
#
# # Modify an element in the list
# my_list[2] = 7
#
# # Print the list
# print(my_list)
# my_tuple = (1, 2, 3, 4, 5)
#
# # Try to add an element to the tuple
# my_tuple.append(6)
c = 1+3j
print(type(c))
d = "hello"
print("d is a string:",isinstance("der",str))
print("c is a complex number:",isinstance(1+3j,complex))
print(isinstance(123,int))
print(isinstance((2,3),tuple))
print(isinstance((2,3),tuple))
print(isinstance({'a':3},tuple))
print(isinstance(123,float))
x=10
x="ketyyuhsjshd" #implicit type casting
print(type(x))
y = 10.00
print(int(y))#explicit type casting
print(id(y))




