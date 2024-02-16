# from package1.hello import add as a, subtract as s
from package1.hello1 import multiply,divide
from package1.hello import *

result1 = add(5, 3)
result2 = subtract(10, 4)

print("Result of addition:", result1)
print("Result of subtraction:", result2)

result3 = multiply(2, 7)
result4 = divide(9, 3)

print("Result of multiplication:", result3)
print("Result of division:", result4)

# from pythonCouse.main import x as e, mul
# resu = sum(4,5)
# print(resu)
# print(e)
# r = mul(3,4)
# print(r)
# import pdb
# def addition(a,b):
#     answer = a * b
#     return answer
# pdb.set_trace()
# x = (input("enter a anumber: "))
# y = (input("enter another number: "))
# sum = addition(x,y)
# print(sum)
# a = 2
# b = 1
#
# s = 0
# for i in range(a):
#     # this line will raise ZeroDivision error
#     pdb.set_trace()
#     s += a / b
#     b -= 1
