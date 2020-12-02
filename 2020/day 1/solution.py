import os
from itertools import combinations
from math import prod


def sanitise_input(input):
    return int(input.replace('/n', ''))


def get_sum_of_multiples(x):
    path = os.path.join(os.path.dirname(__file__), 'inputs.txt')
    with open(path, 'r') as file_handle:
        data = file_handle.readlines()
        all_combinations = combinations(data, x)
        for multiples in all_combinations:
            santised_multiples = [sanitise_input(multiple) for multiple in multiples]
            if sum(santised_multiples) == 2020:
                return prod(santised_multiples)
        

if __name__ == "__main__":
    part_1 = get_sum_of_multiples(2)
    part_2 = get_sum_of_multiples(3)
    print(f'Part 1: {part_1}\nPart 2: {part_2}')