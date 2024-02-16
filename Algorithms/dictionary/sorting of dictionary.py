my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[0]))

print("Ascending Order:", sorted_dict_asc)

my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

sorted_dict_desc = dict(sorted(my_dict.items(),key = lambda item:item[0],reverse=True))

print("Descending Order:", sorted_dict_desc)