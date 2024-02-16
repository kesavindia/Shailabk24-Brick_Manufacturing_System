'''Longest palindrome'''
def is_palindrome(num):

    if num < 0:
        return False

    original_num = num
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10

    return original_num == reversed_num

# Test cases
list1 = [121,543,879,987654,9958599,776677,989,5445]
palindromicList = []
for i in list1:
    if is_palindrome(i):
        palindromicList.append(i)

# num = int(input("Enter a number: "))
# print(is_palindrome(num))
print(palindromicList)
max = palindromicList[0]
for ele in palindromicList:
    if ele > max:
        max = ele
print(max)
