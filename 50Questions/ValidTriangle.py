'''
43 A triangle is valid if the sum of all the three angles is equal to 180 degrees.
Write a program that asks the user to enter three integers as angles and check
whether a triangle is valid or not.

REQUIREMENT GATHERING:

---------------------------------------
| Enter Angle 1: |_________|          |
| Enter Angle 2: |_________|          |
| Enter Angle 3: |_________|          |
|           Submit                    |
|_____________________________________|

ANALYSIS:

Functional Analysis:
User will provide three angles.
Empty values: "Invalid input, please enter all three angles."
Sum not equal to 180 degrees: "Triangle is not valid."

Technical Analysis:
Entity Name: TriangleValidator
State: Data types - INT, Error messages - STRING
Behavior: Operators - IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if all three angles are provided.
2. Determine if the sum of angles is equal to 180 degrees.
3. Print the result.

Programming Language:
State: Define three angles given by the user.

Behavior:
1. Check if all three angles are provided.
2. Determine if the sum of angles is equal to 180 degrees.
3. Print the result.

'''

print("Q43 TriangleValidator")




angle1_input = input("Enter Angle 1: ")
angle2_input = input("Enter Angle 2: ")
angle3_input = input("Enter Angle 3: ")

if angle1_input.isdigit() and angle2_input.isdigit() and angle3_input.isdigit():
    angle1 = int(angle1_input)
    angle2 = int(angle2_input)
    angle3 = int(angle3_input)

    # Determine if the sum of angles is equal to 180 degrees
    is_triangle_valid = angle1 + angle2 + angle3 == 180

    # Print the result
    if is_triangle_valid:
        print("Triangle is valid.")
    else:
        print("Triangle is not valid.")
else:
    print("Invalid input, please enter all three angles.")

