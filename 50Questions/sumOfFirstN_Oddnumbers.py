# Write a program that displays the sum of n odd natural numbers.



'''
REQUIREMENT GATHERING:

---------------------------------------
| Enter 'n' value: |__________|      |
|           Submit                   |
|____________________________________|

ANALYSIS:

Functional Analysis:
User will provide a value for 'n'.
Empty value: "Invalid input, please enter a value for 'n'."
Non-numeric value: "Invalid input, please enter a valid number."

Technical Analysis:
Entity Name: OddSumDisplay
State: Data types - INT, Error messages - STRING
Behavior: Operators - IF, ELIF, ELSE; Loops - FOR

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if 'n' is provided.
2. Check if 'n' is numeric.
3. Display the sum of 'n' odd natural numbers.

Programming Language:
State: Define 'n' given by the user.

Behavior:
1. Check if 'n' is provided.
2. Check if 'n' is numeric.
3. Display the sum of 'n' odd natural numbers.
'''

print("Q8 OddSumDisplay")

n_input = input("Enter 'n' value: ")

if not n_input or not n_input.isnumeric():
    print("Invalid input, please enter a valid number for 'n'.")
else:
    n = int(n_input)
    odd_sum = sum(range(1, 2 * n, 2))
    print(f"Sum of {n} odd natural numbers: {odd_sum}")
