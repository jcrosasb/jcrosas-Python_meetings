numbers = [1, 2, 3, 4, 5]

def odd_or_even(number: int) -> str:
    return 'even' if number % 2 == 0 else 'odd'
   

numbers_dict = {number:odd_or_even(number) for number in numbers}

numbers_dict_2 = {number:'even' if number % 2 == 0 else 'odd' for number in numbers}


print(numbers_dict)

print(numbers_dict_2)