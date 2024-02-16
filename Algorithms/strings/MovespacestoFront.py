# move spaces to the front of a given string
def move_Spaces(inputString):
    newString = ''
    for char in inputString:
        if char ==' ':
            newString += char
    for char in inputString:
        if char !=' ':
            newString += char
    return newString
string = input("Enter a string: ")
result_string = move_Spaces(string)
print(result_string)

