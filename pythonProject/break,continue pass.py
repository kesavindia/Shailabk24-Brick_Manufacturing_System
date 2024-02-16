# def find_multipes():
#     n = int(input("Enter a number: "))
#     answer = 1
#     for i in range(1,n):
#         if 20*i >= n:
#             answer *= 20*i
#             break
#     return answer
# print(find_multipes())

# use continue

# def put_in_list():
#     list1 = ""
#     list2="1,2,3,4,5"
#     for i in list2:
#         if i == ",":
#             continue
#         list1 += (i+" ")
#     return list1
# print(put_in_list())
#
# def put_in_list():
#     list1 = ""
#     list2="1,2,3,4,5"
#     for i in list2:
#         if i == ",":
#             pass
#         list1 += (i+" ")
#     return list1
# print(put_in_list())
#
#Move all the negative numbers to the end of the list.

# def move_negative_numbers():
#     list= [3,4,5,-2,-1,2,8,0,-4]
#     list1 =[]
#     for i in list :
#         if i>=0 :
#             list1.append(i)
#     for i in list:
#         if i < 0 :
#             list1.append(i)
#     return list1
# if __name__ == "__main__":
#     print(move_negative_numbers())

def move_negative_numbers(list1):
    left = 0
    right = len(list1)-1
    while left <= right:
        if list1[left] < 0 :
            list1[left],list1[right] = list1[right],list1[left]
            right -= 1
        else:
            left += 1
    return list1
print(move_negative_numbers([1,-3,4,-5,0,6,-9,1]))


