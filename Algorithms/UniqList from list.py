List =[]
while True:
    num = (input("Enter numbers for list or press 'q' for quit: "))
    if num == 'q':
        break
    List.append(int(num))
List1 = set(List)
print(list(List1))

# def unique_elements(input_list):
#     return [item for item in input_list if input_list.count(item) == 1]
# List =[]
# while True:
#     num = (input("Enter numbers for list or press 'q' for quit: "))
#     if num == 'q':
#         break
#     List.append(int(num))
# res_list = unique_elements(List)
# print(res_list)
