import os
from math import ceil, floor


def calculate_seat_id(row, column):
    return row * 8 + column


def partition(character, lower, upper, upper_char='B', lower_char='F'):
    if character == lower_char:
        return [lower, floor((upper + lower) / 2)]
    elif character == upper_char:
        return [ ceil( (upper + lower) / 2), upper]


def get_row(boarding_pass):
    lower_division = 0
    upper_division = 127
    for character in boarding_pass[:7]:
        lower_division, upper_division = partition(character, lower_division, upper_division)
    return lower_division if character == 'F' else upper_division


def get_column(boarding_pass):
    lower_division = 0
    upper_division = 7
    for character in boarding_pass[7:]:
        lower_division, upper_division = partition(character, lower_division, upper_division, upper_char='R', lower_char='L')
    return lower_division if character == 'L' else upper_division


def get_seat_location(boarding_pass):
    row = get_row(boarding_pass)
    column = get_column(boarding_pass)
    seat_id = calculate_seat_id(row, column)
    return row, column, seat_id


def build_seat_id_list(input_file='inputs.txt'):
    path = os.path.join(os.path.dirname(__file__), input_file)
    seat_list = []
    with open(path, 'r') as file_handle:
        boarding_passes = file_handle.read().splitlines()
        for boarding_pass in boarding_passes:
            seat_list.append(get_seat_location(boarding_pass.upper()))
    return seat_list


if __name__ == "__main__":
    seat_list = build_seat_id_list(input_file='inputs.txt')
    seat_list.sort(key=lambda x: x[2])
    my_seat_index = list(filter(lambda x: seat_list[x][2] - seat_list[x-1][2] != 1, range(1, len(seat_list))))[0]

    print(f'Solution to part a: {seat_list[-1][2]}')
    print(f'Solution to part b: {seat_list[my_seat_index][2]-1}')
