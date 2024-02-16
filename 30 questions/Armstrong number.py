'''Write a program to check if a number is an Armstrong number.

ANALYSIS:

Functional Analysis:

User will provide a number to check if it's an Armstrong number.
Empty value: "Invalid input, please enter a number."
Data types: INTEGER for the number.
Number of values allowed: 1 number
Special characters: Not applicable
Technical Analysis:

Entity Name: ArmstrongNumberChecker
State: Data types - INTEGER; Error messages - STRING
Behavior: Operators - Mathematical operators (**, //); Control Flow - IF, ELSE
DESIGN (Sequence Diagrams):

Algorithm:

Check if a number is provided.
Check if the number is an Armstrong number.
Print the result.
Programming Language:

State: Define a number given by the user.
Behavior:

Check if a number is provided.
Check if the number is an Armstrong number.
Print the result.
'''

print("31 Write a program to check if a number is an Armstrong number")
def isArmstrongNumber():
    input_number = (input("Enter a number: "))
    length_number = len(input_number)
    sum1 = sum(int(digit) ** length_number for digit in input_number)
    return sum1==int(input_number)
print(isArmstrongNumber())

