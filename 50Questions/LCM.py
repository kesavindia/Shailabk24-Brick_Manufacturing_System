'''
38 Implement a program to find the LCM of two numbers.

REQUIREMENT GATHERING:

-----------------------------------------
| Enter First Number: |_________|       |
| Enter Second Number:|_________|       |
|           Submit                    |
|_______________________________________|

ANALYSIS:

Functional Analysis:
User will provide two numbers.
Empty values: "Invalid input, please enter both numbers."

Technical Analysis:
Entity Name: LCMCalculator
State: Data types - INT, Error messages - STRING
Behavior: Operators - WHILE, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if both numbers are provided.
2. Calculate the LCM using the formula.
3. Print the result.

Programming Language:
State: Define two numbers given by the user.

Behavior:
1. Check if both numbers are provided.
2. Calculate the LCM.
3. Print the result.
'''

print("="*23)


# Input two numbers
number1 = input("Enter First Number: ")
number2 = input("Enter Second Number: ")

# Check if both numbers are provided
if number1.isdigit() and number2.isdigit():
    # Calculate the LCM using the formula LCM(a, b) = |a * b| / GCD(a, b)
    x, y = int(number1), int(number2)
    while y:
        x, y = y, x % y

    lcm = abs(int(number1) * int(number2)) // x
    print("LCM of", number1, "and", number2, "is", lcm)
else:
    print("Invalid input, please enter both numbers.")