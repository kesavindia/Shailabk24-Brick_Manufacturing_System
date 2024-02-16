# check whether a number is in a given range

def check_if_in_range(num,stapy,end):
    # return stapy <= num <= end
    if stapy <= num <= end:
        return True
    return False
# number = int(input("Enter a number: "))
# stapy = int(input("Enter a number: "))
# end = int(input("Enter a number: "))
if check_if_in_range(number:=20,stapy:=21,end:=30):
    print("Given number is in a range.")
else: print("Given number is not in a range.")