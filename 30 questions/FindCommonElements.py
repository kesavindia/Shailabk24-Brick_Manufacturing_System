# Find the common elements in two lists using a for loop
input1 = input("enter elements of list1(space separated): ")
list1 = [int(i) for i in input1.split()]
input2 = input("enter elements of list2(space separated): ")
list2 = [int(i) for i in input2.split()]
commonList = []
for i in list1:
    if i in list2:
        commonList.append(i)
print(list1)
print(list2)

print(commonList)
