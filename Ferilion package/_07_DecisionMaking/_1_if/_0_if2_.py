'''
Decision Making:
'''
print("Int to Boolean : ", bool(10))
print("Float to Boolean : ", bool(10.5))
print("String to Boolean : ", bool("Hello"))
print("List to Boolean : ", bool([1, 2, 3]))
print("Tuple to Boolean : ", bool((1, 2, 3)))
print("String to Boolean : ", bool(""))
print("List to Boolean : ", bool([]))
print("Tuple to Boolean : ", bool(()))


'''
0 vs None
----------------
    0    -  Value and is applicable
    None -  NoValue and is not applicable 
    
    Employee: Permanent : eid, name, salary: 0
              Intern    : eid, name, salary: None


# True ==> non-zero           not None
           3,-5,6,4.5,-3.6    'M' [1,2] (1,) {1:1,2:2}, {1,2,3}

# False ==> 0                  None
                               ''  [] () {} set({})

 True       False
 ----------------
 Non 0   :  0
 ----------------
 nonNone :  None

 Non 0 : 34, 432, -454, 500, 1, -1  : True
     0 : 0 : False

nonNone: 'hello' [1,2,3],(1,2), {1:1,2:2}, {1,2,3}
None   : ''  [] () {} set({})

 Operators:
 --------------
    0 vs Non 0:
    ============
    Arithmetic* :10+20 --> 30 : True
                 10-10 -->  0 : False
                 10-20 -> -10 : True
                 
    Assignment   x = 10       : True
                 x = 0        : False
                 
    True vs False:
    ===============
    Relational   10 > 20      : False
                 5  < 10      : True
                 10 == 10     : True
                 5 != 6       : True

    Logical     True and False: False
                True and True : True
                True or False : True
                False or True : True
                not False     : True
                
    Membership  1 in {1,2,3}  : True
                1 in {4,5,6}  : False
                
    Identity    is is not     : True/False


               
    None vs Not None:
    =================
                x = None      : False
                ----------------------
                str1 = ''     : False
                str1 = 'hello': True
                li = []       : False
                li = [1,2,3]  : True
                t1 = ()       : False
                t1 = (1,2,3)  : True
                di = {}       : False
                di = {1:1}    : True
                s1 = set({})  : False
                s1 = {1,2,3}  : True

'''
num = 10  # Static way or Hard coding

num = input("Enter number  :")   # 100 --> '100'
print("Number: ", num, type(num))

num = int(input("Enter number  :")) # 100 --> '100'   ---> 100
print("Number: ", num, type(num))

msg = input("Enter Message  :")
print("Message is : ", msg, type(msg))


# Decision Making
'''
If papyicular condition is True ==> Implement Logic 
else  if condition is False     ==> Implement some other logic 

1 Condition  :    if 
2 Conditions :    if else 
3 Conditions :    if elif else
4 Conditions :    if elif elif else


                           SSC Exam
                PASS                                FAIL    
            Continue  Drop                      Retry    Drop
  
                            Result: 
                    PASS                  FAIL 
                Continue Drop          Retry Drop    

if PASS:
    if Continue:
    else:
else:
    if Retry:
    else:
    
    
Watch a Movie:
---------------
if Movie:
    if Laptop:
        if OTT:
            if Netflix:
                # logic 
            elif Amazon:
                # logic
            elif hotstar:
            
        elif System:
    elif TV:
        Channel1:
            # logic
            
    elif Mobile:
    elif Theater:
        if BenifitShow:
            if Ticket:
            elif Black:
            else:
        elif Morning:
        elif Evening:
    elif Projector: 
    elif Tab:
    else:
        print("No options")
       
       
if movie:
   if netflix:
        10 lines 
             
        
.............
Nested if mechanism

# if syntax
--------------
if <condition>:                    if <condition>{ 
    # body                           # body
                                    }
'''

# REQ: Print customer given number : No conditions
'''
REQ: Print the number 
    State: Customer given number 
    Behavior: Print it 
'''
# STATE
num = int(input("Enter number : "))
# BEHAVIOR
print("Number is  :", num)



