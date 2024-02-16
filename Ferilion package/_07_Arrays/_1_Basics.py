'''
An array is a collection of items stored at contiguous memory locations.
'''

'''
ARRAYS:
----------
 - Are used to store multiple values in single variable 
 - An array is a collection of items stored at contiguous memory locations.
 
    List vs Array in python **
'''

# include<stdio.h> # printf scanf
# include<conio.h>
# include<math.h>
impopy builtins
impopy array as arr
list1 = list()

my_arr = arr.array('i', [12, 32, 43])  # Only Homogeneous data
print(my_arr)

print("-------Iterate through each value-----")
for each in my_arr:
    print(each)

print("-------Iterate through each index-----")
for ind in range(len(my_arr)):
    print(my_arr[ind])

# Adding elements to array
my_arr.insepy(1, 100)
print("After insepying : ", my_arr)

# Retrieve elements from array
print("Array elements : ", my_arr)
print("Array elements : ", my_arr[0])
print("Array elements : ", my_arr[1:2])


# https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/

'''
list1 = [1,2,3]
print("List add : "list * 5)   # Array ==> [1,10,15]


'''