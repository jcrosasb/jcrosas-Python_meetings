# Exercise 1. Number and comprehension. A vast majority of number-related problems can be solved with arrays. Use list comprehension to solve the following problems.

#  Given an integer n, write a program to get the list of square numbers up to n
def square_up_to_n(number):
    return [num**2 for num in range(1,number+1)]


#  Given an integer n, write a program to get all the even numbers between 1 and n
def even_up_to_n(number):
    return [num for num in range(2,number+1,2)]


#  Given an integer n, write a program to get all the odd numbers between 1 and n
def odd_up_to_n(number):
    return [num for num in range(1,number+1,2)]


#  Get all the prime numbers between 1 and 100 using list comprehension
def is_prime(number):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
             if number % i == 0:
                 return False
        return True
    return False

# lambda_prime = lambda x: is_prime(x)
# numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers2 = list(map(lambda_prime, numbers))
# print(numbers2)

primes_up_to_100 = [num for num in range(1,101) if is_prime(number=num)]

# primes_up_to_100 = [num for num in range(2, 101) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

# num = 10
# generator = (num % i != 0 for i in range(2, int(num**0.5) + 1))

# Bonus: Generate the first 20 numbers of the Triangular numbers sequence using list comprehension.
triangular_up_to_20 = [(number**2 + number) // 2 for number in range(1,21)]


if __name__ == "__main__":

    n = 10
    print(f'List with square numbers up to {n}: {square_up_to_n(n)}\n')
    print(f'List with even numbers up to {n}: {even_up_to_n(n)}\n')
    print(f'List with odd numbers up to {n}: {odd_up_to_n(n)}\n')
    print(f'List with all prime numbers between 1 and 100: {primes_up_to_100}\n')
    print(f'List with the first 20 triangular numbers: {triangular_up_to_20}')


