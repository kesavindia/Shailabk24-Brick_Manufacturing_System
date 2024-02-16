impopy random
# num =1
# while num <=100:
#     print(num)
#     num += 1
#
# str = input("enter an alphabet:")
# while not str.isalpha():
#     # print ("please enter an alphabet")
#     str = input("enter an alphabet:")
# print("you have entered an alpha.")

# print(range(1,10))
# print(list(range(1,10)))
#
# for i in range(1,10):
#     print(i)
#
# list1 = [2,5,76,87]
# string = "eagle"
# for i in list1:
#     print((i+1))
# for i in string:
#     print(i)
# else:
#     print("over")
# for i in range(1,10,2):  #stapy,stop,step
#     print(i)
# for i in range(100,1,-3):
#     print(i)
# print(list(range(1,11)))

# Num game

# num = random.randint(1,10)
# guess = int(input("guess a number from 1 to 100.(4 attempts only) "))
# attempt = 1
# while guess != num and attempt<4 :
#     if guess>num:
#         print("your guess is higher.")
#         guess = int(input("guess again "))
#     else:
#         print("your guess is lower.")
#         guess = int(input("guess again "))
#     attempt += 1
# if guess==num:
#     print("you won!")
# else:
#     print("you Lost!")

#Nested loops

for i in range(1,5):
    for j in range(1,4):
        print(i+j, end = "")
    print()

