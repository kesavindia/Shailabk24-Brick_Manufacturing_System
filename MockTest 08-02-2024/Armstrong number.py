'''write a program to check if the given number is Armstrong or not '''

def Armstrong_number(num):

    num_str = str(num)
    len_str = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**len_str
    return sum == num

#Test cases

num = int(input("Enter a number to check if it is an armstrong number: "))
result = Armstrong_number(num)
print(result)
