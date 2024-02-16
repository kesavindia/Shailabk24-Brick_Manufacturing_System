# def areAnagrams(str1,str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()
#     return sorted(str1) == sorted(str2)
# str1 = input("Enter a string: ")
# str2 = input("Enter another string: ")
# if areAnagrams(str1,str2):
#     print(f"Given strings {str1} and {str2} are anagrams.")
# else:
#     print(f"Given strings {str1} and {str2} are not anagrams.")

queue ='BGBGBGGB'

queueList = list(queue)
right_ptr = len(queue)-1

for left_ptr in range(len(queue)-1,-1,-1):
    if queueList[left_ptr] == 'G':
        queueList[left_ptr],queueList[right_ptr] = queueList[right_ptr],queueList [left_ptr]
        right_ptr -= 1
str = ''.join(queueList)
print(str)

for i in range(10):
    print(i,end=" ")