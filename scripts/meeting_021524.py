# A list is ordered and mutable




fruits = ["apple", "banana", "cherry", "orange", "pineapple"]
veggies = ['lettuce', 'peas', 'onions', 'spinach']

# print(id(fruits))

# #a = fruits
# fruits.extend(veggies)

# #print(id(a))
# print(id(fruits))


# print(id(fruits + veggies))

# fruits_and_veggies = fruits + veggies
# print(fruits_and_veggies)

# fruits.pop()
# fruits.pop()
# print(fruits_and_veggies)

# veggies.extend('pumpkin')  # extend must be used with iterables
# print(veggies)

#print(fruits.index('cherry'))

#print(fruits[2])

numbers = [1,0,17,3,4,2,6,7,8,9,10, -1, 2,56,-20]

# ones_zeroes = [1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1, 1,1, 0,0, 1]

# num_zeroes = 0
# for number in ones_zeroes:
#     if number == 0:
#         num_zeroes += 1
# print(num_zeroes)

# print(ones_zeroes.count(2))

# # sorted_numbers = numbers[:]
# # sorted_numbers.sort()

# sorted_numbers = sorted(numbers)

# print(numbers)
# print(sorted_numbers)

# fruits_and_vegetables = [('orange', 'fruit'), 
#                          ('pickles', 'vegetable'), 
#                          ('apple', 'fruit'), 
#                          ('tomatoe', 'fruit'), 
#                          ('lettuce', 'vegetable'), 
#                          ('zuccini', 'vegetable')]

# def categories(item):
#     return item[1] 

# print((1,'orange', 'fruit') <= (-2,'Apple', 'fruit'))

# #fruits_and_vegetables.sort()
# fruits_and_vegetables.sort(key=lambda item: (item[1], item[0]))

# print(fruits_and_vegetables)


# numbers = (1,0,17,3,4,2,6,7,0,8,9,10, -1, 2,56,-20)

# for method in numbers.__dir__():
#     print(method)

# c=0
# for i in range(len(numbers)-1,-1,-1):
#     numbers[i] = numbers[c]
#     c += 1

i, j = 0, len(numbers)-1
while i != j and i < j:
    numbers[i], numbers[j] = numbers[j], numbers[i]
    i += 1
    j -= 1

#numbers=[1,2,3,4,5,6]
# for i in range(len(numbers)):
#     numbers.insert(i,numbers.pop())

#numbers = numbers[::-1]

# numbers.reverse()

# print(numbers)

numbers = (1,0,17,3,4,2,6,7,0,8,9,10, -1, 2,56,-20)

for method in numbers.__dir__():
    print(method)


person1 = ['Juan', 'Rosas', 39, ['UABC', 'UofT']]
person2 = ['Luis', 'Rosas', 36, ['UABC']]
person3 = ['Maria Elena', 'Bonilla', 70, ['UAG']]
person4 = ['Carlos', 'Rosas', 75, ['UAG']]

from typing import Any

people: list[list[Any]] = (person1, person2, person3, person4)

print(people)

# t: tuple = 2,5
# print(type(t))

# def fucntion(x,y):

#     return x,y

# fucntion(2,5)

# people[1][2] = 100

# print(people)

# print(people[1])

# print(people[2:3])

# p1, *middle, p4 = people
# middle = tuple(middle)

# person5 = ['Jose', 'perez', 15, ['UNAM']]

# # # print(people.__add__(person5))
# people = list(people)
# people.append(person5)

# people = tuple(people)
# print(people)

# people[0].append(person5)
# print(people)

# print(people[2][0])
# print(middle)

#(person2, person3)

# print(p1)
# print(p4)


