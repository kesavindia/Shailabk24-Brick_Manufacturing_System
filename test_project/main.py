# impopy math
# # 1)Explicit and Implicit data type conversion:
# # Implicit typecasting
# x = input("Enter a integer")
# y  = input("Enter an string")
# z = input("Enter a string value")
# a  = input("Enter a boolean value ")
# # Explicit typecasting
# b = complex(x)
# c = float(x)
# print(b)
# print(float(z))
# print(type(x))
# print(type(b))
# print(type(c))

# #2)Program for fetching id of a variable
#
# name = input("What is your name?")
# print(id(name))
# number = input("Enter a number.")
# print(id(number))
# bool =input("Enter a boolean value")
# print(id(bool))

# #3) is,in,not in operators:
# list = [1,2,3,4,5]
# var = 10
# if 7 in list:
#     print("number is present in the list")
# elif 5 not in list:
#     print("number is not present in the list")
# else:
#     print("Else block executed.")
# print(list is var) # False. bcoz, address of both are not same

#4) Menu driven program for arithmatic operators
#
# print("Menu driven program\n")
#
# print("1.'+' operator")
# print("2.'-' operator")
# print("3.'*' operator")
# print("4.'/' operator")
# print("5.'%' operator")
# print("6.'//' operator")
# print("7. Exit")
# num = input("Enter a number of your choice: ")
# while True:
#     if num == "1":
#         print("You have selected + operator.")
#         break
#     elif num == "2":
#         print("You have selected - operator.")
#         break
#     elif num == "3":
#         print("You have selected * operator.")
#         break
#     elif num == "4":
#         print("You have selected / operator.")
#         break
#     elif num == "5":
#         print("You have selected modulus operator.")
#         break
#     elif num == "6":
#         print("You have selected floor division operator.")
#         break
#     elif num == "7":
#         break
#     else:
#         print("You have entered invalid number.")
#         break

# 5) Menu driven program for logical operators
#
# print("Menu driven program\n")
#
# print("1.'or' operator")
# print("2.'and' operator")
# print("3.'not' operator")
# print("4. Exit")
# num = input("Enter a number of your choice: ")
# while True:
#     if num == "1":
#         print("If any one of the conditions is true, or operator will give True.")
#         break
#     elif num == "2":
#         print("If both of the conditions are true, and operator will give True.")
#         break
#     elif num == "3":
#         print("not will give reverse of the operand.")
#         break
#     elif num == "4":
#         break
#     else:
#         print("You have entered invalid number.")
#         break
#6) Menu driven program for calculating area, perimeter of circle and rectangle
def area_cirle():
    r = float(input("Enter radius in cm: "))
    return 3.14*r*r
# def perimeter_cirle():
#     r = float(input("Enter radius in cm: "))
#     return 2*3.14*r
# def area_rect():
#     l = float(input("Enter length in cm: "))
#     b = float(input("Enter breadth in cm: "))
#     return l*b
# def perimeter_rect():
#     l = float(input("Enter length in cm: "))
#     b = float(input("Enter breadth in cm: "))
#     return (l + b)*2
#
# print("Menu driven program for Area and Perimeter calculation\n")
#
# while True:
#     print("1.Calculate area")
#     print("2.Calculate perimeter")
#     print("3. Exit")
#     First_choice = input("Enter a number of your choice: ")
#     if First_choice == "1":
#         print("1.Circle")
#         print("2.rectangle")
#         print("3. Exit")
#         second_choice = input("Enter a number of your choice: ")
#         if second_choice == "1":
#             print(area_cirle(),"cm^2")
#         elif second_choice == "2":
#             print(area_rect(),"cm^2")
#         elif second_choice == "3":
#             break
#         else:
#             print("You have entered invalid number.")
#     elif First_choice == "2":
#         print("1.Circle")
#         print("2.rectangle")
#         print("3. Exit")
#         second_choice = input("Enter a number of your choice: ")
#         if second_choice == "1":
#             print(perimeter_cirle(),"cm")
#         elif second_choice == "2":
#             print(perimeter_rect(),"cm")
#         elif second_choice == "3":
#             break
#         else:
#             print("You have entered invalid number.")
#     elif First_choice == "3":
#         break
#     else:
#         print("You have entered invalid number.")
# 7) Menu driven program for bitwise operators

print("Menu driven program\n")

# print("1.'&' operator")
# print("2.'|' operator")
# print("3.'~' operator")
# print("4.'<<' operator")
# print("5.'>>' operator")
# print("6.'^(XOR)' operator")
# print("7. Exit")
# num = input("Enter a number of your choice: ")
# while True:
#     if num == "1":
#         x = int(input("enter an operand: "))
#         y = int(input("enter another operand: "))
#         print(bin(x&y))
#         break
#     elif num == "2":
#         x = int(input("enter an operand: "))
#         y = int(input("enter another operand: "))
#         print(bin(x|y))
#         break
#     elif num == "3":
#         x = int(input("enter an operand: "))
#         y = int(input("enter another operand: "))
#         print((x,y))
#         break
#     elif num == "4":
#         x = int(input("enter an operand: "))
#         y = int(input("enter another operand: "))
#         print((x<<y))
#         break
#     elif num == "5":
#         x = int(input("enter an operand: "))
#         y = int(input("enter another operand: "))
#         print(bin(x >> y))
#         break
#     elif num == "6":
#         x = int(input("enter an operand: "))
#         y = int(input("enter another operand: "))
#         print(bin(x ^ y))
#         break
#     elif num == "7":
#         break
#     else:
#         print("You have entered invalid number.")
#         break
