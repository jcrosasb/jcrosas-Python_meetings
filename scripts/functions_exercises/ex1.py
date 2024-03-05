from typing import List

def sum_list(numbers: List[int]) -> int:
    summation = 0
    for number in numbers:
        summation += number
    return summation


def prod_list(numbers: List[int]) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product


def min_list(numbers: List[int]) -> int:
    min = numbers[0]
    for index in range(1,len(numbers)):
        if numbers[index] < min:
            min = numbers[index]
    return min


def max_list(numbers: List[int]) -> int:
    max = numbers[0]
    for index in range(1,len(numbers)):
        if numbers[index] > max:
            max = numbers[index]
    return max 


if __name__ == '__main__':

    list_of_numbers = [1, 2, 3, 4, 5]
    
    print(sum_list(numbers=list_of_numbers))
    print(prod_list(numbers=list_of_numbers))
    print(min_list(numbers=[3,6,-10,-1,-8, 9, 15]))
    print(max_list(numbers=[3,6,-10,-1,-8, 9, 15]))