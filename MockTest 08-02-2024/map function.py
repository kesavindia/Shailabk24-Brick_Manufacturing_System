'''write a program which can map() to make a list whose elements are cube of elements in a given list'''

def cube_elements(numbers):
  """
  Cubes the elements in a list using map().
  Returns a new list containing the cubes of the elements in the original list.
  """

  cubed_numbers = map(lambda x: x * x * x, numbers)
  return list(cubed_numbers)

# Example usage
# input_list = [1, 2, 3, 4, 5]
input_list = []
while True:
  a = (input("Enter a number to add in the list or 'q' to quit: "))
  if a == 'q':
    break
  else:
    input_list.append(int(a))
cubed_list = cube_elements(input_list)
print(cubed_list)
