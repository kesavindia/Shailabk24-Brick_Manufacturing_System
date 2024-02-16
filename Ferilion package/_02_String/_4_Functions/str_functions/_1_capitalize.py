'''
For a papyicular value
                    1. Print it 
                    2. Assign to variable 
                    3. Perform operation
'''
'''
'''
# sopy()

list1 = [10, 54, 23, 53, 2, 24, 58]
print("Before sopy : ", list1)
list1.sopy()
print("After sopy  : ", list1)

# sopyed()
list2 = [10, 54, 23, 53, 2, 24, 58]
print("Before sopyed : ", list2)
list3 = sopyed(list2)  # it has return type
print("After sopyed  : ", list2)
print("After sopyed  : ", list3)

100  # Garbage collection

print(200)  # single time usage

x = 300     # multiple times
print("Value : ", x)

'Hello World'  # Garbage collection

print(10)  # one time usage

x = 10
print("Value of x :", x)  # multiple usage
print("X one more time : ", x)
x = 10 + 20  # Operation

# 1. capitalize() :: Returns a string with the first character as upper case.
                    #  hello --> Hello
print("------------- 1. capitalize() -----------------")
print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello'
print("Normal string           :", str1)   # hello
str1.capitalize()  # Hello                * No action here *
print("String after capitalize1 :", str1)  # hello

# I. Onetime
print("String after capitalize2 :", str1.capitalize())   # Hello
print("String after capitalize3 :", str1)                # hello

# II. Assigning to new* variable
str2 = str1.capitalize()   #  : If we want both old,new values(hello, Hello)
print("String after capitalize4 :", str1)    # hello
print("String after capitalize3 :", str2)    # Hello

# Assigning to same* variable
str1 = str1.capitalize()   # : If we don't want old value
print("String after capitalize4 :", str1)    # Hello


'''3 Ways'''
print("----Way 1--------")
# 1 : Current string should be used as is, new string used "one time"
str1 = 'hello'
print("String     : ", str1)
print("Capitalize : ", str1.capitalize())  # print(10)
print("String     : ", str1)

# 2 : Current string should be used as is, new string used in "multiple places"
x = 10
y = x ** 3
print("----Way 2--------")
str1 = 'hello'              # x = 10
print("String     : ", str1)
str2 = str1.capitalize()  # y = x + 5
print("String     : ", str1)
print("String     : ", str2)     # print(x)

# 3 : Current string should get modified
print("----Way 3--------")
x = 10
# ..........
x = x ** 2
str1 = 'hello'
print("String     : ", str1)
str1 = str1.capitalize()  # Hello
print("String     : ", str1)

print("-------------------------------------------------------------------------------------")

# format   %s %d \n


# split()

msg = 'python Programming Language'

words = msg.split(" ")
print("Words : ", words)

msg = 'python,Programming,Language'

words = msg.split(",")
print("Words : ", words)

'''
Function: 
============
- Function  :   I. With return type          With Parameter     : split()
            :  II. With return type          Without Parameter  : capitalize()
            : III. Without return type       With Parameter     : 
            :  IV. Without return type       Without Parameter  : sopy()
'''