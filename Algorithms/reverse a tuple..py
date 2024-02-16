# reverse a tuple.
'''
3. Get the first n fibonacci series
'''

'''
SDLC phases:

I. REQUIREMENT GATHERING
II. ANALYSIS
    1. Functional Analysis
    2. Technical Analysis
III. DESIGN
IV. DEVELOPMENT
V. TESTING
VI. DEPLOYMENT/PRODUCTION

I. REQUIREMENT GATHERING: Get a number from user
        ------------------------------------
        |    Enter a number: |_________|    |
        |                                   |
        |            Submit                 |
        |___________________________________|

II. ANALYSIS:
    1. Functional Analysis:
    Customer will give a number(n) whose first n fibonacci series shall be returned.


    scenarios:    Empty string  Ex: ""  : "Invalid literal"
                  zero or one   Ex: 0/1 : "Return same"
                   Ex: -Ve number : "Invalid number"

    only numbers allowed = Yes
    special chars = No

    2. Technical analysis:
    Entity Name: FibonacciSeries

        State : Data types/strs: INT

        Behaviour: operators : 
                    DM       : if elif else
                    Loops    : for loop
III. DESIGN (Sequence diagrams):

Mathematics:

1. check number entered is not empty or invalid literals 
2. Get the number and provide the Fibonacci series

programming language:

STATE:
1. define a number given by user


BEHAVIOR:
2. check the number if valid numbers(if, elif, else)
3. take input number and convepy into tuple perform reverse operation and return reversed tuple.
output: reversed 

IV. DEVELOPMENT:

'''


# Algorithm
# STATE
#input_element = tuple


# BEHAVIOUR
def get_tuple_from_user():
    try:
        # Prompt the user to enter the tuple elements separated by commas
        user_input = input("Enter the tuple elements separated by commas: ")

        # Convepy the user input string to a tuple
        tuple_elements = user_input.split(",")
        tuple_elements = [int(element) for element in tuple_elements]
        tuple_elements = tuple(tuple_elements)

        return tuple_elements
    except ValueError:
        print("Invalid input. Please enter a valid tuple.")
        return None
def reverse_tuple(tuple_elements):
    if not isinstance(tuple_elements, tuple):
        raise TypeError("Input must be a tuple")

    reversed_tuple = ()
    for element in tuple_elements:
        reversed_tuple = (element,) +reversed_tuple

    return reversed_tuple

# Get the tuple from the user
user_tuple = get_tuple_from_user()

if user_tuple:
    # Reverse the tuple
    reversed_tuple = reverse_tuple(user_tuple)
    print("Reversed tuple:", reversed_tuple)
else:
    print("Please enter a valid tuple to reverse.")


