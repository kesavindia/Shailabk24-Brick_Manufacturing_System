# Find the highest 3 values in a dictionary.
dict1 = {'d': 3, 'c': 4, 'b': 2, 'a': 1}
list1 = sorted(dict1.values(),reverse=True)
print(list1)
if len(list1)>=3:
    highest_3_values = list1[:3]
    print(highest_3_values)
else:
    print("There is no enough values.")