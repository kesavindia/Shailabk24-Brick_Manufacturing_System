list = []
while True:
    a = (input("Enter a number or 'q' to quit: "))
    if a == 'q':
        break
    list.append(int(a))

max = list[0]
list1 = []
for ele in list:
    if ele > max:
        max = ele
for i in list:
    if i != max:
        list1.append(i)
sortedlist = sorted(list1,reverse =True)
secondLargest = sortedlist[0]
print("Second largest:",secondLargest)

