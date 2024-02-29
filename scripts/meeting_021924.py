# import random
# import time
# random.seed(42)

# # Generate a list of 1000 random numbers
# # numbers_list = [random.randint(0, 100000) for _ in range(1000)]
# numbers_list = list(range(1000000))
# numbers_set = set(numbers_list)
# numbers_dict = {str(num): num for num in numbers_list}

# number = 10


# def search_for_number(data_structure, number):
#     start = time.time()
#     number in data_structure
#     end = time.time()
#     return end - start

# print(f'Time to seach in list = {search_for_number(numbers_list, number)}\n'
#       f'Time to seach in set = {search_for_number(numbers_set, number)}\n'
#       f'Time to seach in dict = {search_for_number(numbers_dict, number)}')

# Dictionary: mutable collection of key-value pairs

# empty_dict = {}

# print(type(empty_dict))

# for method in empty_dict.__dir__():
#     print(method)


# person1 = ['Juan', 'Rosas', 39, ['UABC', 'UofT']]
# person2 = ['Luis', 'Rosas', 36, ['UABC']]
# person3 = ['Maria Elena', 'Bonilla', 70, ['UAG']]
# person4 = ['Carlos', 'Rosas', 75, ['UAG']]

person1 = {"first_name": 'Juan',
           "last_name": 'Rosas', 
           "age": 39, 
           "city": 'Tijuana',
           "school": {"undergraduate": 'UABC', 
                      "graduate": 'UofT'},
           "married": True}

person2 = {"first_name": 'Luis', 
           "last_name": 'Rosasss', 
           "age": 399, 
           "city": 'Tijuana',
           "school": {"undergraduate": 'UNAM',
                      "graduate": None}}

#print(person1["school"]["graduate"])
# print(person2["school"]["graduate"])
    
# Two methods to add a key-value pair to dict
#person1["city"] = 'Tijuana'
#person2["city"] = 'Tijuana'
#person1.update({"city": 'Tijuana'})

#person1.update(person2)

#people = {}.fromkeys(person1.keys())

#for person in [person1, person2]:
#    for key in list(people.keys()):
#        people[key].append()

# for key in people:
#     people[key] = [person1[key], person2[key]]

# for key in people:
#     people[key] = []
#     print(id(people[key]))
#     for person in [person1, person2]:
#         people[key].append(person[key])

def merge_obj_values(*objs):
    people = {}
    for obj in objs:
        for key in obj:
            people.setdefault(key, []).append(obj[key])
    return people

people2 = merge_obj_values(person1, person2)
#print(people2)

# person1.pop("age")

# print(person1)

# person1.popitem()

# print(person1)

# person1.popitem()

# print(person1)

# person1.clear()
# print(person1)

#print(person1.keys())

#person1["cities"] = 'Ensenada'

#eliminated = person1.pop("city")



#person1["cities"] = [person1.pop("city")]
#
#print(person1.keys())

# for key in person1.keys():
#     if key == 'last_name':
#         key = 'family_name'
#     #print(key)

# print(person1.keys())

#print(person1)

fruits_and_veggies = {"orange": 'fruit', 
                      "carrots": 'veggie',
                      "banana": 'fruit',
                      "lettuce": 'veggie'}

veggies_and_fruits = {}
for k,v in fruits_and_veggies.items():
    veggies_and_fruits.setdefault(v, []).append(k)

#print(veggies_and_fruits)

greeting = 'Hello everyone'
greetings = [greeting] * 10

#for i in range(len(greetings)):
#    print(greetings[i]) 

for foo in greetings:
    print(foo)

for _ in greeting:
    print(greeting)



# c = 10
# while c > 0:
#     print(greeting)
#     c -= 1

# print(id(people["first_name"]))
# print(id(people["last_name"]))


#print(people)

#print(list(person1.values()))
    

def merge_dictionaries(*dictionaries):
    merged_dict = {}
    for dictionary in dictionaries:
        for key in dictionary:
            merged_dict.setdefault(key, []).append(dictionary[key])
    return merged_dict


person1 = {"first_name": 'Juan',
           "last_name": 'Rosas', 
           "age": 39, 
           "city": 'Tijuana',
           "school": {"undergraduate": 'UABC', 
                      "graduate": 'UofT'},
           "married": True}

person2 = {"first_name": 'Luis', 
           "last_name": 'Rosas', 
           "age": 36, 
           "city": 'Toronto',
           "school": {"undergraduate": 'UABC',
                      "graduate": 'UdeS'}}

people = merge_dictionaries(person1, person2)

