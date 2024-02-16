#
# def modify_and_append(file_path):
#     # Initial content
#     initial_content = "In a field, there were cows that would moo."
#
#     # Write the initial content to the file
#     with open(file_path, 'w') as file:
#         file.write(initial_content)
#
#     # Read the content from the file
#     with open(file_path, 'r') as file:
#         content = file.read()
#
#     # Duplicate the string
#     duplicated_content = content
#
#     # Replace 'cows' with 'Ducks' and 'moo' with 'Quack'
#     modified_content = duplicated_content.replace('cows', 'Ducks').replace('moo', 'Quack')
#
#     # Append the modified content to the file
#     with open(file_path, 'a') as file:
#         file.write(modified_content)
#
# # Example usage:
# modify_and_append('example.txt')
x = 'True'
print(type(x))
tuple1 = [1,2,3,'t']
tuple2 = [1,2,3,'t']
print(tuple1+tuple2)
tuple1 = tuple2
print(id(tuple1))
print(id(tuple2))
