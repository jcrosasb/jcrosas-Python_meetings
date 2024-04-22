from typing import List

def _add(matrix1:List[List[int]], matrix2:List[List[int]]):
    '''Function to add matrices'''
    return [[matrix1[r][c] + matrix2[r][c] for c in range(2)]
                                               for r in range(2)]


def _substract(matrix1:List[List[int]], matrix2:List[List[int]]):
    '''Function substract matrices'''
    return [[matrix1[r][c] - matrix2[r][c] for c in range(2)] 
                                           for r in range(2)]


def _multiply(matrix1:List[List[int]], matrix2:List[List[int]]):
    '''Function multiply matrices'''
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] 
                                                  for row in matrix1]


def matrix_calculator(**kwargs) -> List[List[int]]:
    '''Function to perfomer either addition, subtraction or multiplication of two 2x2 matrices
       Parameters:
            kwargs: keyword arguments 
                * operation (either 'add', 'substract' or 'multiply')
                * matrix_1: list of lists of integers
                * matrix_2: * matrix_1: list of lists of integers
       Returns:
            List of lists of integers with the result of the select opeartion
    '''

    # Select chosen operation
    if kwargs['operation'] == 'multiply':
        return _multiply(kwargs['matrix_1'], kwargs['matrix_2'])
    elif kwargs['operation'] == 'add':
        return _add(kwargs['matrix_1'], kwargs['matrix_2']) 
    elif kwargs['operation'] == 'substract':
        return _substract(kwargs['matrix_1'], kwargs['matrix_2']) 
    else:
        raise ValueError('Invalid Operation')


if __name__ == '__main__':

    matrix_1 = [[1, 2], [3, 4]]

    matrix_2 = [[5, 6], [7, 8]]

    print(matrix_calculator(operation='multiply', matrix_1 = [[1, 2], [3, 4]], matrix_2 = [[5, 6], [7, 8]]))
    print(matrix_calculator(operation='add', matrix_1 = [[1, 2], [3, 4]], matrix_2 = [[5, 6], [7, 8]]))
    print(matrix_calculator(operation='substract', matrix_1 = [[1, 2], [3, 4]], matrix_2 = [[5, 6], [7, 8]]))
    # print(matrix_calculator(operation='substracttttt', matrix_1 = [[1, 2], [3, 4]], matrix_2 = [[5, 6], [7, 8]]))

