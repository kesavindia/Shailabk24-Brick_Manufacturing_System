'''
22 Create a program to calculate the average of N numbers.

REQUIREMENT GATHERING:

--------------------------------------
| Enter N:      |______________|     |
|           Submit                    |
|____________________________________|

ANALYSIS:

Functional Analysis:
User will provide the count (N) of numbers.
Empty or zero value: "Invalid input, please enter a positive number."

Technical Analysis:
Entity Name: AverageCalculator
State: Data types - INT, Error messages - STRING
Behavior: Operators - FOR, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if N is provided and it's a positive number.
2. Use a loop to input N numbers.
3. Calculate the sum and average of N numbers.
4. Print the average.

Programming Language:
State: Define N given by the user.

Behavior:
1. Check if N is provided and it's a positive number.
2. Use a loop to input N numbers.
3. Calculate the sum and average of N numbers.
4. Print the average.
'''


print("Q22 AverageCalculator")

n = int(input("Enter N: "))

if n > 0:
    sum_of_numbers = 0

    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        sum_of_numbers += num

    average = sum_of_numbers / n

    print(f"Average of {n} numbers: {average}")
else:
    print("Invalid input, please enter a positive number.")

