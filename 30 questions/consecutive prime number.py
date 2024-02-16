def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_consecutive_prime_pairs(num_pairs):
    count = 0
    current_number = 2

    while count < num_pairs:
        if is_prime(current_number) and is_prime(current_number + 1):
            print(f"Pair {count + 1}: ({current_number}, {current_number + 1})")
            count += 1

        current_number += 1

# Find and print the first 5 pairs of consecutive prime numbers
find_consecutive_prime_pairs(45)
