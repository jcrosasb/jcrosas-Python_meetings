from typing import List


def custom_reduce(numbers: List[int], aggregation, initial: int) -> int:
    for number in numbers:
        initial = aggregation(initial, number)
    return initial


numbers_list = [1, 2, 3, 4, 5]
agg = lambda x,y: x + y**2
initial_value = 0
print(custom_reduce(numbers=numbers_list, aggregation=agg, initial=initial_value))


