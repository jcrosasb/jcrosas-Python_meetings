import pandas as pd


# data = {'Student': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Math': [85, 92, 90, 88],
#         'Science': [90, 85, 95, 87],
#         'History': [88, 78, 82, 90] }

# df_student_grades = pd.DataFrame(data)

# #print(df_student_grades[['Student', 'Science']])

# #df_student_grades['Average'] = (df_student_grades['Math'] + df_student_grades['Science'] + df_student_grades['History'])/3

# # row corresponds to axis=1. Column corresponds to axis = 0
# df_student_grades['Average'] = df_student_grades.apply(lambda row: row[['Math','Science','History']].mean(), axis=1)

# df_student_grades['Max'] = df_student_grades.apply(lambda row: row[['Math', 'Science', 'History']].max(), axis=1)

# print(df_student_grades)

# numbers = [1,2,3,4,5]
# sum_list = lambda x: x+5
# print(list(map(sum_list, numbers)))

def average(x: int, y: int, z: int, m: int) -> float:
    return (x+y+z+m)/3


def average_2(*args: int) -> float:
    return sum(args)/len(args)


def average_3(numbers: list[int]) -> float:
    return sum(numbers)/len(numbers)


# print(average(1,2,3,4))

# print(average_2(1,2,3))

# print(average_3([1,2,3,4]))

# Packing
# def test_function(*args):
#     print(args)
#     print(type(args))


# test_function(1,2,3,4,5)


# def test_function_2(x:int, y:int, z:int, s:str):
#     print(f'x={x}')
#     print(f'z={z}')
#     print(f'y={y}')
#     print(f's={s}')


# #test_function_2(2,4,6,'hello')

# test_tuple = (12,14,16,'hi')
# test_list = {1:12,2:14,3:16,4:'hi'}

# Unpacking
##test_function_2(*test_list)

# def printing_kwargs(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)

# # printing_kwargs(name='salvador',year=2024)

# # printing_kwargs(book='harry potter', character='harry')

# def test_kwargs(x:int, y:int, z:int, s:str):
#     print(f'x={x}')
#     print(f'z={z}')
#     print(f'y={y}')
#     print(f's={s}')

# dictionary = {'x':13, 'y':-2 ,'z':22 ,'s':'goodbye'}

# #test_kwargs(**dictionary)


# def custom_csv_reader(filepath: str, **aakwargs):
#     for key, value in aakwargs.items():
#         print(key, value)
#     data = pd.read_csv(filepath, **aakwargs)
#     return data

# file_path = 'data.csv'
# names = ['new_name', 'new_last_name', 'new_email', 'new_age', 'new_position', 'new_login_time']
# parse_dates = ['new_login_time']

# #print(custom_csv_reader(names=names,parse_dates=parse_dates, filepath=file_path))

# parsing_dict = {'names':['another_name', 'another_last_name', 'another_email', 'another_age', 'another_position', 'another_login_time'], 
#                 'parse_dates': ['another_login_time']}

# parsing_dict_2 = {'names': ['date'],
#                   'usecols': [5]}

# parsing_dict_3 = {'names': ['dev_name','dev_last_name','dev_email'],
#                   'usecols': [0,1,2]}

# df = pd.read_csv('data.csv', **parsing_dict_3, skiprows=1)
#print(df)

# A first-order function is a function that applies to built-in data structures of python

# Higher-order functions: take functions as arguments. Functions of functions

def square(x: int) -> int:
    return x**2

def is_even(x: int) -> bool:
    return x % 2 == 0

numbers = [1,2,3,4,5]#list(range(1000))

numbers_squared = [square(number) for number in numbers if is_even(number)]

#print(numbers_squared)

square_iterator = list(map(lambda x: x**2, (filter(lambda x: x % 2 == 0, numbers))))
# print(numbers_squared.__sizeof__())
# print(square_iterator.__sizeof__())
print(square_iterator)


print(any([True, False, True]))

print(all([True, True, True]))

matrix = [[1,3],
          [-3,0],
          [17,5.9]]

cols = len(matrix[0])

check_1 = all(len(row) == cols for row in matrix)

check_2 = all(isinstance(element, int) for row in matrix for element in row)
print(check_2)

def validate_matrix(matrix):
    check_1 = all(len(row) == cols for row in matrix)
    check_2 = all(isinstance(element, int) for row in matrix for element in row)
    if check_1 and check_2:
        print('matrix valid')
    else:
        print('matrix invalid')

validate_matrix(matrix=matrix)
#print(isinstance(matrix[0][0], int))

for method in cols.__dir__():
    print(method)

# CHECK:
#   1. Decorators
#   2. Closures
#   3. Error handling