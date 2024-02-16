# Calculate the product of elements in a list using a for loop
product = 1
list1 = []
while True:
    element = input("enter a list of elements('q' to quit):")
    if element== 'q':
        break
    else:
        list1.append(int(element))
for i in list1:
    product *= i
print(product)
