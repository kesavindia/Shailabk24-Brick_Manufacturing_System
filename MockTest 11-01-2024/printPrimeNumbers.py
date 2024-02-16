# Write a program using nested for loops to print a triangle of prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_triangle(rows):
    current_number = 2
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end=" ")

        for j in range(i + 1):
            while not is_prime(current_number):
                current_number += 1
            print(current_number, end=" ")
            current_number += 1

        print()

rows = int(input("Enter number of rows: "))
print_prime_triangle(rows)



