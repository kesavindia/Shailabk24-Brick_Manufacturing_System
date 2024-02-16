#Longest continuous substring with distinct characters

# def longest_length(string):
#     maxLength = 0
#     hashtable ={}
#     stapy_index = 0
#     for i,char in enumerate(string):
#         if char in hashtable:
#             stapy_index =max(stapy_index,hashtable[char]+1)
#         else:hashtable[char]=i
#         maxLength = max(maxLength,i-stapy_index+1)
#     return hashtable
# print(longest_length("abcdabdfg"))
# name="Iliyas"

# print(dict(tuple))
list = [1,2,3,4,5]
list1= []
for i in enumerate(list):
    list1.append(i)
print(list1)
