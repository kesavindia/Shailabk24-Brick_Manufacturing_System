# sum all the numbers in a list

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

I. REQUIREMENT GATHERING: Get a list of numbers from user
        ------------------------------------
        |    Enter numbers: |_________|    |
        |                                   |
        |            Submit                 |
        |___________________________________|

II. ANALYSIS:
    1. Functional Analysis:
    Customer will give a number(n) whose first n fibonacci series shall be returned.


    scenarios:    Empty list  Ex: []  : "Invalid literal"
                  only one element   Ex: [3] : "Return same"
                   other than numbers Ex:"f"  : "Invalid number"

    only numbers allowed = Yes
    special chars = No

    2. Technical analysis:
    Entity Name: sum_of_list

        State : Data types/strs: INT

        Behaviour: operators :
                    DM       : if elif else
                    Loops    : for loop
III. DESIGN (Sequence diagrams):

Mathematics:

1. check number entered is not empty or invalid literals
2. Get the numbers and provide the sum

programming language:

STATE:
1. get a list of numbers given by user


BEHAVIOR:
2. check the number if it is empty or only one number.(if, elif, else)
3. take input number and perform addition and return the sum of numbers
output: sum

IV. DEVELOPMENT:

'''


# Algorithm
# STATE


# BEHAVIOUR
# Get the number of numbers from the user
num_numbers = int(input("Enter the number of numbers to sum: "))

# Initialize an empty list to store the numbers
numbers = []

# Get the numbers from the user
for i in range(num_numbers):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Calculate the sum of the numbers
sum = 0
for number in numbers:
    sum += number

# Print the sum
print(f"The sum of the numbers is: {sum}")

