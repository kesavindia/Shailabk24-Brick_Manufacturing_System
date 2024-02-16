# Find the largest number in a list using a for loop


# list1 = []
# while True:
#     element = input("enter a number(q to quit): ")
#     if element == 'q':
#         break
#     list1.append(int(element))
element = input("enter a list of numbers(space separated): ")
list1 = [element1 for element1 in element.split()]

max = list1[0]
for ele in list1:
    if ele > max:
        max = ele
print(list1)
print(max)

