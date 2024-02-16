'''Create a program using for loops to generate a 3x3 magic square (a square in which the
sums of the numbers in  each row, column and both main diagonals are the same).'''
def generate_magic_square():
    # Initialize a 3x3 matrix with zeros
    magic_square = [[0] * 3 for _ in range(3)]

    # Set the initial values for the magic square
    magic_square[0][1] = 1

    # Fill the magic square
    row, col = 0, 1
    for num in range(2, 10):
        magic_square[row][col] = num

        # Move diagonally up and right
        row -= 1
        col += 1

        # Check if the new position is valid, adjust if necessary
        if row < 0 and col > 2:
            row += 2
            col -= 1
        elif row < 0:
            row = 2
        elif col > 2:
            col = 0
        elif magic_square[row][col] != 0:
            row += 2
            col -= 1

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        for num in row:
            print(num, end=" ")
        print()

# Generate and print the 3x3 magic square
magic_square = generate_magic_square()
print("3x3 Magic Square:")
print_magic_square(magic_square)
