import os
import copy
from collections import Counter


class SeatFinder():

    def __init__(self, seating_plan):
        self.seating_plan = seating_plan

    def get_adjacent_cels(self, x, y):
        cells = [
            self.correct_bounds(x, y-1), # top
            self.correct_bounds(x-1, y), # left
            self.correct_bounds(x+1, y), # right
            self.correct_bounds(x, y+1), # bottom
            self.correct_bounds(x-1, y+1), # bottom_left
            self.correct_bounds(x+1, y+1), # bottom_right
            self.correct_bounds(x-1, y-1), # top_left
            self.correct_bounds(x+1, y-1), # top_right
        ]
        return [cell for cell in cells if cell] 

    def get_first_visible_seat(self, x, y):
        directions = [
            [0, -1],
            [-1, 0],
            [+1, 0],
            [0, +1],
            [-1, +1],
            [+1, +1],
            [-1, -1],
            [+1, -1]
        ]
        seat_locations = []
        for d_x, d_y in directions:
            get_next_position = True
            count_x = 0
            count_y = 0
            while get_next_position:
                new_pos = self.correct_bounds((x + d_x) + count_x, (y + d_y) + count_y)
                if new_pos:
                    _x = new_pos[0]
                    _y = new_pos[1]
                    new_seat = self.seating_plan[_y][_x]
                    if new_seat != '.':
                        seat_locations.append([_x, _y])
                        get_next_position = False
                else:
                    get_next_position = False
                count_x += d_x
                count_y += d_y

        return seat_locations

    def correct_bounds(self, x, y):
        if x < 0 or y < 0 or x >= len(self.seating_plan[0]) or y >= len(self.seating_plan):
            return None
        return x, y


def should_become_occupied(x, y, adjacent_cells, seating_plan):
    any_occupied_seats = any(seating_plan[_y][_x] == '#' for _x, _y in adjacent_cells)
    return not any_occupied_seats and seating_plan[y][x] == 'L'


def should_become_empty(x, y, adjacent_cells, seating_plan, tollerence):
    occupied_cells = [True for _x, _y in adjacent_cells if seating_plan[_y][_x] == '#' ]
    return len(occupied_cells) > tollerence and seating_plan[y][x] == '#'


def run_seat_rules(x, y, adjacent_cells, seating_plan, tollerence=3):
    if should_become_occupied(x, y, adjacent_cells, seating_plan):
        return '#'
    elif should_become_empty(x, y, adjacent_cells, seating_plan, tollerence):
        return 'L'
    else:
        return seating_plan[y][x]


def part_a_traverser(seating_plan):
    new_seating_plan = copy.deepcopy(seating_plan)
    adjacent_cell_finder = SeatFinder(seating_plan)

    for y in range(len(seating_plan)):
        for x in range(len(seating_plan[y])):
            adjacent_cells = adjacent_cell_finder.get_adjacent_cels(x, y)
            state = run_seat_rules(x, y, adjacent_cells, seating_plan)
            new_seating_plan[y][x] = state

    return new_seating_plan


def part_b_traverser(seating_plan):
    new_seating_plan = copy.deepcopy(seating_plan)
    adjacent_cell_finder = SeatFinder(seating_plan)

    for y in range(len(seating_plan)):
        for x in range(len(seating_plan[y])):
            adjacent_cells = adjacent_cell_finder.get_first_visible_seat(x, y)
            state = run_seat_rules(x, y, adjacent_cells, seating_plan, tollerence=4)
            new_seating_plan[y][x] = state

    return new_seating_plan


def solve_part_a(seating_plan):
    is_seating_plan_stable = False
    previous_seating_plan = copy.deepcopy(seating_plan)
    while not is_seating_plan_stable:
        new_seating_plan = part_a_traverser(previous_seating_plan)
        is_seating_plan_stable = new_seating_plan == previous_seating_plan
        previous_seating_plan = new_seating_plan

    return sum(row.count('#') for row in previous_seating_plan)


def solve_part_b(seating_plan):
    is_seating_plan_stable = False
    previous_seating_plan = copy.deepcopy(seating_plan)
    while not is_seating_plan_stable:
        new_seating_plan = part_b_traverser(previous_seating_plan)
        is_seating_plan_stable = new_seating_plan == previous_seating_plan
        previous_seating_plan = new_seating_plan

    return sum(row.count('#') for row in previous_seating_plan)




def read_and_process_file(file='inputs.txt'):
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path, 'r') as file_handle:
        read_file = file_handle.read().splitlines()
        seating_plan = []
        for row in read_file:
            data = []
            data.extend(row)
            seating_plan.append(data)
            
        return [
            solve_part_a(seating_plan),
            solve_part_b(seating_plan)
        ]

if  __name__ == "__main__":
    part_a, part_b = read_and_process_file()

    print(f'Solution to part a: {part_a}')
    print(f'Solution to part b: {part_b}')
    