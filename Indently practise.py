# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#     def drive(self):
#         print(f'{self.brand}: drive()')
# suv = Car("Mahindra")
# suv.drive()
'''Both codes are same. this is the wierd behaviour of python'''
# def car_init(self,brand):
#     self.brand =brand
#
# def drive(self):
#     print(f'{self.brand}: drive()')
#
# Car = type('Car',(),{
#     '__init__':car_init,
#     'drive':drive
# })
# car =Car('volvo')
# car.drive()
# p=print("Hi Bob")#python implicitly adds return None at the bottom of all functions
# print(p)
# from datetime import date
# def show_date()->None:
#     print(date.today())
#
# show_date()
# from typing import NoReturn
# def raise_exc() -> NoReturn:
#     raise Exception('Bye bob')
# raise_exc()
from functools import lru_cache,cache
import time
#for improving performance of program by having cache memory
# @lru_cache
# def fib(n:int)->int:
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(0,40):
#     print(f'{i}:{fib(i)}')
# print(fib(20))
# def calc(x):
import time
# a,b='12'
# b,c='34'
# print(a+b+c)
# log = lambda *args: print(*args)
# has_money = True
# has_time = True
# has_friends = True
# has_internet = True
# def func():
#     if has_money:
#         if has_time:
#             if has_friends:
#                 if has_internet:
#                     log('yay')
# func()
# #Guard clause pattern is better than previous approach
# def func():
#     if not has_money:
#         log('No money')
#         return
#     if not has_time:
#         log('No time')
#         return
#     if not has_friends:
#         log('No friends')
#         return
#     if not has_internet:
#         log('No internet')
#         return
#     print('yay')
# func()
#create dictionary
# keys = ('spam','eggs','ham')
# my_d = dict.fromkeys(keys,0)
# print(my_d)
#Type hintiing in python
# string: str = 'string'
# _t:tuple[int|str,...] = (1,2,'f',4,5,6,7) #elipses for any number of elements
# print(_t)
# a,*b,c = 'Python'#forbidden. dont try this
# print(a,b,c)
# *_, = 'Python'
# print(_)
# def my_function():
#   """This is a docstring."""
#   print(my_function.__name__)
#
# # Print the name of the function()
# my_function()
from datetime import datetime,date
# import sys
from typing import NoReturn
# now = datetime.now()
# message = f'{now:%M:%S} Logged!'
# print(message,file = sys.stderr)
# with open('logs.text','a')as fil:
#     print(message,file=fil)
n:float = 100_000_0_000
print(f'{n:_}')
print(f'{n:,}')#magic f string syntax
def show_date()->None:
    print(date.today())
    return  None
today = show_date()
print(today)
def raise_exc()-> NoReturn:
    raise Exception('bye bob')
raise_exc()






# def modify_value(x):
#     x += 10
#
# a = 5
# print(modify_value(a))
# print(a)