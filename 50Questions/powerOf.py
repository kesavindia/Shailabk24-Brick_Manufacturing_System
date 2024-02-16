'''
40 Create a program to check if a number is a power of two.

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
Entity Name: PowerOfTwoChecker
State: Data types - INT, Error messages - STRING
Behavior: Operators - IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a number is provided.
2. Determine if the number is a power of two using a loop and division.
3. Print the result.

Programming Language:
State: Define a number given by the user.

Behavior:
1. Check if a number is provided.
2. Determine if the number is a power of two.
3. Print the result.
'''

print("Q40 PowerOfTwoChecker")

# Input a number
number = input("Enter Number: ")

# Check if a number is provided
if number.isdigit():
    number = int(number)

    # Determine if the number is a power of two
    is_power_of_two = (number > 0) and (number & (number - 1) == 0)

    # Print the result
    print(f"{number} is a power of two." if is_power_of_two else f"{number} is not a power of two" )
else:
    print("Invalid input, please enter a number.")
