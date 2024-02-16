'''
19 Implement a program to reverse a string without using built-in functions.

REQUIREMENT GATHERING:

--------------------------------------
| Enter String: |______________|     |
|           Submit                    |
|____________________________________|

ANALYSIS:

Functional Analysis:
User will provide a string.
Empty value: "Invalid input, please enter a string."

Technical Analysis:
Entity Name: StringReverser
State: Data types - STRING, Error messages - STRING
Behavior: Operators - FOR, WHILE, IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a string is provided.
2. Use loops to reverse the string.
3. Print the reversed string.

Programming Language:
State: Define a string given by the user.

Behavior:
1. Check if a string is provided.
2. Use loops to reverse the string.
3. Print the reversed string.
'''


print("Q19 StringReverser")

string_input = input("Enter String: ")

if string_input:
    reversed_string = ""
    index = len(string_input) - 1

    while index >= 0:
        reversed_string += string_input[index]
        index -= 1

    print("Reversed String:", reversed_string)
else:
    print("Invalid input, please enter a string.")
