#contiguous subarray with maximum sum

# list = [1,2,3,-5,6,3,-6,8,5,-2]
def maxSum(list):
    if not list:
        return None
    max_sum = list[0]
    curr_sum = list[0]
    for i in list[1:]:
        curr_sum = max(i,curr_sum+i)
        max_sum = max(curr_sum,max_sum)
    return max_sum
def get_user_input():
    numbers = []
    while True:
        number = input("Enter a number or 'q' to Quit:")
        if number == 'q':
            break
        else:
            try:
                numbers.append(int(number))
            except Exception:
                print("Enter a valid number")
    return numbers
maxsum = maxSum(get_user_input())

print(maxsum)



