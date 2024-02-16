'''Write a program using while loops to print the first 10 rows of Pascal's Triangle.'''
from math import factorial

rows = int(input("Enter number of Rows = "))
i = 0
while i < rows:
    j = 0
    while j <= rows - i:
        print(end=' ')
        j = j + 1
    k = 0
    while k <= i:
        print(factorial(i) // (factorial(k) * factorial(i - k)), end=' ')
        k = k + 1
    i += 1
    print()