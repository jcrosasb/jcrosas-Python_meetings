list1 = [0,1,2,3,4,5,6,7,8,9,10,11]

print(list1[7])  # Get the 7-th index

print(len(list1))  # Length

print(list1[0])  # First element

print(list1[len(list1) - 1])  # last element
print(list1[-1])


print(list1[-3])  # The third to last element

print(list1[-3:])  # Get the last 3

print(list1[1:-1])  # Ignore first and last elements. Creates a shallow copy

list1 = [0,1,[2],3,4,5,6,7,8,9,10,11]

# list1[2][0] = list1[2][0]*10
list1[2][0] *= 10
print(list1)

print(list1[::2])  # Get every second element (even)
print(list1[1::2])  # Get every second element (odd)

# This works with strings
string1 = 'abcdefghij'
print(string1[::2])

print([20] in list1)  # Check if element in list
print([20,1] in list1)


