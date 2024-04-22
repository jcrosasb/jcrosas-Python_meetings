from typing import Dict

def divisors(number: int) -> Dict:
    '''Function to return all divisors of all numbers from 1 to 'number'
       Parameters:
            number: (integer) Upper limit of numbers on which all divisors will be calculated
       Returns:
            A dictionary with the numbers up to 'number' as keys. The values will be the divisors of each number
    '''
    return {outer_num:[inner_num for inner_num in range(1, outer_num+1) if outer_num % inner_num == 0] for outer_num in range(1, number+1)}


if __name__ == '__main__':

    result = divisors(10)

    for key, value in result.items():
        print(f'{key}: {value}')

# Adjust the range