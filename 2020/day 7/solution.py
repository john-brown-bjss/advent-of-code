import os
import re
from string import digits


REQUIRED_BAG = 'shiny gold'


def search_for_shiny_gold_bags(bags):
    def search_for_goal(bag):
        if bag:
            if REQUIRED_BAG in bags[bag]:
                return True
            else:
                return True in [search_for_goal(nextbag) for nextbag in bags[bag]]

    return [search_for_goal(bag) for bag in bags]
        

def count_number_of_shiny_bags(bags):
    def search_for_goal(bag):
        if bag:
            total = 0
            for nextbag in bags[bag]:
                total += bags[bag][nextbag] * (search_for_goal(nextbag) + 1)
            return total
    return search_for_goal(REQUIRED_BAG)

def convert_bags_to_dict(bags):
    bag_dict = {}
    for bag in bags:
        line, contents = bag.replace(' bags', '').replace(' bag', '').replace('.', '').split(' contain ')
        amounts =  [int(contents) for contents in contents.split() if contents.isdigit()]
        remove_digits = str.maketrans('', '', digits)
        colours = contents.translate(remove_digits).strip().split(', ')
        bag_dict[line] = {colours[i].strip(): amounts[i] for i in range(len(amounts))}
    return bag_dict


def read_and_process_file(file='inputs.txt'):
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path, 'r') as file_handle:
        bags = file_handle.read().splitlines()
        bag_dict = convert_bags_to_dict(bags)
        return [
            search_for_shiny_gold_bags(bag_dict).count(True),
            count_number_of_shiny_bags(bag_dict)
        ]


if __name__ == "__main__":
    part_a, part_b = read_and_process_file()

    print(f'Solution to part a: {part_a}')
    print(f'Solution to part b: {part_b}')
