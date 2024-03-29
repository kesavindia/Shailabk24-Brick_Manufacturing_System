

# Function Definition categories
''''''
'''
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type

T T 
T F
F T
F F
'''

# Sum functionality

print("------------CAT 1  --- w P -- w R-------------------")
# 1st -> T T :: Function with parameters, with return type
num1 = 10
num2 = 20

def sum(n1, n2):
    res = n1 + n2
    return res

print("Addition is : ", sum(num1, num2))  # print(10)

output = sum(num1, num2)                  # x = 10   print(x)
print("Addition is : ", output)


print("------------CAT 2 --- w P  --- wo R-------------------")

# 2nd -> T F :: Function with parameters, without return type

num1 = 10
num2 = 20

def sum(n1, n2):
    res = n1 + n2
    print("Addition is : ", res)

sum(num1, num2)
print("Second cat : ", sum(num1, num2))  # No use

print("------------CAT 3 --- wo P --- w R-------------------")


# 3rd --> F T :: Function without parameters, with return type

def sum():
    n1 = 10
    n2 = 20
    res = n1 + n2
    return res

output = sum()
print("Addition is : ", output)

print("------------CAT 4 --- wo P wo R -------------------")

# 4th  --> F F  :: Function without parameters, without return type

def sum():
    n1 = 10
    n2 = 20
    res = n1 + n2
    print("Addition is : ", res)

sum()
print("Cat 4 : ", sum())  # No use



x = 10.5
print(int(x))


'''
variable             paramater
==================================
num1                 n1 
emp_id               eid e_id
e_name               name ename 
salary               sal 



n1                   num1
'''
smarks = int(input("Enter marks : "))

def get_student_marks(marks):
    if marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    elif marks >= 35:
        return "Third Class"
    else:
        return "FAIL"

result = get_student_marks(smarks)
print("Student result is : ", result)


def add():
    return 1, 2, 3

print("Value : ", x)


# Student result
marks = 55

def get_stresult(m):
    if m >= 60:
        return "First Class"
    elif m >= 50:
        return "Second Class"
    else:
        return "Third Class"

result = get_stresult()
print("Result is : ", result)