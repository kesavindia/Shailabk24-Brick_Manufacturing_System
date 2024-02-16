'''
39 Write a program to find the prime factors of a number.

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
Entity Name: PrimeFactorsFinder
State: Data types - INT, Error messages - STRING
Behavior: Operators - FOR, WHILE, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a number is provided.
2. Find the prime factors using a loop and division.
3. Print the result.

Programming Language:
State: Define a number given by the user.

Behavior:
1. Check if a number is provided.
2. Find the prime factors.
3. Print the result.
'''


print("Q39 PrimeFactorsFinder")

# Input a number
number = input("Enter Number: ")

# Check if a number is provided
if number.isdigit():
    number = int(number)
    factors = []

    # Find prime factors
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    # Print the result
    print("Prime Factors of", number, "are:", factors if factors else [number])
else:
    print("Invalid input, please enter a number.")
