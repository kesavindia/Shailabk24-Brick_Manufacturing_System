
# # REQ: Check if given number is prime or not # if elif else
# Entity: number
# state of number : datatype -int
# behaviour : prime_num(), generate_prime()
# def prime_number(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     else:
#         i = 2
#         while i*i <= n:
#             if n%i == 0:
#                 return False
#             else:
#                 return True
# if __name__ == "__main__":
#     # State
#     n = int(input("enter an integer number: "))
#     if prime_number(n):
#         print("Given number {} is a prime number.".format(n))
#     else:
#         print("Given number is not a prime number.")
# REQ: Check whether given number is Positive or Negative or Zero # if elif else
# State(Data/DataType)
# num1 = float(input("Enter a number: "))
# #Behaviour
# if num1 > 0:
#     print("Positive number")
# elif num1 == 0:
#     print("Zero")
# else:
#     print("Negative number")
# #------------------------------------------
# # REQ: Check whether given number is even or odd # if elif else
# # State
# num2 = int(input("Enter number : "))
# print("Given number is : ", num2)
# # Behavior
# if num2 % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")
# #---------------------------------------------
# # REQ: Check whether given number is greater than 20 # if elif else
# # State
# num3 = int(input("Enter number : "))
# # Behavior
# if num3 > 20:
#     print("Number is greater")
# else:
#     print("not found")
# #----------------------------------------------
#
# # REQ: Check if given number is lesser than 50 # if elif else
# # State
# num4 = int(input("Enter number : "))
# #Behaviour
# if num4 < 50:
#     print("Number is lesser")
# else:
#     print("not found")
#--------------------------------------------------------

# # REQ : Check if given number is palindrome or not
# # State
# num6 = int(input("Enter a number : "))
# # Behaviour
# temp=num6
# rev=0
# while(num6 > 0):
#     dig = num6 % 10
#     rev = rev * 10 + dig
#     num6 = num6 // 10
# if(temp == rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")
# #---------------------------------------------
#
# # REQ: Check if given string is palindrome
# # State
# str = str(input("Enter a word : "))
# # Behaviour
# if(str == str[::-1]):
#     print("The letter is a palindrome")
# else:
#     print("The letter is not a palindrome")
# #--------------------------------------------------
#
# # REQ: Check if the person is over 18 or not #if elif else
# age = int(input("Enter the age : "))
# # Behaviour
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are not an adult")
# #--------------------------------------------------
# write a fn. to list the first N prime numbers.
Entity: number
state of number : datatype -int
behaviour : prime_num(), generate_prime()
def prime_num(n):
    if n<2:
        return False
    elif n<4:
        return True
    else:
        i=2
        while i <= n**.5:
            if n%i == 0:
                return False
            i += 1
        return True
def generate_prime(n):
    primes = []
    i =2
    while len(primes) < n:
        if prime_num(i):
            primes.append(i)
        i += 1
    return primes
n = int(input("Entera number: "))
prime_num_list = generate_prime(n)
print(f"the first {n} primes numbers are {prime_num_list}")

