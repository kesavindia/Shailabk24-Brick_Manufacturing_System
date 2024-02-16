# multiplication table of the given number

def multiplicationTable(n):
    for i in range(1,11):
        print(f'{n}X{i} = {n*i}')
multiplicationTable(5)