# Exercise 2. Wordy comprehension. List comprehensions in Python are datatype agnostic and apply to the items in a list. 
# A list comprehension over strings applies methods for strings. Write a solution to the following questions using list comprehension.

# Get the word length of a given list of words
words = ['day', 'night', 'white', 'black', 'positive', 'negative']
words_length = [len(word) for word in words]

# Get each of the words in a list capitalized
capitalized_words = [word.capitalize() for word in words]

# Remove the vowels of each of the words in a list of words
def remove_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join([char for char in string if char not in vowels])

words_no_vowels = [remove_vowels(word) for word in words]


print(f'The list of words is: {words}\n')
print(f'The length of the words is: {words_length}\n')
print(f'The capitalized words are: {capitalized_words}\n')
print(f'The words without vowels are: {words_no_vowels}')

   