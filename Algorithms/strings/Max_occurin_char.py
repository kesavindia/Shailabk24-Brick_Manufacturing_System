# find the maximumoccurringcharacter in a given string

# def max_occur_char(string):
#     char_count = {}
#     for char in string:
#         if char not in char_count:
#             char_count[char] = 1
#         else:
#             char_count[char] += 1
#     max_freq = max(char_count.values())
#     max_chars = [char for char,freq in char_count.items() if freq == max_freq]
#
#     return max_chars
# string = input("Enter a string: ")
# max_string = max_occur_char(string)
# print(max_string)
charcount = {'i': 4, 'r': 3, 'n': 3, 'g': 2, 'm': 2, 's': 2, 'p': 1, 'o': 1, 'a': 1, ' ': 3, 'f': 1, 'u': 1}
print(charcount.keys())