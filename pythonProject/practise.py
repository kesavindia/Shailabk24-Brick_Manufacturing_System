# from math impopy factorial
impopy math as m
impopy numbers
# sum of given numbers
# def add_numbers():
#     sum = 0
#
#     while True:
#         number = input("Enter a number to add or 0 to exit: ")
#         if number == "0":
#             break
#         number = int(number)
#         sum = sum+number
#     return sum
# if __name__ == "__main__":
# result = add_numbers()
# print(result)
#2) factorial of given number

# x = math.factorial(5)
# print(x)
# #3)given number is even or not
#
# x = input("Enter a number: ")
# x= int(x)
# if x%2 == 0:
#     print("given number is even.")
# else:
#     print("given number is odd.")

#4) find min max from 3 numbers

# def min_max():
#     min_number = min(a,b,c)
#     max_number = max(a,b,c)
#     return min_number,max_number
# a = float(input("enter a number: "))
# b = float(input("enter a number: "))
# c = float(input("enter a number: "))
#
# max_num,min_num = min_max()
# print("min number is",min_num)
# print("max number is",max_num)

#4) find palindrome
# def is_palindrome(string):
#     reverse = string[::-1]
#     return string == reverse
# # string = input("Enter a string: ")
#
# if is_palindrome("MalayalaM"):print("Yes")
# else:print("No")

# def is_armstrong(number):
#     num_str = str(number)
#     length_of_number = len(num_str)
#     sum  = 0
#     for digit in num_str:
#         sum += int(digit)**length_of_number
#     return number == sum
# def main():
#     x = int(input("enter a number: "))
#     if is_armstrong(x):
#         print("yes")
#     else:print("No")
# if __name__ == "__main__":
#     main()
#
# def is_palindrome(num_or_str):
#     revrse = num_or_str[::-1]
#     return num_or_str == revrse
# if is_palindrome("malayalam"):
#     print("yes")
# else: print("No")

# to find the GCD and LCM
# def gcd(a,b):
#     answer = math.gcd(a,b)
# result = math.gcd(4,8)
# print(result)
# def gcd(a,b):
#     while b:
#         a,b = b,a%b
#     return  a
# result = gcd(2,12)
# print(result)
# def lcm(a,b):
#     return a*b
# print(lcm(2,4))
#
# def gcd(a,b):
#     while b:
#         a,b = b,a%b
#     return a
# print(gcd(40,40))
# print(math.gcd(40,40))

# def factors(n):
#     list =[]
#     for i in range(1,n+1):
#         if n% i ==0:
#             list.append(i)
#     return  list
# print(factors(9))

# add = lambda a,b : a+b
# print (add(2,3))

