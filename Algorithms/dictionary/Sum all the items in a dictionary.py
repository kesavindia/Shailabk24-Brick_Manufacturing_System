dict1 = {'b': 3, 'c': 4, 'a': 1}
sum1 = 0
for x in dict1.values():
    sum1 += x
sum2 = sum(dict1.values())
print(sum1)
print(sum2)

#multiplication of values in dict
my_dict = {'a': 2, 'b': 3, 'c': 4}

product = 1

for value in my_dict.values():
    product *= value

print("Product of all items:", product)
