stream = ['Saul', 'calls', 'Walther', 'calls', 'Saul', 'calls', 'Jessi']

# indexes = [index for index, word in enumerate(stream) if word == 'calls']
# print(indexes)

words_and_position = {}
for word in stream:
    words_and_position[word] = [index for index, item in enumerate(stream) if item == word]

print(words_and_position)

words_and_position_2 = {word:[index for index, item in enumerate(stream) if item == word] for word in stream}
print(words_and_position_2)