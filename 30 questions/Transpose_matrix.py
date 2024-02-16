# Write a program to transpose a given matrix using a while loop
def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    #Initialising the result matrix with zero value for all its elements.
    transposed_matrix = [[0]*cols for _ in range(rows)]
    i =0
    while i<rows:
        j = 0
        while j < cols:
            transposed_matrix[i][j] = matrix[j][i]
            j += 1
        i += 1
    return transposed_matrix
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        col = int(input(f"Enter element at position ({i+1},{j+1}): "))
        row.append(col)
    matrix.append(row)
result = transpose_matrix(matrix)
print("original matrix:")
for i in matrix :
    print(i)
print("Transposed Matrix: ")
for row in result:
    print(row)

