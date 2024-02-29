
# numbers = [print(number**2) for number in [1,2,3,4,5]]
# print(numbers)


letters_numbers = {'a':1,
                   'b':2,
                   'c':3}

def is_prime(integer: int, another_int: int):
    if integer > 1:
        for i in range(2, int(integer**0.5) + 1, 2):
             if integer % i == 0:
                 return False
        return True
    return False

# # letters_number_2 = {key:value for key, value in [('a',1),('b',2),('c',3)]}
# letters_number_2 = {key.capitalize():is_prime(value) for key, value in letters_numbers.items()}

# print(letters_number_2)

# for key,value in letters_numbers.items():
#     letters_numbers[key] = is_prime(value)

# print(letters_numbers.items())

# letters_number_3 = {number:number**3 for number in range(10)}

# print(letters_number_3)

# letters_number_4 = dict([('a',1),('b',2),('c',3)])

# print(letters_number_4)
# print(list(letters_number_3.items()))

# cities_temps_C = {'Morelia': 24,
#                 'Oaxaca': 30,
#                 'Ensenada': 18,
#                 'Tijauan': 17}

# def convert_C_to_F(temp):
#     return 1.8*temp + 32

# cities_temps_F = {city:convert_C_to_F(temp) for city,temp in cities_temps_C.items()}
# print(cities_temps_F)

# names = ['Juan', 'Sol', 'Salvador', 'David', 'Sol', 'Salvador']

# name_count = {name:names.count(name) for name in names}
# print(name_count)



# operations = {'add': lambda x, y: x + y, 
#               'subtract': lambda x, y: x - y, 
#               'multiplication': lambda x, y: x * y, 
#               'constant':lambda x, y: 42}

# result_for_10_5 = {operation: operations[operation](10,5) for operation in operations}
# print(result_for_10_5)


# numbers = {number:number for number in []}
# print(numbers)

# names_grades = [('Juan',10), ('Sol',11), ('Salvador',12), ('David',13), ('Sol',14), ('Salvador',15), ('Juan',8)]

# #names_grades.sort(reverse=True)

# print(names_grades)

# names_grades_dict = {frozenset(name):grade for name,grade in names_grades}
# print(names_grades_dict)



# hashable_list = [({'a','b'}, 1), ({'z','x'}, 2), ({'f','h'}, 3)]
# hashable_list_dict = {frozenset(key):value for key, value in hashable_list}


# names_gardes_dict = {print(name):grade for name,grade in names_grades}
# print(names_gardes_dict)



# #numbers = [1,2,3,4,.......,1e9]
# numbers = [i for i in range(1e7)]
# for number in numbers:
#     print(number)

# for number in range(1e7):
#     print(number)


students = [{'name': 'Alice', 'score': 85},{'name': 'Bob', 'score': 92},

               {'name': 'Alice', 'score': 78},{'name': 'Charlie', 'score': 89},

               {'name': 'Bob', 'score': 95}, {'name': 'Alice', 'score': 90},

               {'name': 'David', 'score': 88} ]


highest_scores = {student['name']:student['score'] for student in students}

print(highest_scores)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6,7,8}



inter = {number for number in set1 if number not in set2}
print(inter)




# scores = {'John':12,'Steve':34}

# print(max(scores))
