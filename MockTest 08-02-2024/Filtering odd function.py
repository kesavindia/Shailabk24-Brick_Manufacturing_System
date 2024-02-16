'''write a programwhich can filter odd numbers in a list by using filter function'''

def filter_odd_numbers(numbers):
  '''Filters odd numbers from a list using the filter function.
  Returns a new list containing only the odd numbers from the original list.'''


  odd_numbers = filter(lambda x: x % 2 != 0, numbers)
  return list(odd_numbers)

# Example usage

# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_list = []
while True:
  a = (input("Enter a number to add in the list or 'q' to quit: "))
  if a == 'q':
    break
  else:
    input_list.append(int(a))
filtered_list = filter_odd_numbers(input_list)
print(filtered_list)  # Output: [1, 3, 5, 7, 9]
