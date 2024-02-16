list = [12,"kumar",0.43,True,87,None,'s']
dictionary = {}

for item in list:
    dictionary[item] = type(item)
print(dictionary)