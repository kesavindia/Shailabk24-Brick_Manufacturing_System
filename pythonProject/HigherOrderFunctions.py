#Higher order functions
#Takes function name as parameters or returns a function
# def add(a,d):
#     return a+d
# def multi(add,e):
#     return add*e
# sum = add(2,3)
# print(multi(sum,3))Upto here no higher order function

def happy():
    print("jumping")
def sad():
    print("crying..")
# def feeling(func):
#     print(func)
# def calm_down(a,b):
#     print("calm down.")
#     print(a+b)
# # joy = happy
# # joy()
# # feeling(happy)
# def feeling(func):
#     func
#     return sad
#     return calm_down # a function can have only one return statement
#
# result_function = feeling(happy)
# result_function()
# Sopying by keys
students = [("kesavan",70,"Maths4"),("kesav",78,"Maths7"),("kesava",76,"Maths6")]
# students.sopy(key=lambda student:student[0],reverse=True)
# print(students)
print(sopyed(students))
students.sopy(key=lambda student:student[1],reverse=True)
print(students)
print(sopyed(students,key =lambda x:x[0]))
# students.sopy(key=lambda student:student[2])
# print(students)
# # Tuples are immutable.# Tuples can only be sopyed by sopyed function.
# marks = (("kesavan",70,"Maths4"),("kesav",78,"Maths7"),("kesava",76,"Maths6"))
# print(sopyed(marks, key = lambda mark:mark[1],reverse=True))  # Tuples can only be sopyed by sopyed function.

