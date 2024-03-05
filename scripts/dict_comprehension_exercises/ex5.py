def count_vowels(word: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


names = ['Saul', 'Goodman', 'Walther', 'White']

vowel_freq = {name:count_vowels(name) for name in names}
    
print(vowel_freq)

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowel_freq_2 = {name:sum(1 for letter in name if letter in vowels) for name in names}

print(vowel_freq_2)