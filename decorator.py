# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator using the @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
# say_hello = my_decorator(say_hello)

# say_hello()
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(1):
#             func(*args, **kwargs)
#     return wrapper
#
#
# @decorator
# def greet(**kwargs):
#     print(f"Hello, {kwargs.get('name','hty')}!")
# greet(name ='kesavan')


# Python program to illustrate
# nested functions
def outerFunction(text):
    def innerFunction():
        print(text)
    return innerFunction


if __name__ == '__main__':
    fn = outerFunction('Hey!')
    fn()