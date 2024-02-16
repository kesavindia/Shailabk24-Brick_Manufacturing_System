# How do you remove all occurrences of a given character from the input string
def removechars(str1,target):
    str = ""
    for char in str1:
        if target != char:
            str += char
    return str
stringInput = input("Enter a string: ")
TargetChar = input("Enter target char to remove: ")

resultStr = removechars(stringInput,TargetChar)
print(resultStr)