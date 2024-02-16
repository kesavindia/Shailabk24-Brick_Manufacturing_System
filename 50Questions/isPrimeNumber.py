def isprime():
    user_input = int(input("Enter a number:"))
    if user_input<2:
        return False
    for i in range(2,int(user_input**0.5)+1):
        if user_input%i == 0:
            return  False
    return True
print(isprime())