'''
37 Create a program to calculate the sum of digits of a given number.

REQUIREMENT GATHERING:

---------------------------------------
| Enter Number: |_________|           |
|           Submit                    |
|_____________________________________|

ANALYSIS:

Functional Analysis:
User will provide a number.
Empty value: "Invalid input, please enter a number."

Technical Analysis:
Entity Name: DigitSumCalculator
State: Data types - INT, Error messages - STRING
Behavior: Operators - WHILE, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a number is provided.
2. Calculate the sum of its digits.
3. Print the result.

Programming Language:
State: Define a number given by the user.

Behavior:
1. Check if a number is provided.
2. Calculate the sum of its digits.
3. Print the result.
'''


print("Q37 DigitSumCalculator")

# Input a number
number = input("Enter Number: ")

# Check if a number is provided
if number.isdigit():
    # Calculate the sum of its digits
    digit_sum = sum(int(digit) for digit in number)
    print("Sum of digits:", digit_sum)
else:
    print("Invalid input, please enter a number.")
