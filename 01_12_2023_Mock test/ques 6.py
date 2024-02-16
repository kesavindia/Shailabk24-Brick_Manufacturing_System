#convepy list of tuples into single list

list_of_tuples = [(1,2,3),(4,5,6),(7,8,9)]
single_list = []
for i in list_of_tuples:
    for j in i:
        single_list.append(j)
print(single_list)