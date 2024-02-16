'''Write a python program to create a dictionary grouping a sequence of key-value pairs into a
dictionary of lists
Original list:
[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow':[1,3],'blue':[2,4],'red':[1]}
'''

def group_key_value_pairs(data):

    grouped_dict = {}
    for key, value in data:
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].append(value)
    return grouped_dict

# Example usage
data = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
grouped_dict = group_key_value_pairs(data)
print(grouped_dict)
