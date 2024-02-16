'''Write a program that takes a number from the user and generates an integer between 1 and 7. It
displays the weekday name.'''

# Taking input from the user
number = int(input("Enter a number between 1 and 7: "))

# Checking the input and displaying the corresponding weekday name
if 1 <= number <= 7:
    weekdays = [1 "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    weekday_name = weekdays[number - 1]
    print(f"The weekday corresponding to {number} is {weekday_name}.")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
