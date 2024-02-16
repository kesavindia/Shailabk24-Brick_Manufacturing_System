def movespacestofront(string):
    spaces = [char for char in string if char.isspace()]
    non_spaces = [char for char in string if not char.isspace()]
    result_str = ''.join(spaces+non_spaces)
    return result_str
input_string = input("Enter a string: ")
result = movespacestofront(input_string)
print(result)