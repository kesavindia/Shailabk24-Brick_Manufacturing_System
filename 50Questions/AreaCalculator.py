'''
32 Create a program to calculate the area of different geometric shapes (circle, rectangle, triangle).

ANALYSIS:

Functional Analysis:

User will select a geometric shape (circle, rectangle, triangle) to calculate its area.
Empty value: "Invalid input, please select a shape."
Data types: INTEGER for shape selection, FLOAT for dimensions.
Number of values allowed: 1 shape selection, dimensions based on the selected shape.
Special characters: Not applicable
Technical Analysis:

Entity Name: AreaCalculator
State: Data types - INTEGER, FLOAT; Error messages - STRING
Behavior: Mathematical formulas for calculating the area of each shape; Control Flow - IF, ELIF, ELSE
DESIGN (Sequence Diagrams):

Algorithm:

Check if a shape is selected.
Depending on the selected shape, calculate the area using the corresponding formula.
Print the result.
Programming Language:

State: Define shape selection and dimensions given by the user.
Behavior:

Check if a shape is selected.
Depending on the selected shape, calculate the area.
Print the result.

'''

import math

# Prompt the user to select a shape
print("Select Shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

# Get the user's choice for the shape
shape_choice = int(input("Enter your choice (1-3): "))

# Check if a shape is selected
if not shape_choice:
    print("Invalid input. Please select a shape.")
else:
    # Depending on the selected shape, prompt for dimensions and calculate the area
    if shape_choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius**2
    elif shape_choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
    elif shape_choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
    else:
        print("Invalid choice. Please select a valid shape.")

    # Print the result
    if shape_choice in [1, 2, 3]:
        print(f"Area of the selected shape: {area}")
