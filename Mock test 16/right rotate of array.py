# rotate a list to the right by n steps

def rotate_list(nums,k):
    n = len(nums)
    k %= n #(To handle when k>n)
    for i in range(k):
        last_element = nums.pop()
        nums.insert(0,last_element)
    # nums[:]=nums[-k:]+nums[:-k]
    return nums
nums = []
while True:
    a = (input("Enter a number to add in the list or 'q' to quit: "))
    if a == 'q':
        break
    else: nums.append(int(a))
k = int(input("enter a number for nth position rotation: "))
print(nums)
answer = rotate_list(nums,k)
print(answer)