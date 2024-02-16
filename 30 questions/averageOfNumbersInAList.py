# Find the average of numbers in a list using a for loop

numbers = input("enter a list of numbers(space separated): ")
list1 = [int(number) for number in numbers.split()]
sum =0
count=0
for i in list1:
    sum += i
    count = count+1
if count>0:
    avg = sum / len(list1)
print(int(avg))