
letters_numbers_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

numbers_letters_dict = {value:key for value, key in letters_numbers_dict.items()}

print(numbers_letters_dict)