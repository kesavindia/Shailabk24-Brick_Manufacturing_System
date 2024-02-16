'''write a python program for handling errors like
zerodivision error,value error,index error,type error with syntax'''

def divide_numbers(x, y):
  try:
    result = x / y
    return result
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  except ValueError:
    print("Error: Invalid input values. Please enter numbers only.")
  except TypeError:
    print("Error: Unsupported operand types. Please use numbers only.")

def access_list_element(my_list, index):
  try:
    element = my_list[index]
    print("Element at index", index, "is:", element)
  except IndexError:
    print("Error: Index out of range.")

# Example usage
try:
  result = divide_numbers(10, 2)
  print("Division result:", result)
  access_list_element([1, 2, 3], 5)
except Exception as e:  # Catch any other unexpected errors
  print("An unexpected error occurred:", e)
