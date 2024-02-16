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
2. check the number if it is 0 or 1(if, elif, else)
3. take input number and perform recursion function and return the series of numbers
output: 0,1,1,2,3.....

IV. DEVELOPMENT:

'''
# Algorithm
# STATE


# BEHAVIOUR
def fibonacci(n):
    if not isinstance(n,int):
        raise ValueError("Enter a valid numbers only.")
    elif n<0:
        raise ValueError("Enter positive numbers only.")
    elif n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
try:
    n = int(input("Enter a number: "))
    fib_series = [fibonacci(i) for i in range(n)]
    print(fib_series)
except ValueError as e:
    print(f"Error:{e}")

