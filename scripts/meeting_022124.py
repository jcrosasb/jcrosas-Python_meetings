from typing import List
# numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)

# iterator = iter(range(5))

# for number in iterator:
#     print(number)

# for number in numbers:
#     print(number)

# for number in iterator:
#     print(number)
    
# def generator_function(data):
#     for item in data:
#         yield item
#     # yield data  # returns an iterator

# custom_generator = generator_function(range(1,6))

# for item in custom_generator:
#     print(item)

# for item in custom_generator:
#     print(item)

# for method in generator_function([1,2,3,4,5]).__dir__():
#     print(method)
    

def lazy_caterer_number(data: List[int]):
    for number in data:
        yield (number**2 + number + 2) // 2

def lazy_caterer_number_2(data: List[int]):
    my_list = []
    for number in data:
        my_list.append((number**2 + number + 2) // 2)
    return my_list

numbers = [1,2,3,4,5]

sequence = iter(lazy_caterer_number_2(numbers))

lazy_caterer_number_3 = ((number**2 + number + 2) // 2 for number in numbers)

print(type(lazy_caterer_number_3))

for number in lazy_caterer_number_3:
    print(number)


word = 'qwds12312@knaf'
print(word.replace('@', ' ').capitalize()[::-1])
#print(word)