#Lambda functions are anonymous functions
#
# add = lambda x:x+1
# print(add(2))
# product = lambda a,b,c:a*b*c
# print(product(1,2,3))
# is_higher = lambda h:h>=165
# print(is_higher(165))
# print(is_higher)

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

person = {"age": 30,"name": "Alice", }

greet(**person)