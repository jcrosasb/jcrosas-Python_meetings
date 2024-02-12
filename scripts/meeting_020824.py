list1 = [9]
list2 = [1, 'b', 'c']

#print(list1 > list2)

dict1 = {'a':1, 'b':2}
dict2 = {'a':3, 'b':4}

#print(dict1 == dict2)  # works

# print(dict1 > dict2)  # does not works

#print(dict1.values())  # Check if key is in dict

# Hash function:
#   (1) Given the same input it always returns the same output
#   (2) Different input may result in same output
# Something is hashable if it has a hashing function

# SET is a collection of unique hashable elements
x = 700
set1 = {3,2,1,8,9, 'hello', False, 4.56, 0, (3,2), x}  # Only has unique elements

x = 20

# print(x in set1)
# print(700 in set1)
# print((3,2) in set1)


def hash_function(x):
    return x % 5

#print(hash_function(19))

x = None
print(z == None)