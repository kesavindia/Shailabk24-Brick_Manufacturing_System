'''
Create file(like:text file) perform CRUD operations inside data of text file using file handling
'''

import os
def create_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except OSError as e:
        raise OSError(f"Error creating file '{filename}': {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except OSError as e:
        raise OSError(f"Error reading file '{filename}': {e}")

def delete_file(filename):
    try:
        os.remove(filename)
    except OSError as e:
        raise OSError(f"Error deleting file '{filename}': {e}")

# Examples:
filename = 'MyData.txt'

# Create the file
create_file(filename, "This is some sample data.\n")

# Read the file
contents = read_file(filename)
print(f"File contents:\n{contents}")

# Delete the file
delete_file(filename)
print(f"File '{filename}' deleted.")
