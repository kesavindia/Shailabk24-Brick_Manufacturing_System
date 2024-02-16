'''write a generator function that generates the squares of numbers upto a specified limit'''

def square_generator(limit):

  #Generates the squares of numbers up to a specified limit.

  for num in range(1, limit + 1):
    yield num * num

# Example usage
limit = int(input("Enter a number: "))
for square in square_generator(limit):
  print(square)
