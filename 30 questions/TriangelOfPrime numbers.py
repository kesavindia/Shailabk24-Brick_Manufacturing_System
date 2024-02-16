# 25.	Write a program using nested for loops to print a triangle of prime numbers

def isPrime(num):
    if num<2:
        return False
    for i in range(2,int(num**.5)+1):
        if num%i == 0:
            return False
    return True
def printTriangle(height):
    currentNumber = 2
    for i in range(1,height+1):
        for j in range(i):
            while not isPrime(currentNumber):
                currentNumber += 1
            print(currentNumber, end=" ")
            currentNumber += 1
        print()
h = int(input("Enter the height of triangle: "))
result = printTriangle(h)









