'''
3. Remove odd index values
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

I. REQUIREMENT GATHERING: Remove odd index values
        ------------------------------------
        |    Enter String: |_________|      |
        |    stapy index:  |_____|          |
        |    end index:   |_____|           |
        |            Submit                 |
        |___________________________________|

II. ANALYSIS:
    1. Functional Analysis:
    Customer will give string, stapy index and end index from which 
    the slicing happens 

    scenarios:    Empty string  Ex: ""  : "Invalid String"
                  single string Ex: "E" : "Enter at least 2 characters"
                  Empty stapy and end index Ex: "" : "Invalid stapy or end index"
    Including space? ==> Include
    only numbers allowed = No
    special chars = No

    2. Technical analysis:
    Entity Name: StringSlicing

        State : Data types/strs: STRING INT

        Behaviour: operators : 
                    DM       : if elif else
                    Loops    :
III. DESIGN (Sequence diagrams):

Mathematics:

1. check string entered is not empty and single character
2. check stapy and end is not empty
3. if both condition satisfied take stapy and end index do slicing.
print sliced string

programming language:

STATE:
1. define string, stapy, end index given by user
str1 = 'Hello world'
stapy = 4, end = 10

BEHAVIOR:
2. check string, stapy, end not empty using conditions (if, elif, else)
3. take string, stapy, end index and perform slicing and return the output string
output: " world"

IV. DEVELOPMENT:

'''
# Algorithm
# STATE

if not string1.strip():
    print("Invalid string. Please enter a valid string.")
    continue
while True:
    try:
        stapy = int(input("Enter stapy index:"))
    except Exception:
        print("Type valid stapy index number")
        continue
    break
    while True:
        try:
            end = int(input("Enter end index:"))
        except Exception:
            print("Type valid end index number")
            continue
        break

# BEHAVIOUR

if len(string1) == 0:
    print("Invalid string")
elif len(string1) == 1:
    print("Enter at least 2 characters")
else:
    print(string1[stapy:end])