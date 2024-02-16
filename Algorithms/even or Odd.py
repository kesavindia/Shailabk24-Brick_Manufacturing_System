#check given number is even or odd
'''
REQ: check given number is even or odd
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



I. REQUIREMENT GATHERING : Find length of given string. 

                       GUI
        ------------------------------------
        |    Enter Number: |_________|      |
        |            Submit                 |
        |___________________________________|

        Output: Odd or Even

II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a number which can contains any  characters
           like numbers, alphabets, special symbols etc., and 
           It should consider only numbers.
           Once he clicks on Submit button, True or False should be displayed.

    Scenarios:    
              i. Including space/special chars?  ==> Function only takes numerical characters
             ii.  Numbers allowed ? Yes

    2. Technical Analysis:
    ------------------------
    Entity Name: Even or odd

            State   : Data types/strs:   INT

            Behavior: Operators      :  %
                      DM             :  if else
                      Loops          :  Yes (For Loop)

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
   number                           num = 123
    .....
                                  BEHAVIOR:
                                  ----------
2. consider only digits.            2. Initialize counter as 0
3. Traverse through each char     3. Use for loop to iterate through each char from both sides
   from               4. Return True if both side traversal is same.
4. check for equality                           (Operators / Loops)
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

# message = 'Hello World'  # static way


# print("Length of given string : ", len(message))


# 2. Algorithm ***

# print("--------2. Algorithm ***----------")
# STATE
# message = 'Hello World'

# BEHAVIOR


"""
  This function checks if a text is a palindrome using recursion.

  Args:
    text: The text to be checked.

  Returns:
    True if the text is a palindrome, False otherwise.
"""
def is_palindrome_recursive(text):
    text = text.lower()
    text=''.join(i for i in text if i.isalnum())
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome_recursive(text[1:-1])

text = input("Enter a text: ")
if is_palindrome_recursive(text):
    print(f"Given string '{text}' is palindrome")
else:
    print(f"Given string '{text}' is not palindrome")





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
