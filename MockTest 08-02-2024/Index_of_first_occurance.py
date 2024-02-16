''' find the index of the first occurance in a string:
Given two strings needle and haystack, return the index of the first occurance of needle in haystack,
or -1 if the needle is not part of haystack.
example: input: haystack = "sadbutsad", needle="sad"
output=0'''

def str_str(haystack: str, needle: str) -> int:

    if not needle:  # Handle empty needle case
        return 0
    for i in range(len(haystack) - len(needle) + 1):

        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

# Example usage
haystack = input("Enter a string: ")
needle = input("Enter another string: ")
index = str_str(haystack, needle)
print(index)  # Output: 0
