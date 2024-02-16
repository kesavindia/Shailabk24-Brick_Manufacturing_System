# Write a program that asks the user to enter 3 numbers in three variables and
# then displays the largest number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Comparing the numbers to find the largest
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3

# Displaying the result
print(f"The largest number is: {largest_number}")
