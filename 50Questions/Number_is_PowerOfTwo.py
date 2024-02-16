
'''
23 Create a program to check if a number is a power of two.

REQUIREMENT GATHERING:

--------------------------------------
| Enter Number: |______________|     |
|           Submit                    |
|____________________________________|

ANALYSIS:

Functional Analysis:
User will provide a number.
Empty or zero value: "Invalid input, please enter a positive integer."

Technical Analysis:
Entity Name: PowerOfTwoChecker
State: Data types - INT, Error messages - STRING
Behavior: Operators - WHILE, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a number is provided and it's a positive integer.
2. Use a loop to divide the number by 2 until it becomes 1.
3. If at any step, the number is not divisible by 2, it's not a power of two.

Programming Language:
State: Define the number given by the user.

Behavior:
1. Check if a number is provided and it's a positive integer.
2. Use a loop to divide the number by 2 until it becomes 1.
3. If at any step, the number is not divisible by 2, print "Not a power of two."
   Otherwise, print "Power of two."
'''

print("Q23 PowerOfTwoChecker")

num = int(input("Enter Number: "))

if num > 0:
    original_num = num

    while num > 1 and num % 2 == 0:
        num /= 2

    if num == 1:
        print(f"{original_num} is a power of two.")
    else:
        print(f"{original_num} is not a power of two.")
else:
    print("Invalid input, please enter a positive integer.")
