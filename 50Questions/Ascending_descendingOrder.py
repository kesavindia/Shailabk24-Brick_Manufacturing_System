'''
9 Write a program that accepts three numbers from the user and prints
 "increasing" if the numbers are in increasing order,
 "decreasing" if the numbers are in decreasing order,
 and "Neither increasing nor decreasing order" otherwise.
'''

'''
REQUIREMENT GATHERING:

---------------------------------------
| Enter Number 1: |__________|      |
| Enter Number 2: |__________|      |
| Enter Number 3: |__________|      |
|           Submit                   |
|____________________________________|

ANALYSIS:

Functional Analysis:
User will provide three numbers.
Empty value: "Invalid input, please enter all three numbers."
Non-numeric value: "Invalid input, please enter valid numbers."

Technical Analysis:
Entity Name: OrderChecker
State: Data types - INT, Error messages - STRING
Behavior: Operators - IF, ELIF, ELSE; Logical Operators - AND, OR

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if all three numbers are provided.
2. Check if all three numbers are numeric.
3. Determine if the numbers are in increasing, decreasing, or neither order.
4. Print the result.

Programming Language:
State: Define three numbers given by the user.

Behavior:
1. Check if all three numbers are provided.
2. Check if all three numbers are numeric.
3. Determine if the numbers are in increasing, decreasing, or neither order.
4. Print the result.
'''


print("Q9 OrderChecker")

num1_input = input("Enter Number 1: ")
num2_input = input("Enter Number 2: ")
num3_input = input("Enter Number 3: ")

if not num1_input or not num1_input.isnumeric() or not num2_input or not num2_input.isnumeric() or not num3_input or not num3_input.isnumeric():
    print("Invalid input, please enter valid numbers for all three values.")
else:
    num1 = int(num1_input)
    num2 = int(num2_input)
    num3 = int(num3_input)

    if num1 < num2 < num3:
        print("Increasing")
    elif num1 > num2 > num3:
        print("Decreasing")
    else:
        print("Neither increasing nor decreasing order")
