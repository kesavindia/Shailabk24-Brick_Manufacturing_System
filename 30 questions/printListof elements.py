# Print the elements of a list using a for loop
list1 = []
while True:
    element = input("enter a list of elements('q' to quit):")
    if element=='q':
        break
    else:
        list1.append(element)
for i in list1:
    print(i,end=" ")

