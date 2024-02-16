# Print maximum of three given numbers
'''

#
REQ: Print maximum of three given numbers
'''

'''
SDLC Phases:
------------
    I. REQUIREMENT GATHERING
    II. ANALYSIS
            1. Functional Analysis
            2. Technical Analysis        
    III. DESIGN
    IV. DEVELOPMENT
    V.  TESTING
    VI. DEPLOYMENT/PRODUCTION



I. REQUIREMENT GATHERING : Print factorial of given number 

                       GUI
        ------------------------------------
        |    Enter numbers: |_________|      |
        |            Submit                 |
        |___________________________________|

        Output: maximum of three numbers

II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give three numbers.  
           Once he clicks on Submit button, maximum of the numbers should be displayed.

    Scenarios:     Empty number    Ex: ""    : return False
                i. Non number     Ex: "H"   : return False
               ii. Numbers allowed ?: Yes             


    2. Technical Analysis:
    ------------------------
    Entity Name: maxNumber

            State   : Data types/strs:   INT

            Behavior: Operators      :  <= %
                      DM             :  if else
                      Loops          :  Yes (For Loop) range function

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write a  number                      1. Define a number 
    on paper             
    .....
                                  BEHAVIOR:
                                  ----------
1. calculate maximum of           1. Calculate the factorial of number 
    three numbers                 2. Return factorial
                                    (Recursion)                             


'''
'''
IV. DEVELOPMENT:
=================
        1. Builtin Functions
        2. Algorithm **       : 150 / 220
        3. Functions  : 40
        4.OOPS        : 20     5. EH  : 10    6. FH  : 5       
        7.Database    : 3      8. UI  : 3
'''
# 1.Builtin functions

# print("-----1. Builtin Functions--------")

# factorial= 1*2...n  # static way


# print("Factorial of given number : ",factorial)


# 2. Algorithm ***

# print("--------2. Algorithm ***----------")
# STATE
# factorial_of_number

# BEHAVIOR


"""
  This function returns the max of 3 numbers.

  Args:
    number: 3 integer numbers

  Returns:
 maximum of given 3 numbers.
"""


def max_num(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else: return c
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

maxnumber = max_num(num3,num2,num1)
print((maxnumber))



# 3 Using Functions  ==>   40
# print("--------3 Using Functions----------")
# 4 OOPS  ==> 10
# print("--------4 Object Oriented----------")
# 5 Exception handling  ==> 5
# print("--------5 Exception handling----------")
# 6 File Handling  ==> 3
# print("--------6 File Handling----------")
# 7 Database interaction MVC  ==> 10
# print("--------7 Database interaction----------")
# 8 UI Interaction   ==> 3
# print("--------8 UI Interaction----------")
