# Sets are mutable
#numbers = {1,2,3,'a',4,10,5,6}
# numbers = [1,10,2,3]
# # print(numbers)
# # print(id(numbers))
# # numbers.remove(1)
# # #print(removed_element)

# # print(numbers)
# # # print(id(numbers))

# # numbers.add(1)
# # print(id(numbers))

# for elem in numbers:
#     print(elem)

# set2 = {5,7,8,numbers}

# numbers = {1,2,3}
# numbers2 = {3,2,1}
# print(numbers==numbers2)

numbers = {1,2,3,4,5,6,7,8,9,10}

even = set()
for number in numbers:
    if number % 2 == 0:
        even.add(number)
print(even)

odd = numbers.difference(even)
print(odd)

test = {number for number in numbers if number % 2 == 0}

print(test)

set_test = {1,2,3, frozenset([1, 2, 3, 4])}

set1 = {1,2,3}
for method in set1.__dir__():
    print(method)