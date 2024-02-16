# def square(x):
#     return x * x
#
# def apply(func, value):
#     return func(value)
#
# result = apply(square, 5)
# print(result)
# def greet(name):
#     return f"Hello, {name}!"
#
# greeting = greet
# print(greeting("John"))
# def multiply_by(factor):
#     def multiplier(x):
#         return x * factor
#     return multiplier
# # multiplier(3)
# double = multiply_by(2)
# print(double(5))  # Output: 10
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = {
    'add': add,
    'subtract': subtract
}
result = operations.get('add')(5, 3)
print(result)
print(operations['subtract'](10,5))