'''
Entity : Employee 
------------------
STATE:
    Attributes: eid, name, sal, address, company, mobile, email
    Values     :100, Madhu, 5000, 'Bangalore', 'ORACLE', '4234324324', 'afddfds@oracle.com'
    type       : int, str, float, str, str,str,str

Java  : type attr = value    int eid = 100
python:      attr = value        eid = 100




'''
#
'''

SDLC Process:
--------------
1. Requirement Gathering
2. Analysis
        - Functional
        - Technical 
3. Design 
4. Development 
5. Testing 
6. Deployment 

REQ: Print if Customer given number is greater than 10
Operation: CRUD : CREATE
Entity   : Noun : Number

    State   : Customer given number
    Behavior: Print it 
                    ==>  if it is greater than 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is greater than 10   : Behavior
 3. If val > 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number   (NOUN)  : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is greater than 10    (VERB)
                    = >     if     

  Entity  :    Customer         
  State   :    given number 
  Behavior:    Print it if number is  > 10
 
 English :  if the given number is greater than 10 then print it.
 python  :  if       num                  >     10:
                    print("") 
'''
# State
num = int(input("Enter number10 : "))
# Behavior
if num > 10:
    print("Number is : ", num)  # if block
    print("--I am in if block----")

print("-----End of Program-----")




# State
num = int(input("Enter number2 : "))
# Behavior
if num > 10:
    print("Number is : ", num)

# REQ ****: Check and print if Customer given number is greater than 10
'''
State: Customer given number
Behavior: Print it 
            ==>  if  is greater than 10

Functional Analysis:
---------------------
 1. Customer will give number        : STATE 
 2. Check if it is greater than 10   : Behavior
 3. If val > 10 ==> Print it 

Technical Analysis: 
--------------------
  1. STATE    :  Datatypes/Datastructures   : Customer given number   (NOUN)  : int
  2. BEHAVIOR :  Operators, DM, Loops       : Check if it is greater than 10    (VERB)
                      >     if 
'''
print("---------1----------")
# STATE
num = int(input("Enter value : "))

# BEHAVIOR
if num > 10:  # if Customer given number is greater than 10
    print("Yes it is greater : ", num)   # Indentation 4 spaces in block

print("-----------------------End of program-----------------------")


print("---------2----------")
# I. REQ ****: Print whether given number is Even or Odd.
'''
CRUD      : CREATE
State*    : int 
Validation: Client/Server
Behavior* : Operators,    DM,        Loops 
            = % ==      if else        --

II. Analysis:
==================
    Functional Analysis:  
        1. Customer will give number 
        2. Check whether it is even or odd
        3. Print it accordingly
    Technical Analysis: 
        STATE   : int 
        Behavior: Operators,  DM,          Loops 
                  % ==       if else

III. Design: (Sequence Diagrams):  
=============
    Maths Solution:
    ---------------
        As given   x = 43       # STATE
        x % 2 = 45 % 2         # Behavior
              = 1
        As reminder is 1, given value is Odd Number
        -----------------------------------------------------
        As given  x = 22       # STATE
        x % 2 = 22 % 2         # Behavior
              = 0
        As reminder is 0, given value is Even Number
        ------------------------------------------------------

'''
# IV. DEVELOPMENT :

# State
num = int(input("Enter number : "))
print("Given number is : ", num)

# Behavior : Skeleton Structure

if num % 2 == 0:
    print("Even number : ", num)
else:
    print("Odd number : ", num)



if num % 2 == 0:
    print("And it is EVEN")
else:
    print("And it is ODD")

print("-----------End of Program--------------")

# 10 conditions   : 4 sub conditions
'''
if cond1:
    if sc1:
        pass
    elif sc2:
        pass
    elif sc3:
        pass
    else:
        pass
elif cond2:
    pass
    
# Watching Movie:
----------------
if Theater:
    if Money:
        if Multiplex:
            pass
        eilif SingleScreen:
            pass
    else:
        
elif TV:
    pass
elif Laptop:
    pass
elif Mobile:
    pass
    
    
....
.....
else:
    pass
    
    
if Theater:
    if Money:
        if Multiplex:
            if online:
                body 
            elif cash:
    
    
    
    
'''



'''

# Behavior
if num % 2 == 0:
    print("Even number : ", num)
else:
    print("Odd number : ", num)

'''

print("---------3----------")

# REQ: Check whether given number is Positive or Negative or Zero      # if elif else

# State
num = int(input("Enter number : "))

# Behavior
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# BEHAVIOR
if num > 0:
    print("Positive number", num)
elif num < 0:
    print("Negative number", num)
else:
    print("-----Zero-----", num)


