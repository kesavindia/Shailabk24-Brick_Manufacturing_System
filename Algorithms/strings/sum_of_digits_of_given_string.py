# compute sum of digits of a given string
def sum_of_digits(string):
    sum = 0
    for char in string:
        if char.isdigit():
            sum += int(char)
    return sum
print(sum_of_digits('123 e r4'))
