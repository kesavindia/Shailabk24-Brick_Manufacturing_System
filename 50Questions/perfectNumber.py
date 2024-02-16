'''
18 Create a program to check if a number is a perfect number.

REQUIREMENT GATHERING:

--------------------------------------
| Enter a Number: |__________|      |
|           Submit                    |
|____________________________________|

ANALYSIS:

Functional Analysis:
User will provide a number.
Empty value: "Invalid input, please enter a number."
Non-numeric values: "Invalid input, please enter a numeric value."

Technical Analysis:
Entity Name: PerfectNumberChecker
State: Data types - INT, Error messages - STRING
Behavior: Operators - FOR, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a number is provided and numeric.
2. Find the factors of the number.
3. Determine if the sum of factors equals the number (perfect number).
4. Print the result.

Programming Language:
State: Define a number given by the user.

Behavior:
1. Check if a number is provided and numeric.
2. Find the factors of the number.
3. Determine if the sum of factors equals the number (perfect number).
4. Print the result.
'''

print("Q18 PerfectNumberChecker")

number_input = input("Enter a Number: ")

if number_input.isdigit():
    num = int(number_input)

    if num > 0:
        factors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                factors_sum += i

        if factors_sum == num:
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")
    else:
        print("Invalid input, please enter a positive number.")
else:
    print("Invalid input, please enter a numeric value.")
