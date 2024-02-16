'''Implement a program to calculate simple interest.

----------------------------------------
| Enter Principal: |_______________|  |
| Enter Rate:      |_______________|  |
| Enter Time:      |_______________|  |
|       Submit                          |
|______________________________________|
ANALYSIS:

Functional Analysis:

User will provide principal amount, rate of interest, and time to calculate simple interest.
Empty value: "Invalid input, please enter all required values."
Data types: FLOAT for principal and rate, INTEGER for time.
Number of values allowed: 3
Special characters: Allowed
Technical Analysis:

Entity Name: SimpleInterestCalculator
State: Data types - FLOAT, INTEGER; Error messages - STRING
Behavior: Operators - Mathematical operators (+, *, /); Formula - Simple Interest Formula (SI = P * R * T / 100)
DESIGN (Sequence Diagrams):

Algorithm:

Check if principal, rate, and time are provided.
Calculate simple interest using the formula.
Print the result.
Programming Language:

State: Define principal, rate, and time given by the user.
Behavior:

Check if principal, rate, and time are provided.
Calculate simple interest.
Print the result.'''

print("Q27  simple interest")

principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = int(input("Enter Time: "))


if not all([principal, rate, time]):
    print("Invalid input. Please enter all required values.")
else:

    simple_interest = (principal * rate * time) / 100


    print("Simple Interest:", simple_interest)