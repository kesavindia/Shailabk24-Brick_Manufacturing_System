'''write a program to generate te fibonacci series upto a specified number of terms.'''
def fibonacci(n):# n is the term number to calculate.

  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
num_terms = int(input("Enter a number terms:"))
for i in range(num_terms):
  fibonacci_number = fibonacci(i)
  print(f"Term {i+1}: {fibonacci_number}")

