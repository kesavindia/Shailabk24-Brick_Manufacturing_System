# Find the number of occurrences of a character in a String
def no_of_occurances(string,target_char):
    count=0
    for char in string:
        if target_char == char:
            count += 1
    return count
input_string  = input()
target = input()
count = no_of_occurances(input_string,target)
print(count)