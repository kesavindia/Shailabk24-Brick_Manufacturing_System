# How to findout if the given two strings are anagrams or not?
def isAnagram(str1,str2):
    if len(str1) != len(str2):
        return "Not an anagram."
    str1char = {}
    str2char = {}
    for char in str1:
        str1char[char] = str1char.get(char,0)+1
    for char in str2:
        str2char[char] = str2char.get(char,0)+1
    for char,freq in str1char.items():
        if str2char[char] != freq:
            return False
        return True
str1 = input("enter a string: ")
str2 = input("enter another string: ")
result = isAnagram(str1,str2)
print(result)


