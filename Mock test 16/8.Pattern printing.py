#16. Pattern printing
row =5
for i in range(1,row+1):
    for j in range(1,30):
        if j%2 ==1:
            print(j,end = " ")
    print()