from typing import List

len_lambda = lambda string: len(string)


def sort_by_length(words: List[int], operation):
    '''Uses bubble sort'''
    size = len(words)
    for i in range(size):
        for j in range(size-i-1):
            if operation(words[j]) > operation(words[j+1]):
                words[j], words[j+1] = words[j+1], words[j]
    return words

len_lambda = lambda string: len(string)
word_list = ['apple', 'banana', 'orange', 'grape']

print(sort_by_length(words=word_list, operation=len_lambda))

def sort_by_length_2(words: List[int], operation):
    return sorted(words, key=operation)

print(sort_by_length_2(words=word_list, operation=len_lambda))
