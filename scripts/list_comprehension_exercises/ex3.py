# Exercise 3. Matrix Transpose. A matrix in Python can be represented as a list of lists, i.e., a 2D list. 
# The transpose of a matrix refers to swapping elements in position (i,j) to position (i,j). 
# Use list comprehension to transpose the matrix.

def transpose(matrix):
    rows, columns = len(matrix), len(matrix[0])
    return [[matrix[row][column] for row in range(rows)] for column in range(columns)]


if __name__ == "__main__":
    m = [[1, 2, 3, 4], 
         [5, 6, 7, 8], 
         [9, 10, 11, 12], 
         [13, 14, 15, 16]]
    
    mat = '\n'.join([str(row) for row in m])
    print(f'The matrix is:\n{mat}')

    transpose_matrix = '\n'.join([str(row) for row in transpose(matrix=m)])
    print(f'\nThe transposed matrix is:\n{transpose_matrix}')