# Implement a program using nested for loops to print a diamond pattern

def print_diamond(height):
    # Loop for each row
    i = 1
    while i <= height:
        # Print leading spaces
        space = 1
        while space <= height - i:
            print(" ", end="")
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

    # Loop for the bottom half of the diamond
    i = height - 1
    while i >= 1:
        # Print leading spaces
        space = 1
        while space <= height - i:
            print(" ", end="")
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
        i -= 1

# Get user input for the height of the diamond
height = int(input("Enter the height of the diamond: "))

# Call the function to print the diamond pattern
print_diamond(height)

