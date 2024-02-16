# string1 = 'asdasd'
# string2 = "asdasd"

# string3 = '''
# Hello ()
# world
# '''

# print(string3.strip())

# num_pi = 3.1415926535
# formatted_number = "{:.3f}".format(num_pi)
# print(formatted_number)

# def print_pi(num_decimal, num_pi):
#     #print("{:.3f}".format(num_pi))
#     format_string = "{:." + str(num_decimal) + "f}"
#     print(format_string)
#     print(format_string.format(num_pi))


# print_pi(6, num_pi)   


# if n, then you want a string of 2*n-1 slots

# def print_stars(num_lines):
#     for i in range(1, num_lines + 1):
#         print(' '*(num_lines-i) + '*'*(2*i-1))

# print_stars(5)



## Range function

# # From 0 to 4
# for i in range(5):
#     print(i)


# # From 1 to 4
# for i in range(5):
#     print(i)

# # From 0 to 9, in increments of 2
# for i in range(0,9,2):
#     print(i)

# # Negative numbers
# for i in range(0,-5,-1):
#     print(i)

# # Negative numbers 
# for i in range(0,-5,-1):
#     print(i)


fruits_and_vegetables = [('orange', 'fruit'), ('apple', 'fruit'), ('tomatoe', 'fruit'), ('lettuce', 'vegetable'), ('pickles', 'vegetable'), ('zuccini', 'vegetable')]

for i, (name, category) in enumerate(fruits_and_vegetables):
    #print("{}: {:10} {} ".format(i+1, name, category))
    print("{}: {:_>10} {} ".format(i+1, name, category))

# for i in [0,1,2,3,4,5]: #:range(1, len(fruits_and_vegetables), 2):
#     name, category = fruits_and_vegetables[i]
#     if name == 'pickles':
#         break
#     print("{}: {:_>10} {} ".format(i+1, name, category))
# else:
#     print('all done')

# list_even = list(range(2,100,2))
# print(list_even)

# i = 0
# while i < len(fruits_and_vegetables):
#     name, category = fruits_and_vegetables[i]
#     print("{}: {:_>10} {} ".format(i+1, name, category))
#     i += 1
 