rows_A = int(input("Enter number of rows for Matrix A: "))
columns_A = int(input("Enter number of columns for Matrix A: "))

matrix_A = []
for i in range(rows_A):
    row = []
    for j in range(columns_A):
        element = float(input(f"Enter element at position ({i+1},{j+1}) for Matrix A: "))
        row.append(element)
    matrix_A.append(row)

# Input Matrix B
rows_B = int(input("Enter number of rows for Matrix B: "))
columns_B = int(input("Enter number of columns for Matrix B: "))

matrix_B = []
for i in range(rows_B):
    row = []
    for j in range(columns_B):
        element = float(input(f"Enter element at position ({i+1},{j+1}) for Matrix B: "))
        row.append(element)
    matrix_B.append(row)

# Matrix Multiplication
if columns_A != rows_B:
    print("Invalid matrix format, please enter a valid matrix for multiplication.")
else:
    # Initialize Result Matrix
    result_matrix = []
    for i in range(rows_A):
        row = []
        for j in range(columns_B):
            row.append(0)
        result_matrix.append(row)




    # Matrix Multiplication
    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    # Print Result Matrix
    print("Result Matrix:")
    for row in result_matrix:
        print(row)
