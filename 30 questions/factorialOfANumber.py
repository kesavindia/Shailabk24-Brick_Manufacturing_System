# 8.	Calculate factorial of a number using a while loop
import math
num=int(input("Enter a number: "))

factorial = 1
i=1
while i <= num:
    factorial *= i
    i += 1
fact = math.factorial(num)
print(factorial)
print(fact)
