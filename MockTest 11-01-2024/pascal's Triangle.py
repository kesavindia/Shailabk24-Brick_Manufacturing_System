from math import factorial

rows = int(input("Enter Rows = "))
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
    i = i + 1
    print()