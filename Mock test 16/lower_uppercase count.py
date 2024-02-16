# Write a program to check whether a entered character is lowercase (a to z) or uppercase (A to Z).

def number_of_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if 'a'<= char <= 'z':
            lower_count += 1
        elif 'A' <= char <= 'Z':
            upper_count += 1
        else:
            print("entered string is not a valid string.")
    return upper_count,lower_count
Input_string = (input("Enter a string: "))
upper_case_count,lower_case_count = number_of_upper_lower((Input_string))
print("Lower case letters count: ",lower_case_count)
print("Upper case letters count: ",upper_case_count)


