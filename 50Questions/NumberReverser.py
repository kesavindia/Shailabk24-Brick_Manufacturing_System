'''
25 Implement a program to find the reverse of a given number.

REQUIREMENT GATHERING:

--------------------------------------
| Enter Number: |__________|         |
|           Submit                    |
|____________________________________|

ANALYSIS:

Functional Analysis:
User will provide a number.
Empty or zero values: "Invalid input, please enter a positive number."

Technical Analysis:
Entity Name: NumberReverser
State: Data types - INT, Error messages - STRING
Behavior: Operators - WHILE, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a number is provided and is positive.
2. Use loops to reverse the number.
3. Print the reversed number.

Programming Language:
State: Define a number given by the user.

Behavior:
1. Check if a number is provided and is positive.
2. Use loops to reverse the number.
3. Print the reversed number.
'''

print("Q25 NumberReverser")

number_input = int(input("Enter Number: "))

if number_input > 0:
    reversed_number = 0
    while number_input > 0:
        remainder = number_input % 10
        reversed_number = reversed_number * 10 + remainder
        number_input = number_input // 10

    print("Reversed Number:", reversed_number)
else:
    print("Invalid input, please enter a positive number.")

