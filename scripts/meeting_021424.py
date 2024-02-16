# fruits_and_vegetables = [('orange', 'fruit'), 
#                          ('apple', 'fruit'), 
#                          ('tomatoe', 'fruit'), 
#                          ('lettuce', 'vegetable'), 
#                          ('pickles', 'vegetable'), 
#                          ('zuccini', 'vegetable')]


# i = iter(fruits_and_vegetables)
# while item := next(i, None)[0] != 'pickels':
#     print(item)
#     # name, type = item
#     # print(name, type)


# i = iter(fruits_and_vegetables)
# while item := next(i, None):
#     name, type = item
#     if name == 'pickles':
#         break
#     print(name, type)

# i = iter(fruits_and_vegetables)
# name, type = next(i, None)
# while name != 'pickles':
#     print(name, type)
#     name, type = next(i, None)
    
# i = iter(fruits_and_vegetables)
# while (item := next(i, (None,))[0] != 'pickels':
#     name, type = item
#     print(name, type)

#non_empty_list = [1,2,3]

#print(non_empty_list.__len__())

#print(len(non_empty_list))

#print(non_empty_list.__dir__())

#print(len(dir(non_empty_list)))


# list1 = ['a', 'b']
# list2 = ['e', 'c']

# letters = [list1, list2]

# print('a' in [letters[0] for i in letters])

# print('a' in list1)



# numbers = [1,2,3,4,5]
# numbers_iterator = iter(numbers)

# while True:
#     item = next(numbers_iterator, None)  # None is used as the default value to indicate the end of iteration
#     if item is None:  # If the default value is returned, indicating the end of iteration
#         break  # Exit the loop
#     print(item)


# fruits = ("apple", "banana", "cherry", "orange", "pineapple")

# # Create iterator
# fruits_iterator = iter(fruits)

# next_fruit = next(fruits_iterator)
# while  next_fruit:
#     print(next_fruit)
#     next_fruit = next(fruits_iterator, False)


# fruits = ("apple", "banana", "cherry", "orange", "pineapple")

# # Create iterator
# fruits_iterator = iter(fruits)

# while  item := next(fruits_iterator, False):
#     print(item)

fruits = ("apple", "banana", "cherry", "orange", "pineapple")

# Create iterator
fruits_iterator = iter(fruits)

while  (item := next(fruits_iterator, False)) != 'orange':
    print(item)