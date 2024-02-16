'''Python function to find the factorial of a number'''
def factorial(n):
  """
  This function calculates the factorial of a non-negative integer n.

  Args:
      n: The non-negative integer for which to calculate the factorial.

  Returns:
      The factorial of n.
  """

  if n < 0:
    raise ValueError("n cannot be negative")

  if n == 0:
    return 1

  return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
