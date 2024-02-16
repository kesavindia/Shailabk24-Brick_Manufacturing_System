# Sort a dictionary by key
dict1 = {'a': 1, 'b': 2,'d': 3, 'c': 4}
dict2 = {'b': 3, 'c': 4}
Asc_sortedDict =  dict(sorted(dict1.items(),reverse=True))
print("Sorted in ascending order",Asc_sortedDict)
Desc_sortedDict = dict(sorted(dict1.items(),key = lambda x:x[0],reverse=True))
print("Sorted in descending order",Desc_sortedDict)
