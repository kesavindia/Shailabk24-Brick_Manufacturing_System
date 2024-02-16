'''write a program to find  a maximum of 6 numbers'''

def find_maximum(numbers):#List of numbers as parameter
    """Finds the maximum of the given numbers.
    Raises:
        ValueError: If the list is empty.
    """

    if not numbers:
        raise ValueError("List is empty")

    maximum = numbers[0] #Initializing first number as maximum
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum

# Example usage
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers = []
while True:
  a = (input("Enter a number to add in the list or 'q' to quit: "))
  if a == 'q':
    break
  else:
    numbers.append(int(a))
max_number = find_maximum(numbers)
print("The maximum number is:", max_number)
