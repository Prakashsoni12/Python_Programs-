'''Write a program that takes two matrices as input and returns their product.
'''

def matrix_multiplication(mat1, mat2):
    # Get the dimensions of the matrices
    rows_mat1, cols_mat1 = len(mat1), len(mat1[0])
    rows_mat2, cols_mat2 = len(mat2), len(mat2[0])
    # Check if the matrices can be multiplied
    if cols_mat1 != rows_mat2:
        raise ValueError("The number of columns of the first matrix must be equal to the number of rows of the second matrix.")
    # Create a new matrix to store the result
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]
    # Perform matrix multiplication
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

mat1 = [[1,2,3],[4,5,6]]
mat2 = [[7,8],[9,10],[11,12]]
result_matrix = matrix_multiplication(mat1, mat2)
print("The result matrix is: ",result_matrix)
