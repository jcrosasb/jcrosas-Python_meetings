matrix_A = [[1, 2], 
            [3, 4]]

matrix_B = [[5, 6], 
            [7, 8]]


def matrix_mult(matrix1, matrix2):
    rows = len(matrix1)
    cols = rows
    result = []
    for r in range(rows):
        result_row = []
        for c in range(cols):
            counter = 0   
            for i in range(rows):
                counter += matrix1[r][i] * matrix2[i][c]
            result_row.append(counter)
        result.append(result_row)      
    return result


def matrix_mult_lc(matrix1, matrix2):
    rows = len(matrix1)  # Number of columns
    cols = rows  # Number of rows (= to rows because it is a square matrix mult)

    return [[sum([matrix1[r][i]*matrix2[i][c] for i in range(rows)]) 
                                              for c in range(cols)] 
                                              for r in range(rows)]

def matrix_multiply(A, B):
    # Initialize an empty result matrix with the appropriate dimensions
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def matrix_mult_zip(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) 
                        for B_col in zip(*B)]
                                for A_row in A]


print(matrix_mult(matrix_A, matrix_B))

print(matrix_mult(matrix_A, matrix_B))

print(matrix_multiply(matrix_A, matrix_B))

print(matrix_mult_zip(matrix_A, matrix_B))

# NOTES:
# Salvador:
#   1. Try it with the zip() function


