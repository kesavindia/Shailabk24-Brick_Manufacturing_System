# Write a program in to convert a decimal number into binary
def decimaltobinary(number):
    if not number:
        return 'A'
    binaryString =""
    while number > 0:
        remainder = number % 2
        binaryString = str(remainder) + binaryString
        number //= 2
    return binaryString
decimal = int(input("Enter a number: "))
binary = decimaltobinary(decimal)
print(binary)




