
''''''
'''
Given function : f(x) = 2x + 1. Find f(x)  when x = 10
                 -------------  ---------  -----------
                 # Behavior       REQ          State 
                 
STATE    : x = 10        : Data types/Data structures
BEHAVIOR : f(x) = 2x + 1 : Functions / Methods

'''
print("----Generic functions-------")
# print() id() type()
# x = 10
# print(x, id(x), type(x))
# sal = 100.4
# print(sal, id(sal), type(sal))
#
# print("---- int function-------")
#
# # int --> int()
# x = 10.4
# print("Before : ", x, type(x))
# x = int(x)
# print("After : ", x, type(x))
#
# print("----float function-------")
#
# # float --> float()
# x = 10
# print("Before : ", x, type(x))
# x = float(x)
# print("After : ", x, type(x))
#
# print("----bool function-------")
#
# # bool --> bool()
# x = 0
# print("Before : ", x, type(x))
# x = bool(x)
# print("After : ", x, type(x))
#
# print("----string function-------")
#
# # str       --> str()   40+
# num = 123456
# print("Before : ", num, type(num))
# num = str(num)  # "123456"
# print("After : ", num, type(num))

'''
print() id() type()
int      -----> int()
float    -----> float()
boolean  -----> bool()
string    ----> str()   40+  (10+ to 15+)
list       ---> list()  10+
tuple      ---> tuple()  2+
dictionary ---> dict()  10+
set        ---> set()    3+
'''
x = .009,0.9,.8
print(str(x))
# Armstrong number

def armstrong_number(n):
    n0_of_digits = len(n)
    if n<1:
        print("not armstrong number")
    elif len(n) == 1:
        print("Given number is armstrong number")
    else:
        sum = 0
        for

