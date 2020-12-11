import os
from collections import Counter

def does_permutation_exist(permutations, permutation, element_to_remove):
    permutation.remove(element_to_remove)
    return permutation in permutations


def get_all_permutations_in_adaptor_chain(power_converters):
    power_converters.append(max(power_converters) + 3)

    combinations = {0: 1}
    for power_converter in power_converters:
        combinations[power_converter] = (
            combinations.get(power_converter - 1, 0) +
            combinations.get(power_converter - 2, 0) +
            combinations.get(power_converter - 3, 0)
        )

    return combinations[power_converters[-1]]


def get_occurences_in_adaptor_chain(power_converters):
    joltage_differences = [min(power_converters) - 0]

    for index in range(1, len(power_converters)):
        difference = power_converters[index] - power_converters[index-1]
        joltage_differences.append(difference)
    
    joltage_differences.append(3)
    return Counter(joltage_differences)


def read_and_process_file(file='inputs.txt'):
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path, 'r') as file_handle:
        power_converters = [int(x) for x in file_handle.read().splitlines()]
        power_converters.sort()
        return [
            get_occurences_in_adaptor_chain(power_converters),
            get_all_permutations_in_adaptor_chain(power_converters)
        ]


if __name__ == "__main__":
    part_a, part_b = read_and_process_file()

    # Part a solution
    one_jolt_differences = part_a.get(1, 0)
    three_jolt_differences = part_a.get(3, 0)
    print(f'Solution to part a: {one_jolt_differences * three_jolt_differences}')
    
    # Part b solution
    print(f'Solution to part b: {part_b}')