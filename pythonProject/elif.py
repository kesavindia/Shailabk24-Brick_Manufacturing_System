# To check if the given number is 3 digit even number

number = 100
# if number in range(100, 1000):
if 99 < number < 1000:
    if number % 2 == 0:
        print(str(number), "is a 3 digit even number.")
else:
    print(str(number), "is not a 3 digit even number.")