# def firstrepeatedchar(string):
#     seen_chars = set()
#     for char in string:
#         if char in seen_chars:
#             return char
#         seen_chars.add(char)
#     return None
# input_string = input("Enter a string: ")
# repeated_char = firstrepeatedchar((input_string))
# print("Repeated char:",repeated_char)

# def find_first_repeated_character(input_string):
#     char_index = {}
#     for  index, char in enumerate(input_string):
#         if char in char_index:
#             return char, char_index[char]
#         char_index[char] = index
#     return None
# # Example usage:
# input_str = "wbacabad"
# result = find_first_repeated_character(input_str)
#
# if result:
#     char, index = result
#     print(f"First repeated character: '{char}' at index {index}")
# else:
#     print("No repeated characters.")


def find_first_repeated_character(input_string):
 char_index = {}

 for index, char in enumerate(input_string):
   if char in char_index:
     return f"First repeated character: '{char}' at index {char_index[char]},"
   char_index[char] = index

 return "No repeated characters."

# Example usage:
input_str = "wbacabad"
result = find_first_repeated_character(input_str)

print(result)


