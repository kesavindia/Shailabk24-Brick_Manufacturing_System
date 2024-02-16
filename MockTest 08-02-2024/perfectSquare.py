# '''write a program taht checks if a given number is a perfect square
# '''
# def is_perfect_square(n):
#
#   # Handle negative numbers and 0
#   if n < 0:
#     return False
#   elif n == 0:
#     return True
#
#   # Check if the square root of n is an integer
#   sqrt_n = int(n**0.5)
#   return sqrt_n * sqrt_n == n
#
# # Example usage
# number = int(input("Enter a number: "))
# if is_perfect_square(number):
#   print(f"{number} is a perfect square.")
# else:
#   print(f"{number} is not a perfect square.")

def decorator(func):
  def wrapper(*args):
    print(f"Result of {args[0]} and {args[1]} :")
    return func(args[0],args[1])
  return wrapper
@decorator
def add(x,y):
  return x+y
res = add(2,3)
print(res)