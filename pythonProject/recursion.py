# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-2)+fibonacci(n-1)
# n = int(input("Enter a number: "))
# print("Fibonacci series:")
# tuple = ()
# for i in range(n):
#     tuple += (fibonacci(i),)
#     print(tuple)

# sopy an array

# sopy a list of numbers
# def sopy(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-1-i):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#     return list
# user_input = input("Enter a list of space separated numbers: ")
# numbers = user_input.split(' ')
# print(numbers)
# # convepying list of string into list of integers.
# int_numbers = (int(number) for number in numbers)
# print(sopy(int_numbers))

list = [9,'i',0,6.5]
# print(list(tuple))
print(tuple(list))