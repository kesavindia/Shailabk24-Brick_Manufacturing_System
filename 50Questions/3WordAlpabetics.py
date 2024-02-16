'''Write a program that prompts the user to enter three names.
Your program should display the names in descending order.'''
'''SDLC Phases:
------------
    I. REQUIREMENT GATHERING
    II. ANALYSIS
            1. Functional Analysis
            2. Technical Analysis        
    III. DESIGN
    IV. DEVELOPMENT
    V.  TESTING
    VI. DEPLOYMENT/PRODUCTION


I. REQUIREMENT GATHERING : Display the names in descending order
        ------------------------------------
        |    Enter String: |_________|      |
        |            Submit                 |
        |___________________________________|

II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give 3 Strings, Here we should display the 
    names in alphabetically descending order

    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "Enter at least 2 characters"
               ii. Single word     Ex: "Hello" ==>  H:1, e:1, l:2, o:1
              iii. Multiple words  Ex: "Hello World Welcome to python"
                                               ==> H:2, e:2...... " ":4
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Including space?  ==> Space not allowed
               vii. Only Numbers allowed ?  No
               viii. Special chars   ==> No


    2. Technical Analysis:
    ------------------------
    Entity Name: Descending order

            State   : Data types/strs:  STRING 

            Behavior: Operators      :  NA
                      DM             :  NA
                      Loops          :  NA '''

print("Q10 NameSorter")

name1_input = input("Enter Name 1: ")
name2_input = input("Enter Name 2: ")
name3_input = input("Enter Name 3: ")

if not name1_input or not name2_input or not name3_input:
    print("Invalid input, please enter all three names.")
else:
    names = [name1_input, name2_input, name3_input]
    names.sort(reverse=True)
    print("Names in descending order:", names)
