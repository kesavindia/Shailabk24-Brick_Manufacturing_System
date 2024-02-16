'''28.Create a program to simulate a simple calculator with basic operations.
ANALYSIS:

Functional Analysis:

User will provide two numbers and select an operation to perform.
Empty value: "Invalid input, please enter all required values."
Data types: FLOAT for numbers, INTEGER for operation selection.
Number of values allowed: 2 numbers and 1 operation selection
Special characters: Allowed
Technical Analysis:

Entity Name: SimpleCalculator
State: Data types - FLOAT, INTEGER; Error messages - STRING
Behavior: Operators - Mathematical operators (+, -, *, /); Control Flow - IF, ELIF, ELSE
DESIGN (Sequence Diagrams):

Algorithm:

Check if two numbers and an operation are provided.
Perform the selected operation.
Print the result.
Programming Language:

State: Define two numbers and an operation given by the user.
Behavior:

Check if two numbers and an operation are provided.
Perform the selected operation.
Print the result.
'''
print("28.simple calculator")
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

# Prompt the user to select an operation
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

# Get the user's choice for the operation
operation = int(input("Enter your choice (1-5): "))

# Check if all values are provided
if all([num1, num2, operation]):
    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 - num2
    elif operation == 3:
        result = num1 * num2
    elif operation == 4:
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            result = num1 / num2
    elif operation == 5:
        exit()
    else:
        print("Invalid choice. Please select a valid operation.")
print("Result:", result)
