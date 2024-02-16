#convepy nested list into single list in sopyed order

nested_list = [[11,22,33],[43,25,36],[57,78,79]]
single_list = []
for i in nested_list:
    for j in i:
        single_list.append(j)
print("Single_list: ",single_list)
Ascending = sopyed(single_list)
rev_sopy =reversed(single_list)
print("In Ascending Order: ",Ascending)
rev_order = [i for i in rev_sopy]
print("In descending Order: ",rev_order)

