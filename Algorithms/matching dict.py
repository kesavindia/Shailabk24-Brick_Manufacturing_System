def common_keys(dict1,dict2):
 all_keys = set(dict1.keys())|(set(dict2.keys()))
 all_keys = set(dict1.keys()).union(set(dict2.keys()))
 common_keys = set(dict1.keys())&(set(dict2.keys()))


 print(common_keys)
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'a':2,'e':3,'f':4}
common_keys(dict1,dict2)
