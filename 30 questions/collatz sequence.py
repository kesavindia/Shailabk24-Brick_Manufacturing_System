'''Implement a program using a while loop to generate and print the Collatz sequence for
given starting number.'''
def collatz_sequence(starting_number):
    while starting_number != 1:
        print(starting_number, end=" ")
        if starting_number % 2 == 0:
            starting_number //= 2
        else:
            starting_number = 3 * starting_number + 1

    print(1)  # Include the final 1 in the sequence

# Get user input for the starting number
start_number = int(input("Enter the starting number for the Collatz sequence: "))

# Generate and print the Collatz sequence
print(f"Collatz sequence for {start_number}:")
collatz_sequence(start_number)
