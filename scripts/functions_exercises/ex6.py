from typing import Dict


# def calculator_2(number1: int, number2: int) -> Dict:
#     return dict(zip(['add', 'sub', 'prd', 'div'], [(lambda x, y: x + y)(a,b), 
#                                                    (lambda x, y: x + y)(a,b), 
#                                                    (lambda x, y: x * y)(a,b), 
#                                                    (lambda x, y: x / y)(a,b)]))

# a, b = 18, 3
# print(calculator_2(a, b))


calculator = dict(zip(['add', 'sub', 'prd', 'div'], [lambda x, y: x + y, 
                                                 lambda x, y: x + y,
                                                 lambda x, y: x * y,
                                                 lambda x, y: x / y]))

print(calculator(18,3))

# a, b = 18, 3
# calculator['add'](a, b)