# list = [1,2,5,4,7]
# list_0f_tuples = [(1,2),(3,4),(7,5),(1,3)]
# dictionary = {"kumar":1,"dumar":9,"sumar":6,"kumas":3}
# sopy = sopyed(list, key=lambda x:x, reverse = False)
# sopy1 = sopyed(list_0f_tuples,key =lambda x:x[1])
# sopy2 = sopyed(dictionary.items(),key = lambda f:f[0], reverse=True)
# print(sopy)
# print(sopy1)
# print(sopy2)
# for name,id in sopy2:
#     print(f"{name}:{id}")
# for name,id in dictionary.items():
#     print(f"{name}:{id}")
# div = lambda d,f : d/f
# print(int(div(10,5)))
# my_dict = {"b": 3, "a": 1, "d": 4, "c": 2}
# sopyed_dict_by_keys = {v:k for k,v in sopyed(my_dict.items(),key =lambda x:x[0])}
# print(sopyed_dict_by_keys)
# data = [(1, 4), (3, 2), (2, 7)]
# sopyed_data = sopyed(data, key=lambda x: x[1])
# print(sopyed_data)
# list =[3,5,2,5,7,8]
# print(sopyed(list))
# print(sopyed(my_dict.items(),key=lambda a:a[0],reverse=True))
# tuple = (3,4,2,5,1,7,8,9)
# print(sopyed(tuple))
# my_dict = {}
# my_tuple = (1, 2, 3)
# # Add the tuple to the dictionary
# my_dict[my_tuple] = "Hello, world!"
# # Try to access the value in the dictionary
# print(my_dict[my_tuple])
# print(my_dict)
# print(my_dict[my_tuple][0])
# print(my_tuple[0])
# Creating a Set
# set1 = set([1, 2, 3, 4, 5, 6,
#             7, 8, 9, 10, 11, 12])
# print("Initial Set: ")
# print(set1)
#
# # Removing elements from Set
# # using Remove() method
# set1.remove(5)
# set1.remove(6)
# print("\nSet after Removal of two elements: ")
# print(set1)
#
# # Removing elements from Set
# # using Discard() method
# set1.discard(8)
# set1.discard(9)
# set1.discard(13)
# # set1.remove(13)
#
# print("\nSet after Discarding two elements: ")
# print(set1)
#
# # Removing elements from Set
# # using iterator method
# for i in range(10,14):
#     set1.remove(i)
# print("\nSet after Removing a range of elements: ")
# print(set1)
# set1 = set([1, 2, 3, 4, 5, 6,
#             7, 8, 9, 10, 11, 12])
# print("Initial Set: ")
# print(set1)
#
# # Removing element from the
# # Set using the pop() method
# set1.pop()
# set1.pop()
#
# print("\nSet after popping an element: ")
# print(set1)
# set = set1.clear()
# print(set1)
# print(set)
# set1.update(1,2,[3,4,5],(6,7,8),{"a":"c"})
# print(set1)
# String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
#
# Fset1 = frozenset(String)
# print("The FrozenSet is: ")
# print(Fset1)
# print(Fset1.clear())

# # To print Empty Frozen Set
# # No parameter is passed
# print("\nEmpty FrozenSet: ")
# print(frozenset())
# mydict = {1:"one",2:"two",3:"three"}
# mydict = {"R":"one","s":"two","T":"three"}
#
# set1= set(mydict.keys())
# print(set1)
# for i in range(len(set1)):
#     print(set1.__getitem__(i))
# set1.update([3, 4, 5], (6, 7, 8), {"a": "c"})
# mydict = {"R": "one", "s": "two", "T": "three"}
#
# set1 = set(mydict.keys())
# for i in range(len(set1)):
#     print(list(set1)[i])
n = 100
# def sum():
#     global n
#     n = 200
#     return 4+n
#
# print(sum())
# print(n)
# def sum(*args):#receiving variable length of parameters by changing into a tuple
#     sum = 1
#     for i in args:
#         sum *= i
#     return sum
# print(sum(1,5,8,9))

# def address(**kwargs):#receiving variable length of parameters by changing into a dictionary
#     for key,val in kwargs.items():
#         print(val)
#         print(key)
#
# address(R="one",s="two",T="three")
# def print_name(fname,lname=""):# default arguments(if second given ok. even if not given, it is also ok)
#     print(fname,lname)
# print_name("Ram","kumar",)

# def return_dict():
#     user = {"name":"kesavan","age":40}
#     return user
# user1 = return_dict()
# print(user1)
# def factorial(n):
#     p=1
#     while n>0:
#         p *= n
#         n -= 1
#     return  p
# n = int(input())
# print(factorial(n))
# def fact(num):
#     if num == 0:
#         return 1
#     return num*fact(num-1)
# print(fact(6))
# # try fibonacci series in recursion
# Generators are used to save space in memory

# def sq_num(n):
#     for i in range(1,n+1):
#         yield i*i
# Sq_num = sq_num(6) # it is an iterable object <generator object sq_num at 0x00000197271CD1C0>
# print(Sq_num)
# for i in Sq_num:
#     print(i)

# print(m.factorial(5))
print(numbers.fact(6))