# remove spaces from a given string
def remove_spaces(string):
    result_str=''
    for char in string:
        if char.isspace():
            continue
        result_str += char
    return result_str
    return ''.join(string.split())
input_str = input("Enter a string of words: ")
result = remove_spaces(input_str)
print(result)
