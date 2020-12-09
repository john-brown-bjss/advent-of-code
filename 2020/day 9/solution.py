import os
from itertools import combinations


def solve_part_b(cypher, failed_value):
    for continuos_amount in range(2, len(cypher)):
        for index in range(len(cypher)):
            data = cypher[index: continuos_amount + index]
            if sum(data) == failed_value:
                return min(data), max(data)


def is_sum_of_preamble(preamble, value):
    for sum_1 in range(len(preamble)):
        for sum_2 in range(1, len(preamble)):
            if preamble[sum_1] + preamble[sum_2] == value:
                return preamble[sum_1], preamble[sum_2]
    

def solve_part_a(cypher):
    preamble_length = 25
    preambles = []
    for index in range(preamble_length, len(cypher)):
        preamble = cypher[index-preamble_length: index]
        preamble_sums = is_sum_of_preamble(preamble, cypher[index])
        if not preamble_sums:
            return preambles, cypher[index]
        preambles.append(preamble) 


def read_and_process_file(file='inputs.txt'):
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path, 'r') as file_handle:
        cypher = [int(x) for x in file_handle.read().splitlines()]
        sums, value = solve_part_a(cypher)
        min_val, max_val = solve_part_b(cypher, value)
        print(f'Solution to part a: {value}')
        print(f'Solution to part b: {min_val + max_val}')


if __name__ == "__main__":
    read_and_process_file(file='inputs.txt')
