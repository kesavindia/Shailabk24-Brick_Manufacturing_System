'''1.Write a program that asks the user for their age and the type of ticket they want (child, adult, senior).
Based on their age and ticket type, calculate and display the ticket price.'''

# print("Want to know ticket price?")
# option = input("Type 'Yes' to continue: ")
# while option.lower() == "yes":
#     Name = input("Enter your name: ")
#     Age = int(input("Enter your age: "))
#     Type_of_ticket = input("Enter your category (child/ladies/gents/seniorCitizen): ")
#     if Age < 12:
#         print("Your ticket price: ", "Rs.100")
#     elif Age > 12 and Type_of_ticket == "ladies":
#         print("Your ticket price: ", "Rs.200")
#     elif Age > 59:
#         print("Your ticket price: ", "Rs.150")
#     else:
#         print("Your ticket price: ", "Rs.250")
#     continue_loop = input("Type 'Yes' to continue.'No' to exit: ")
#     if continue_loop.lower() != "yes" :
#         break
'''2.Create a temperature convepyer program that asks the user to input a temperature in Celsius and then convepys it to Fahrenheit.
It include an option for the user to convepy from Fahrenheit to Celsius as well.'''
# print("Welcome to temperature convepyer")
# def celcius_Farenheit(temp_in_C):
#     return temp_in_C * (9 / 5) + 32
# def farenheit_Celcius(temp_in_F):
#     return (temp_in_F- 32) * 5/9.
# while True:
#     print("1. Celcius to Fahrenheit")
#     print("2. Fahrenheit to Celcius")
#     print("3. Exit")
#     option1 = input("enter 1 or 2 to choose: ")
#     if option1 == "1":
#         input1 = float(input("Enter temperature in Celcius: "))
#         temp_in_F = celcius_Farenheit(input1)
#         print("Temperature in Farenheit = {:.2f}°F".format(temp_in_F))
#     elif option1 == "2":
#         input1 = float(input("Enter temperature in Farenheit: "))
#         temp_in_C = farenheit_Celcius(input1)
#         print("Temperature in Celcius = {:.2f}°C".format( temp_in_C))
#     elif option1 == "3":
#         break
#     else:
#         print("invalid input")
'''3.Ask the user to enter their account balance and then provide options for withdrawing
 or depositing money. Use decision making to update the account balance accordingly.'''
#
# print("1. Withdraw")
# print("2. Deposit")
# option = input("Enter one option from above:(1 or 2 ): ")
# balance = int(input("Enter your account balance: "))
# if option == "1":
#     entered_amount = int(input("Enter amount to withdraw: "))
#     if entered_amount < balance:
#         balance = balance-entered_amount
#         print("Your updated balance: ",balance)
#     else:
#         print("Insufficient balance to withdraw.")
# elif option == "2":
#     deposit = int(input("Enter amount to deposit: "))
#     balance += deposit
#     print("your updated balnce is:", balance)

'''4. Create a basic calculator that performs addition, subtraction, multiplication, and division.
 Prompt the user to enter two numbers and the operation they want to perform. '''
# print("Simple calculator")
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multi(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
# while True:
#     print("1. Press '1' for addition")
#     print("2. Press '2' for addition")
#     print("3. Press '3' for addition")
#     print("4. Press '4' for addition")
#     print("5. Press '5' to Quit")
#     option1 = input("enter a number of your choice: ")
#     if option1 == "1":
#         input1 = int(input("Enter a number: "))
#         input2 = int(input("Enter another number: "))
#         print(add(input1,input2))
#     elif option1 == "2":
#         input1 = int(input("Enter a number: "))
#         input2 = int(input("Enter another number: "))
#         print(sub(input1, input2))
#     elif option1 == "3":
#         input1 = int(input("Enter a number: "))
#         input2 = int(input("Enter another number: "))
#         print(multi(input1, input2))
#     elif option1 == "4":
#         input1 = int(input("Enter a number: "))
#         input2 = int(input("Enter another number: "))
#         print(div(input1, input2))
#     elif option1 == "5":
#         break
#     else:
#         print("invalid input")
'''5.Write a program that asks the user for their age and checks if they are eligible to vote. 
 Consider additional conditions, such as citizenship status.'''











