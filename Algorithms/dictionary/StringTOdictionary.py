# input_string = '{"key1": 1, "key2": 2, "key3": 3}'
#
# import json
#
# # Use json.loads to convert the string to a dictionary
# result_dict = json.loads(input_string)
#
# print("Resulting Dictionary:", result_dict)
#
# inp_str = "abcdABCDEE"
# result_dict1 = {char:ord(char) for char in inp_str}
# print(result_dict1)
# inp = input("Enter a string to convert into a dictionary.: ")
# result_dict2 = {char:index+1 for index,char in enumerate(inp)}
# print(result_dict2)
from collections import defaultdict

inp = input("Enter a string to convert into a dictionary: ")

result_dict2 = defaultdict(list)

for index, char in enumerate(inp,start=3):
    result_dict2[char].append(index)

print("Resulting Dictionary:", result_dict2)