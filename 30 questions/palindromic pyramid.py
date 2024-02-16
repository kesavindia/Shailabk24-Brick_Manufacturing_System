# Implement a program using while loops to print a palindromic pyramid pattern

def print_palindromic_pyramid(height):
    # Initialize variables
    i = 1

    # Loop for each row
    while i <= height:
        # Print leading spaces
        space = 1
        while space <= height - i:
            print("  ", end="")
            space += 1

        # Print increasing numbers
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1

        # Print decreasing numbers in reverse order
        j = i - 1
        while j >= 1:
            print(j, end=" ")
            j -= 1

        # Move to the next line
        print()
        i += 1

# Get user input for the height of the pyramid
height = int(input("Enter the height of the palindromic pyramid: "))

# Call the function to print the palindromic pyramid
print_palindromic_pyramid(height)
