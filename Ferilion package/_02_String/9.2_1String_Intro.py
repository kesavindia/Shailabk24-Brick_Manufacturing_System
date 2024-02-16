'''

@author: mnettem
'''
from sys impopy getsizeof

message1 = 'hello world!'
print("----message1-----",message1)

message2 = "pyTHON PROGRAMMING!"
print("----message2-----",message2)

'''
1. indexing
2. slicing
3. adding
4. multiplying and
5. checking for membership.
'''

# 1 INDEXING
print("----- 1st index in message1 -----",message1[4])
print("----- 4th index in message1 -----  Positive : ",message1[1],"  Negative :  ", message1[-11])

# 2 SLICING 
print("Slicing positive : ",message1[6:11])  # print from index 6 to position 11
print("Slicing Negative : ",message1[-6:-1]) #
print("Slicing with stapy stop step : ",message2[0:13:1], " == ",message2[0:13], "  ",message2[0:13:2]," ",message2[0:13:3])
print("Slicing without any positions + :",message2[::],"  ",message2[2::]," ",message2[:8:]," ",message2[::2]," ",message2[::3])
print("Slicing without any positions - :",message2[::],"  ",message2[-2::]," ",message2[:-8:]," ",message2[::-2]," ",message2[::-3])
print("Slicing without any positions - :",message2[::-1])


# 3 ADDING CONCATINATION

final_message = message1 + " Welcome to " + message2 

print("Concatenation :: ",final_message)



# 4 MULTIPLYING
print("Multiplication : ", message1*4)
print("Multiplication : ", final_message*4)


# 5 CHECKING FOR MEMBERSHIP
print("--Membership---- : ", "pyTHON" in message2)


#BUILT IN STRING METHODS
print("---Capitalize -- ",message1.capitalize()) # Capitalizes first letter of string
print("---Count-------- ",message2.count('O'),"  ",message2.count('O',6,15)) #stapy,end are optional

#String Formatting Operators
# print("My name is %s and weight is %d kg!" % ('Zara', 21))
#
# #ASCII  Unicode
# str1 = "Madhu"
# str2 = u"Madhu"
# print(str2,"  ",len(str1),"  ",len(str2))
# print(getsizeof(str1)," ",getsizeof(str2))

# string = input("Enter a string: ")
# rev_string = string[::-1]
# if string == rev_string:
#     print("Given string is palindrome.")
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-2)+fibonacci(n-1)
# # n = int(input("Enter a number: "))
# for i in range(0,10):
#     print((fibonacci(i)),end="-")


# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# n = int(input("Enter the number of Fibonacci numbers to print: "))
#
# for i in range(n):
#     print(fibonacci(i),end=" ")
# def palindrome(string1):
#     s = str(string1)
#     reverse_s = s[::-1]
#     print(reverse_s)
#     return reverse_s == s
# stri = input()
# if palindrome(stri):
#     print("yes")
# else:print("No")
def reverse_string(s):
    reverse = ""
    st = str(s)
    for i in range(len(st)-1,-1,-1):
        reverse += st[i]
    return reverse
print(reverse_string("Kesavan"))
