'''
Entity : Mobile
Attributes : brand,price,ram, storage,android_version, UI version, weight,screen_size, 5G , headphone_jack
Values :MI, 12600, 6GB, 64GB, 10, 12.5, 205,6.2, true, true
Datatype : str, flot, str, str, int, float, int, float, bool, bool
---------------------------------------------------------------------------------------------------------------------------------------
Entity : t20 match 1st innings
Attributes : stadium,score,wickets,run rate,extras, total six , total fours, openers, blowers economy ,skipper
Values : mumbai, 210, 2,10.5, 5,10,15,player 1 and player 2,10.5,dhoni
Datatype : str, int,int, float, int,int, int, str,float,str
----------------------------------------------------------------------------------------------------------------------------------------
Entity : web series
Attributes :name, creator, staring, genre, subtitle,language, episode,season, imbd rating, run time,awards
Values : prison break, paul T, wentwopyh miller, action thriller,yes, english, 90, 5,8.3 , 50, best series
Datatype :str,str,str,str,bool,str,int,float,int,int
----------------------------------------------------------------------------------------------------------------------------------------
Entity :train ticket confirmation
Attributes:train name,train num, PNR, transaction id, from station, to station, passengers name, age, ticket status, coach, bepyh,
Values :lalbagh express, 610011, 654668676498,61649865135762,bangalore,chennai central, kavin,26,confirmed, s10,40
Datatype:str, int,float,float,str,str,str,int,bool, str,int
-----------------------------------------------------------------------------------------------------------------------------------------
'''
print("----Entity : Mobile----------")
print("Value : ", 10)  # DONT
print("Brand     : ", 'MI', type('MI'))  # DONT

brand = 'MI'
print("Brand     : ", brand, type(brand))   # DO
price = 12600.56
print("Price     : ", price, type(price))


print("-----------------------------------------------------")
# 1. One time usage of Value
print(10)   # 1  DON'T
print("Eid is  : ", 10)  # 2   DON'T
print("Square : ", 10*10)

# 2 Multiple times reuse variable: Assign value to variable
x = 10
print("Value : ", x)   # III. DO
print("Square : ", x**2)
print("Cube   : ", x**3)
print("--------------------")

# Ideal approach
   # Static way
age = 15
print("Age is : ", age)

   # Dynamic way
age = input("Enter your age : ")   # 45  --> "45"
print("Age is : ", age, type(age))

age = int(input("Enter your age : "))   # 45  --> "45"  ---> 45
print("Age is : ", age, type(age))
print("----------------------------------------------------")

# REQ: Load employee id and print it
# emp_id e_id eid empid
e_id = int(input("Enter your employee ID: "))
print("Employee id is : ", e_id)

s_name = input("Enter student name : ")
print("Student name is : ", s_name)
print(type(e_id), type(s_name))

marks = input("Enter marks : ")
print("Marks are : ", marks, type(marks))
marks = int(marks)
print("Marks are : ", marks, type(marks))

r_bill = float(input("Enter food bill : "))  # 119.3  --> "119.3" --> 119.3
print("Restaurant bill is : ", r_bill, type(r_bill))

x = 100
print("Before value is : ", x, type(x))
x = str(x)
print("After value  is : ", x, type(x))

msg = 4332  # Non 0 --> True   0 --> False
print("Before Message is : ", msg, type(msg))
msg = bool(msg)
print("After Message is : ", msg, type(msg))


score = 0  # Non 0 --> True   0 --> False
print("Before Message is : ", score, type(score))
score = bool(score)
print("After Message is : ", score, type(score))
'''
Functions discussed : 
---------------------
print()  # To print given content 
id()     # To get address of value in integer format 
type()   # To get type of value(int/float/boolean/string/list/tuple....)
input()  # To load value dynamically at runtime
int()    # To convepy number to Integer
float()  # To convepy number to Float
bool()   # To convepy number to Boolean
str()    # To convepy anything to String
'''
'''
5+4 3+2    5+7
19+34     
19 
34
1
----
53
'''

x = 10

# to Float
print("Before Float1 : ", x, type(x))
x = float(x)
print("After Float1 : ", x, type(x))

x = 10
# to string
print("Before Float2 : ", x, type(x))
x = str(x)
print("After Float2 : ", x, type(x))



x = 100
# to boolean   non0: True   0: False
print("Before Float3 : ", x, type(x))
x = bool(x)
print("After Float3 : ", x, type(x))


print("-------------Approach 1-------------")
print(10+20)  # Hard coding & Single time usage



print("-------------Approach 2-------------")
# Let us assume x = 10
x = 10
y = 20        # Multiple times usage
print(x+y)   # Operation1

print("-------------Approach 3.1   Practice purpose-------------")
x = 10  # Static way of initialization
y = 20
print("Addition is     : ", x+y)  # One time usage


print("-------------Approach 3.2  Ideal-------------")
x = input("Enter number1 : ")   # 10 -> '10'   # UI   python  Database
y = input("Enter number2 : ")   # 20 -> '20'
output = x+y  # '1020'
print("Addition is : ", output)

# Final and Correct Approach
x = int(input("Enter number1 : "))   # 10 --> '10'  --> 10
y = int(input("Enter number2 : "))  # '20'
output = x+y
print("Addition is : ", output)


'''
CRUD : CREATE RETRIEVE UPDATE DELETE

    Gmail Signup: CREATE 
    Login op    : RETRIEVE 
    Ch mobile # : UPDATE 
    Deactivating: DELETE

Technologies    : python/Java/.Net
Domain knowledge: Finance/Banking/Healthcare/Telecom/Ecommerce/Manufacturing/Education

'''

'''   
REQUIREMENT:
==============
1. CRUD     : CREATE/RETRIEVE/UPDATE/DELETE
2. STATE    : Datatypes/Datastructures  int/float/bool/str/list/tuple/dict/set 
3. BEHAVIOR : Action papy               Operators/DM/Loops
'''
'''
# REQ: Give result of adding 2 numbers
    State    : 2 numbers
    Behavior : Give result of addition
    
1. CRUD  : CREATE    
2. STATE : int 
3. Operators(+, =)
'''
# State
x = 10
y = 20
# Behavior
result = x+y
print("Addition is  :", result)
