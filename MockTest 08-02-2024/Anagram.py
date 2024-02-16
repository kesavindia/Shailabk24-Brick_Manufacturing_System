'''write a program to check if the given strings are anagram or not'''

def is_anagram(str1, str2):# 2 strings input
    """Checks if two strings are anagrams of each other.
    Returns True if the strings are anagrams, False otherwise.
    """

    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    char_counts = {}
    for char in str1:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for char in str2:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1

    return True

# Test cases
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = is_anagram(str1,str2)
print(result)
