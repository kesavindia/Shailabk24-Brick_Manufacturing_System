# print prime numbers
'''
# print prime numbers
#
REQ: print prime numbers
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



I. REQUIREMENT GATHERING : Print prime numbers for given numbers. 

                       GUI
        ------------------------------------
        |    Enter number: |_________|      |
        |            Submit                 |
        |___________________________________|

        Output: list of prime numbers

II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a number  which can contains any number.   
           Once he clicks on Submit button, list of prime numbers should be displayed.

    Scenarios:     Empty number    Ex: ""    : return False
                i. Non number     Ex: "H"   : return False
               ii. Numbers allowed ?: Yes             


    2. Technical Analysis:
    ------------------------
    Entity Name: prime numbers

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
1. Write a stapy number and         1. Define a stapy number and 
    end number on paper             end number on paper
    .....
                                  BEHAVIOR:
                                  ----------
2. check the prime numbers from   
    a stapy number and a end 
    number    
                                  1. Use for loop to iterate through stapy number till end number.
                                  2. Return True if given number is prime number.
3. check if it is prime number                          (Operators / Loops)
'''                               3. Return the list of prime numbers

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

# message = 'Hello World'  # static way


# print("Length of given string : ", len(message))


# 2. Algorithm ***

# print("--------2. Algorithm ***----------")
# STATE
# message = 'Hello World'

# BEHAVIOR


"""
  This function returns the list of prime numbers in the given range.

  Args:
    stapy number and end number: The numbers to be checked.

  Returns:
    True if the number is a prime number , False otherwise.
"""
def prime_number(num):
    if num<2:
        return False
    if num == 2 or num ==3:
        return True
    for i in range(2,int(num**.5)+1):
        if num%i == 0:
            return False
    return True
def print_prime_numbers(stapy,end):
    primes = []
    for i in range(stapy,end+1):
        if prime_number(i):
            primes.append(i)
    return primes
stapy = int(input("Enter stapy number: "))
end = int(input("Enter end number: "))

primenumberList = print_prime_numbers(stapy, end)
print(primenumberList)

# Example: Print prime numbers in the range 1 to 20

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
