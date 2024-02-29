# Exercise 5. More on matrices. Square matrices are special matrices with the same number of rows and columns. 
# The rotation of a square matrix consists of moving the row column elements within a degree. 
# The degree lies in 90, 180, and 270. Use a list comprehension to rotate square matrices.

def rotate_90(matrix):
    '''Function to rotate a matrix by 90 degrees. Must be a square matrix'''
    rows, columns = len(matrix), len(matrix)
    return [[matrix[row][col] for row in range(rows)] for col in range(columns-1, -1, -1)]

   
def rotate(matrix, degree):
    '''Function to rotate a matrix by 90, 180 or 270 degrees. Must be a square matrix'''
    if degree == 90:
        return rotate_90(matrix)
    elif degree == 180:
        return rotate_90(rotate_90(matrix))
    elif degree == 270:
        return rotate_90(rotate_90(rotate_90(matrix)))
    else:
        raise ValueError('Degrees must be 90, 180 or 270')


if __name__ == "__main__":

    m = [[1, 2, 3, 4], 
         [5, 6, 7, 8], 
         [9, 10, 11, 12], 
         [13, 14, 15, 16]]
    
    mat = '\n'.join([str(row) for row in m])
    print(f'The matrix is:\n{mat}')

    deg = 270
    rotated_matrix = '\n'.join([str(row) for row in rotate(matrix=m, degree=deg)])
    print(f'\nThe matrix rotated by {deg} degrees is:\n{rotated_matrix}')

   