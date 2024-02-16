'''Create a program to calculate the compound interest.

REQUIREMENT GATHERING:

----------------------------------------------
| Principal Amount: |______________|        |
| Rate of Interest: |______________|        |
| Time (years):     |______________|        |
|           Submit                          |
|____________________________________________|

ANALYSIS:

Functional Analysis:
User will provide principal amount, rate of interest, and time.
Empty or zero values: "Invalid input, please enter positive values."

Technical Analysis:
Entity Name: CompoundInterestCalculator
State: Data types - FLOAT, Error messages - STRING
Behavior: Operators - FORMULA, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if principal amount, rate of interest, and time are provided and are positive.
2. Calculate compound interest using the formula.
3. Print the result.

Programming Language:
State: Define principal amount, rate of interest, and time given by the user.

Behavior:
1. Check if principal amount, rate of interest, and time are provided and are positive.
2. Calculate compound interest using the formula.
3. Print the result.
'''


print("Q24 CompoundInterestCalculator")

principal_amount = float(input("Principal Amount: "))
rate_of_interest = float(input("Rate of Interest: "))
time_years = float(input("Time (years): "))

if principal_amount > 0 and rate_of_interest > 0 and time_years > 0:
    compound_interest = principal_amount * (1 + rate_of_interest / 100) ** time_years - principal_amount
    print(f"Compound Interest: {compound_interest:.2f}")
else:
    print("Invalid input, please enter positive values.")

