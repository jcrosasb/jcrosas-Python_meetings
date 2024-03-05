from typing import List, Dict

def even_odd_dict(numbers: List[int], operation) -> Dict:
    even, odd = lambda_even_odd(numbers)
    return {item[0]:item[1] for item in lambda_even_odd(numbers)}
    

lambda_even_odd = lambda lst: (('even', [num for num in lst if num % 2 == 0]), ('odd', [num for num in lst if num % 2 != 0]))
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(even_odd_dict(numbers=list_numbers, operation=lambda_even_odd))