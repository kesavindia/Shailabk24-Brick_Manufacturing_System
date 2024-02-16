# ''' 1. Addition:
#  Write a program to add two numbers entered by the user'''
#
# def add(num1,num2):
#     # num1 = int(input("enter first number: "))
#     # num2 = int(input("enter second number: "))
#     sum = num1+num2
#     print(sum)
# add(2,3)
# add(-1,-2)
# add(-2,1)
# add(2,-2)
#
# def sub():
#     num1 = int(input("enter first number: "))
#     num2 = int(input("enter second number: "))
#     difference = num1-num2
#     print(difference)
# sub()
#
# def multiply():
#     num1 = int(input("enter first number: "))
#     num2 = int(input("enter second number: "))
#     product = num1*num2
#     print(product)
# multiply()

# def division():

# def modulus(a,b):
#     result =a%b
#     print(result)
# modulus(10,3)

# result = pow(2,3)
# result = 2**3
# print(result)
#7.comparsion
# x=34
# y=35
# if x==y:
#     print("same number")
# elif x>y:
#     print("x is bigger")
# else:
#     print("y is bigger")
#8. 20<=number>=30

# def check_number():
#     n = int(input("Enter a number: "))
#     # if 10 <= n >=20:
#     if n<=20 and n>=10:
#         print("entered number is correct.")
#     else:print("entered number is not correct.")
# check_number()
'''9. Logical OR:
Write a program to check if a number entered by the user is either less than 5 or greater than 15.'''
# def check_number():
#     n = int(input("Enter a number: "))
#     if n < 5 or n > 15:
#         print("entered number is correct.")
#     else:print("entered number is not correct.")
# check_number()
#0. Logical NOT:
#Write a program to check if a number entered by the user is not equal to 0

# def check_number():
#     n = int(input("Enter a number: "))
#     if n != 0:
#         print("number entered by the user is not equal to 0.")
#     else:
#         print("number entered by the user is equal to 0")
# check_number()

'''11. Bitwise Operators:
Write a program to perform bitwise AND, OR, XOR, left shift, and right shift operations on two 
integers.'''

# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter another number: "))
# n1ANDn2 = n1&n2
# print(n1ANDn2)
# n1ORn2 = n1|n2
# print(n1ORn2)
# n1XORn2 = n1^n2
# print(n1XORn2)
# n = int(input("Enter another number: "))
# left_shift = n<<1
# print(left_shift)
# right_shift = n>>3
# print(right_shift)
# 12. Swapping Variables:
# Write a program to swap two variables without using a temporary variable.
# a=2
# b=3
# print("before swap a is ",a)
# print("before swap b is ",b)
# a,b = b,a
# print("after swap a is ",a)
# print("after swap b is ",b)
#13. Check Even or Odd:
# Write a program to check if a number entered by the user is even or odd using bitwise operators.
# def is_even(n):
#     return n&1 == 0
# num = int(input("enter a number: "))
# if is_even(num):
#     print("entered number {} is even.".format(num))
# else:
#     print("entered number {} is odd.".format(num))
'''14. Toggle Case of a String:
Write a program to toggle the case of characters in a given string. (Convepy uppercase letters to 
lowercase and vice versa)'''

# def toggle_string(s):
#     result =""
#     for char in s:
#         if char.isupper():
#            result += char.lower()
#         else:
#             result += char.upper()
#     return result
# string = input("enter a string: ")
# toggled_string = toggle_string(string)
# print(toggled_string)

'''15. Calculate Simple Interest:
Write a program to calculate simple interest based on user input for principal amount, rate, and 
time'''

# def simple_interest(p,t,i):
#     return p*t*i/100
# p= float(input("enter principle: "))
# t= float(input("enter period in years: "))
# i= float(input("enter annual interest rate: "))
#
# result = simple_interest(p,t,i)
# print("Simple interest =", "{:.2f}".format(result))

# calculate BMI

# def calculate_bmi(weight,height):
#     bmi = weight/(height**2)
#     return round(bmi,2)
# def main():
#     w = float(input("Enter your weight in kgs: "))
#     h = float(input("Enter your height in mtrs: "))
#     bmi = calculate_bmi(w,h)
#     print(f"your bmi is {bmi}.")
#     print("your bmi is ","{:.2f}".format(bmi))
#     if bmi < 18:#
#         print("you are under weight.")
#     elif bmi < 25:
#         print(f"your weight {w} is normal.")
#     elif 25<=bmi and bmi<30:
#         print("you are over weight.")
#     else:
#         print("you are obese.")
# if __name__ == "__main__":
#     main()

# age = int(input("Enter your age: "))
# DL = (input("Enter Yes if you have dl or No: "))
# if age>=18 and DL == "Yes":
#     print("true")
# else:
#     print("false")
# def is_adult_with_license():
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         has_DL = input("Do you have a DL? press y or n: ") == "y"
#     if age>=18 and has_DL:
#         print("you are an adult with a licence")
#     elif age <18:
#         print("you are not an adult to have  a licence")
#     else:
#         print("you are an adult. please apply for a license.")
# is_adult_with_license()


# def check_if_student(age,is_studying):
#     return age<=22 or is_studying
# age = int(input("enter your age:"))
# is_studying = input("Are you studying? type YES or NO: ") == "YES"
# if check_if_student(age,is_studying):
#     print("You are a student.")
# else:
#     print("You are not a student.")

# num1 = int(input("enter a number: "))
# num2 = int(input("enter another number: "))
# remainder = num1% num2
# print(remainder)

# def is_not_happy():
#     is_happy = input("Are you happy?type Y or N: ") == "Y"
#     if not is_happy :
#         print("you are not healthy.")
#     else:
#         print("you are healthy.")
# is_not_happy()
# bitwise operators
#Perform a bitwise AND operation between num1 (binary: 0101) and num2 (binary: 0011).
# a = 6
# b = 5
# print(a & b)
# print(a | b)
# print(a ^ b)
# x = 0b0101
# y = 0b0011
# bitwise_and = x & y
# bitwise_or = x | y
# bitwise_xor = x ^ y
# print(bin(bitwise_and))
# print(bin(bitwise_or))
# print(bin(bitwise_xor))

# a="-2.0349"
# n=round(float(a),3)
# print(n)
# print("****{msg:<20}******".format(msg="haello"))
# num =1012233
# print("the different format is {:,}".format(num))

