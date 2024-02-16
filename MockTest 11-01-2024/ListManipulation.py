
'''Nested List Manipulation:
	Given a nested list of integers, write a program to find the sum of all elements in the list. The list may contain sub lists, and the program should handle arbitrary levels of nesting.
	input: nested_list = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10, 11]]]
	output: sum_of_elements = 76'''
def sum_nested_list(nested_list):
  sum_of_elements = 0
  for element in nested_list:
      if isinstance(element,list):
          sum_of_elements += sum_nested_list(element)
      else:
          sum_of_elements += element
  return sum_of_elements

nested_list = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10, 11]]]
sum_of_elements = sum_nested_list(nested_list)
print(f"The sum of all elements in the list: {sum_of_elements}")
