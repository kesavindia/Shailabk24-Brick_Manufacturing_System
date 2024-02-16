'''
41 Develop a program to check if a number is an abundant number.

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
Entity Name: AbundantNumberChecker
State: Data types - INT, Error messages - STRING
Behavior: Operators - IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a number is provided.
2. Determine if the number is an abundant number.
3. Print the result.

Programming Language:
State: Define a number given by the user.

Behavior:
1. Check if a number is provided.
2. Determine if the number is an abundant number.
3. Print the result.
'''

print("Q41 AbundantNumberChecker")

number_input = input("Enter Number: ")

if number_input.isdigit():
    number = int(number_input)
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    is_abundant_number = sum_of_divisors > number
    if is_abundant_number:
        print(number, "is an abundant number.")
    else:
        print(number, "is not an abundant number.")
else:
    print("Invalid input, please enter a number.")
