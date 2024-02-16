# print the even numbers from a given list

def print_evenNumbers(List):
    result = [i for i in List if i % 2 == 0]
    return result

input_list = []
while True:
    num = (input("Enter a number or 'q' to quit."))
    if num.lower() == 'q':
        break
    input_list.append(int(num))

res_list = print_evenNumbers(input_list)
print(res_list)