# remove duplicate characters of a given string
def remove_duplicate_char(string):
    set1 = set()
    for char in string:
        if char.isspace():
            continue
        set1.add(char)
    return set1
str = input("enter a string: ")
without_duplicate = remove_duplicate_char(str)
result_string=""
for char in without_duplicate:
    result_string += (char)
print(result_string)
