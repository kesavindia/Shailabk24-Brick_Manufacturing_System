#sopy a list of tuple based on a specific index
#
# tuple = (1,2,3,4,5,6,8,7)
# sopyed_tuple=()
# max=-100000
# for i in range(0,len(tuple)):
#     if tuple[i] > max:
#         max = tuple[i]
#     sopyed_tuple += max,
# print(sopyed_tuple)

#rotate a list by to the right by k steps. solve in py

 def rotate_list(nums,k):
     n = len(nums)
#     k %= n #(To handle when k>n)
#     # for i in range(k):
#         # last_element = nums.pop()
#         # nums.insert(0,last_element)
#     nums[:]=nums[-k:]+nums[:-k]
#     return nums
# answer = rotate_list([1,2,3,4,5],2)
# print(answer)
for i, char in enumerate("kesavan"):
    print(char,i)