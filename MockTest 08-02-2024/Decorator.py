'''create a decorator to validate the input and provide instructions to perform factors of the given number'''
def validate_and_instruct(func):

  def wrapper(num):
    """
    Wrapper function that performs validation and instructions.
    Returns the result of the decorated function.
    """
    if not isinstance(num, int):
      raise TypeError("Input must be an integer.")
    if num <= 0:
      raise ValueError("Input must be a positive integer.")

    print("To find the factors of", num, ", you can:")
    print("Write a program to iteratively check for divisibility.")

    return func(num)

  return wrapper

@validate_and_instruct
def find_factors(num):
  factors = []
  for i in range(1, num + 1):
    if num % i == 0:
      factors.append(i)
  return factors

# Example usage
num = int(input("Enter a number: "))
result = find_factors(num)
print("Factors of 12:", result)
