# 9.	Find the first occurrence of a number in a list using a while loop

Numbers = (input("enter a list of numbers(space separated).: "))
list1 =   [int(num) for num in Numbers.split()]
find_number = int(input("enter a number to find: "))
index = 0
found = False
while index <= len(list1)-1:
    if list1[index] == find_number:
        found = True
        break
    index += 1
if found:
    print(f"The searching number {find_number} is in index {index}.")
else:
    print(f"The searching number {find_number} is not found.")