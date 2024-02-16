# Merge two Python dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)
merged_dict = {**dict2,**dict1} # unpacking dictionary elements and joining
print(merged_dict)
