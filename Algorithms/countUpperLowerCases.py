# accepts a string and calculate the number of upper case letters and lower case letters
def caseCount(string):
    uppercount = 0
    lowercount = 0
    digitcount = 0
    otherLiterals = 0
    for char in string:
        if char.isupper():
            uppercount += 1
        elif char.islower():
            lowercount += 1
        elif char.isdigit():
            digitcount += 1
        else:
            otherLiterals += 1

    return uppercount,lowercount,digitcount,otherLiterals
string = input("enter a string: ")
uppercount, lowercount,digitcount,othercount  = caseCount(string)
print(f"the upper count is {uppercount}")
print(f"the lower count is {lowercount}")
print(f"the digit count is {digitcount}")
print(f"the other count is {othercount}")

