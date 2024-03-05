names = ['Saul', 'Goodman', 'Walther', 'White']

letters = set()

for name in names:
    for char in name:
        letters.add(char)

print(letters)

letters_2 = {char for name in names for char in name}
print(letters_2)