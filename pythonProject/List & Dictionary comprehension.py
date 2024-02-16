#List comprehension
# List = [expression for item in iterable if condition]
# List = [expression if-else condition for item in iterable]

#Print square of n natural numbers in a list

# list1 = [i*i if i<5 else i for i in range(1,10+1) ]
# print(list1)
# list = [23,45,67,65,78]
# list2 = [round(i*.9)  for i in list if i<50]
# print(list2)

'''Dictionary comprehension
dictionary = {key:expression for (key,val) in iterable}
dictionary = {key:expression for (key,val) in iterable if condn}
dictionary = {key:expression if-else for (key,val) in iterable}
dictionary = {key:function for (key,val) in iterable}'''
# dictionary = {"Ram":500,"Ram1":800,"Ram2":700,"Ram3":500,"Ram4":600}
# dict1 = {key.upper():round(val*.9) for (key,val) in dictionary.items() if val>500}
# dict2 = {key:val<800 for key,val in dictionary.items()} # evaluates true or false
# print(dict2)
# dict3 = {key:val if val<800 else val*2 for key,val in dictionary.items()}
# print(dict3)
# def discount(key,val):
#     if key == "Ram" or key == "Ram1":
#         val *= .2565
#     return val
# dict4 = {key:"{:.2f}".format(discount(key,val)) for key,val in dictionary.items()}
# print(dict4)
'''Zip function zips 2 or more iterables into one iterable.'''
name = ("Ram","Shyam","Shiva","Muruga","Angalaparameswari")
place = ("w1","w2","w3","w4","w5")
bakthas = (23,45,67,89,90)
zipped = list(zip(name,bakthas))  #list of tuples
print((zipped))
zipped1 = tuple(zip(name,bakthas))  #tuples of tuples
print((zipped1))
zipped2 = dict(zip(name,bakthas)) #Dictionary
print((zipped2))
zipped3 = set(zip(name,bakthas))  #set of tuples
print((zipped3))