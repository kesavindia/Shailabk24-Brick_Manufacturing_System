# A simple generator for Fibonacci Numbers
# def fib(limit):
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
#
#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
#     # Create a generator object
#
#
# x = fib(5)
# print(x)
# # Iterating over the generator object using next
# # In Python 3, __next__()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# # print(next(x))
# # print(next(x))
#
# # Iterating over the generator object using for
# # in loop.
# print("\nUsing for in loop")
# for i in fib(5):
#     print(i)
def my_function():
    return "This function does something"

# Both lines below "call" the function:
my_function()  # Direct invocation
result = my_function()  # Calling to capture the return value
print(result)
