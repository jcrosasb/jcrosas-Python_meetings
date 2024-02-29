# import time

# def recursive_factorial(n):
#     if n == 0:
#         return 1
#     return n * recursive_factorial(n-1)

# start = time.time()
# recursive_factorial(205)
# end = time.time()
# print(end-start)

# def iter_factorial(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial *= i
#     return factorial

# start = time.time()
# iter_factorial(205)
# end = time.time()
# print(end-start)

# assigment, define initialize(), iter(), next() using an OOP approach



numbers = [1,2,3,4,5]

def initialize(data):
    global index
    index = 0
    return data, index

def itera(data):
    '''The method is responsible for returning an iterator object'''
    return data

def nexte(data):
    global index 
    index += 1
    if index <= len(data):
        return data[index-1]
    else:
        pass
        #raise StopIteration

    
print(initialize(numbers))

print(nexte(numbers))
print(nexte(numbers))
print(nexte(numbers))

print(numbers)
print(numbers.pop())
print(numbers)

# my_list = [1, 2, 3, 4, 5]
# my_list.pop()  # Removes and returns the last element
# print(my_list) 