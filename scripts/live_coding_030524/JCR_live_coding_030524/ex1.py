from typing import Dict

def divisors(number: int) -> Dict:
    '''Function to return all divisors of all numbers from 1 to 'number'
       Parameters:
            number: (integer) Upper limit of numbers on which all divisors will be calculated
       Returns:
            A dictionary with the numbers up to 'number' as keys. The values will be the divisors of each number
    '''
    # Here I create a dict comprehension which uses a list comprehension inside
    # The list comprehension is: 
    #
    #       [inner_num for inner_num in range(1, (outer_num//2 + 1)) if outer_num % inner_num == 0] + [outer_num],
    #
    # where inner number is the number that is being iterated and outer number is the number to which we want to get the divisors.
    # The list comprehension sweeps from 1 to (outer_num//2 + 1). The reason for this is that any number above this cannot be a divisor,
    # so there is no need to sweep them. The result will be a list with all divisors of the outer number, plus the outer number itself
    # added via concatenation (+)
    #
    # One we have the listh comprehension with the divisors for each number, we just iterate in a dict comprehension over the 
    # range (1, number+1), using outer number as a key and the list comprehension as a value
    return {outer_num:[inner_num for inner_num in range(1, (outer_num//2 + 1)) if outer_num % inner_num == 0] + [outer_num] for outer_num in range(1, number+1)}
    

if __name__ == '__main__':

    result = divisors(10)

    for key, value in result.items():
        print(f'{key}: {value}')
