
# This example is from Data Structures Tutorial
word = 'screws'
data_map = [None] * 7

my_hash = 0
for letter in word:
    my_hash = (my_hash + ord(letter) * 23) % len(data_map)

#print(my_hash)


print(hash(2))  # Test for ints

print(hash(2.3))  # Test for floats

print(hash('hello'))  # Test for strings

print(hash((1,2,3)))  # Test for tuples