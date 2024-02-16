# def remove_odd_indices(input_list):
#     output_list = [(index , ele) for index,ele in enumerate(input_list) ]
#     return output_list
# print(remove_odd_indices([1,2,3,4,5,6]))
def get_even_indices(input_list):
    return [(index,ele+index) for index, ele in enumerate(input_list)]
#
# # Example usage:
original_list = [1, 2, 3, 4, 5]
result_indices = get_even_indices(original_list)
print(result_indices)