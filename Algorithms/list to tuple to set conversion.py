#List to Tuple (without using tuple()):

my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(elem for elem in my_list)
# List to Set (without using set()):

my_list = [1, 2, 3, 4, 5]
my_set = {elem for elem in my_list}

# Tuple to List (without using list()):

my_tuple = (1, 2, 3, 4, 5)
my_list = [elem for elem in my_tuple]

# Tuple to Set (without using set()):

my_tuple = (1, 2, 3, 4, 5)
my_set = {elem for elem in my_tuple}

# Set to List (without using list()):

my_set = {1, 2, 3, 4, 5}
my_list = [elem for elem in my_set]

# Set to Tuple (without using tuple()):
my_set = {1, 2, 3, 4, 5}
my_tuple = tuple(elem for elem in my_set)

These examples use list comprehensions or set comprehensions to manually create a new iterable of the
desired type. Note that these methods are less concise and less efficient than using the built-in functions
provided by python.