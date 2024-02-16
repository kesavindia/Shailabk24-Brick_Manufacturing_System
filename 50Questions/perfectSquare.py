'''
29 Implement a program to check if a given number, is a perfect square.
ANALYSIS:

Functional Analysis:

User will provide a number to check if it's a perfect square.
Empty value: "Invalid input, please enter a number."
Data types: INTEGER for the number.
Number of values allowed: 1 number
Special characters: Allowed
Technical Analysis:

Entity Name: PerfectSquareChecker
State: Data types - INTEGER; Error messages - STRING
Behavior: Operators - Mathematical operators (*); Control Flow - IF, ELSE
DESIGN (Sequence Diagrams):

Algorithm:

Check if a number is provided.
Check if the number is a perfect square.
Print the result.
Programming Language:

State: Define a number given by the user.
Behavior:

Check if a number is provided.
Check if the number is a perfect square.
Print the result.

'''
print("29 perfect square")
number = int(input("Enter a Number: "))

if not number:
    print("Invalid input. Please enter a number.")
else:
    square_root = int(number**0.5)
    if square_root * square_root == number:
        result = f"{number} is a perfect square."
    else:
        result = f"{number} is not a perfect square."


print( result)