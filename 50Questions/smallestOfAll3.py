'''Develop a program to find the smallest among three numbers.

ANALYSIS:

Functional Analysis:

User will provide three numbers to find the smallest among them.
Empty value: "Invalid input,if all three numbers are not entered."
Data types: INTEGER for numbers.
Number of values allowed: 3 numbers
Special characters: Allowed
Technical Analysis:

Entity Name: SmallestNumberFinder
State: Data types - INTEGER; Error messages - STRING
Behavior: Operators - Mathematical operators (<); Control Flow - IF, ELIF, ELSE
DESIGN (Sequence Diagrams):

Algorithm:

Check if three numbers are provided.
Find the smallest among the three numbers.
Print the result.
Programming Language:

State: Define three numbers given by the user.
Behavior:

Check if three numbers are provided.
Find the smallest among the three numbers.
Print the result.

'''

print("q30 30 .Develop a program to find the smallest among three numbers")
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if not all([num1, num2, num3]):
    print("Invalid input. Please enter all three numbers.")
else:
    smallest = min(num1, num2, num3)
    print("Smallest Number:", smallest)
