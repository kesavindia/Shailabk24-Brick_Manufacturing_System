# Create a program using for loops to print a square matrix in spiral order
def print_spiral_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    while top <= bottom and left <= right:
        # Printing top row
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")

        top += 1

        # Printing right column
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")

        right -= 1

        # Printing bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")

            bottom -= 1

        # Printing left column
        for i in range(bottom,top-1,-1):
            print(matrix[i][left],end = " ")
        left += 1


matrix = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

print_spiral_matrix(matrix)
