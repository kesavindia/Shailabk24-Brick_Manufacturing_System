# Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

n=15
result_dict = {}
#
# for x in range(1,n+1):
#     result_dict[x] = x*x
# print(result_dict)
# result_dict[6] = 36
# print(result_dict.get(3) )
# print(result_dict[3] )
#
# print(result_dict)

for i in range(1,n+1):
    result_dict[i] = i*i
print(result_dict)