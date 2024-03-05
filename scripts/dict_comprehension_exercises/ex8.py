words = ['Saul', 'Goodman']

def count_letters(word):
    return {letter:word.count(letter) for letter in word}

word_letter_count = {word:count_letters(word) for word in words}
print(word_letter_count)


word_letter_count_2 = {word:{letter:word.count(letter) for letter in word} for word in words}
print(word_letter_count_2)