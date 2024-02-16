#right angle triangle

# for i in range(2,7):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
#
# row=5
# for i in range(row,0,-1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
# row =5
# # for i in range(1,row+1):
# #     space = " "*(row-i)
# #     print(space+((str(i)+" ")*i)+space)
#
# for i in range(row,0,-1):
#     space = " "*(row-i)
#     print(space+("*"+" ")*i+space)
#
# for i in range(1,row+1):
#     space = " "*(row-i)
#     print(space+(str(i)+" ")*i+space)


row =7

for i in range(row,0,-1):
    space = " "*(row-i)
    print(space+(str(i)+" ")*i+space)
for i in range(0,row+1):
    for j in range(0,i):
        print(i,end = " ")
    print()
for i in range(row,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()



thislist = tuple(["apple", "banana", "cherry"])
print(thislist)



















