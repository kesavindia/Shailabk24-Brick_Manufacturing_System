'''write the python program to find to count the frequency of each element in a list
str1 = " You must be the change; you wish$ to see in the world."'''

str1 = "You must be the change; you wish$ to see in the world."
str1 = str1.lower()
d = {}# initializing an empty dictionary
for char in str1:
    if char not in d.keys():
        d[char] = 1
    else:
        d[char] += 1
for key, value in d.items():
    print(f"{key}:{value}")
