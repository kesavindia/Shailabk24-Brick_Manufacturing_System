'''
I. REQUIREMENT GATHERING : Find Length of longest string in python.



II. ANALYSIS:
    1.Functional Analysis:
        The user wants to find the length of the longest string in a list.
        The list can contain strings with various characters: numbers,
        alphabets, special symbols, etc.


    Scenarios:
        Empty string in the list: Ex: "" → Output: "Invalid String"
        Single character in the list: Ex: "H" → Output: "Enter at least 2 characters"
        Single word in the list: Ex: "Hello" → Output: Length of the string
        Multiple words in the list: Ex: "Hello World Welcome to python" → Output: Length of the longest string
        Combination of characters in the list: Ex: "Hello1234%^&%$!bangalore" → Output: Length of the longest string
        Multiline string in the list: Ex: "hello world, bangalore, python\nhello programming\nworld language" → Output: Length of the longest string
        Including space? → Don't include spaces in the length calculation.
        Only numbers allowed in the list? → No restrictions

    2.Technical Analysis:

    Entity Name: LongestStringLength
    State:
        Data Types: LIST, STRING, INT
    Behavior:
        Operators: =, +=
        Decision-Making: if
        Loops: For Loop

Design (Sequence Diagrams):
Mathematics:
    Write the problem on paper: ["", "H", "Hello", "Hello World Welcome to python", "Hello1234%^&%$!bangalore"]
    Initialize the length of the longest string as 0.
    Iterate through each string in the list.
    For each string, initialize the count as 0.
    Traverse through each character, incrementing the count for each non-space character.
    Update the length of the longest string if the current string is longer.
Programming Language:
    State:
        Define the list: strings_list = ["", "H", "Hello", "Hello World Welcome to python", "Hello1234%^&%$!bangalore"]
        Initialize the length of the longest string as 0.

    Behavior:
        Use a for loop to iterate through each string in the list.
        For each string, initialize a counter as 0.
        Use another for loop to iterate through each character, incrementing the counter for each non-space character.
        Update the length of the longest string if the current string is longer.
        Print the length of the longest string.
'''
# Development

# STATE
string_list1 = input("Enter the elements of the list, separated by commas: ")
string_list = string_list1.split(',')

# BEHAVIOR
longest_length = 0
longest_string = ""

for string in string_list:
    current_length = 0
    for char in string:
        current_length += 1
    if current_length > longest_length:
        longest_length = current_length
        longest_string = string

print("Length of the longest string:", longest_length)
print("Longest string:", longest_string)

