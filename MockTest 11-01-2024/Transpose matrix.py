# Write a function to transpose a given matrix (2D list) in-place without using any built-in functions or libraries.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(row + 1, cols):
            # Swaping elements
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

matrix = [
    [1, 2, 3,'3a'],
    [4, 5, 6,'6a'],
    [7, 8, 9,'10a'],
    [10,11,12,13]
]
transpose_matrix(matrix)

for row in matrix:
    print(row)
