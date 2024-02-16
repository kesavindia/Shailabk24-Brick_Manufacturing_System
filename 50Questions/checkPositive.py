'''4 Write a program that reads a floating-point number and prints "zero" if the number is zero.
Otherwise, print "positive" or "negative". Add "small" if the absolute value of the number is less than
1, or "large" if it exceeds 1,000,000.'''

# Taking input from the user
number = float(input("Enter a floating-point number: "))

# Checking the conditions and printing the appropriate message
if number == 0:
    print("zero")
elif number > 0:
    if abs(number) < 1:
        print("positive small")
    elif number > 1000000:
        print("positive large")
    else:
        print("positive")
else:
    if abs(number) < 1:
        print("negative small")
    elif abs(number) > 1000000:
        print("negative large")
    else:
        print("negative")
