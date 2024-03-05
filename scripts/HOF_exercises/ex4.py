count_vowels = lambda string: (string.upper(), sum(1 for letter in string.upper() if letter in {'A', 'E', 'I', 'O', 'U'}))

words = ["hello", "world", "python"]

result = list(map(count_vowels, words))
print(result)