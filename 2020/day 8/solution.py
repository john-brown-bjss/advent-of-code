import os
import re
from string import digits


def get_accumulation(instructions):
    accumulator = 0
    for value in instructions:
        instruction = instructions[value]
        data = list(instruction.keys())[0]
        if 'acc' in data:
            direction = data[4:5]
            if direction == '+':
                accumulator += int(data[5:])
            elif direction == '-':
                accumulator -= int(data[5:])
    return accumulator


def run_instruction(instruction_set, location):
    instruction = instruction_set[:3]
    amount = max(1, int(instruction_set[5:]))
    direction = instruction_set[4:5]
    
    if instruction == 'nop':
        location += 1
    elif instruction == 'acc':
        location += 1
    elif instruction == 'jmp':
        if direction == '+':
            location += amount
        elif direction == '-':
            location -= amount
    else:
        raise Exception(f'Unknown instruction: {instruction}')
    return location


def find_infinite_loop_and_fix(boot_code):
    jmp_indexs = [index for index, instruction in enumerate(boot_code) if 'jmp' in instruction]

    for jump_index in jmp_indexs:
        instructions = {}
        location = 0
        boot_code[jump_index] = 'nop ' + boot_code[jump_index][4:]
        while(location < len(boot_code)):
            try:
                instruction_set = boot_code[location]
                if location in instructions:
                    raise Exception('Infinite loop exists')
                instructions[location] = {instruction_set: location}
                location = run_instruction(instruction_set, location)
            except Exception as ex:
                location = -1
                break
        if location != -1:
            return get_accumulation(instructions)
        boot_code[jump_index] = 'jmp ' + boot_code[jump_index][4:]


def run_boot_code(boot_code):
    instructions = {}
    location = 0
    stop_occured = False
    while(not stop_occured):
        try:
            instruction_set = boot_code[location]
            if location in instructions:
                raise Exception('Infinite loop exists')
            instructions[location] = {instruction_set: location}
            location = run_instruction(instruction_set, location)
        except Exception as ex:
            print(str(ex))
            stop_occured = True
    
    return get_accumulation(instructions)
    

def read_and_process_file(file='inputs.txt'):
    path = os.path.join(os.path.dirname(__file__), file)
    with open(path, 'r') as file_handle:
        boot_code = file_handle.read().splitlines()
        return [
            run_boot_code(boot_code),
            find_infinite_loop_and_fix(boot_code)
        ]


if __name__ == "__main__":
    part_a, part_b = read_and_process_file()

    print(f'Solution to part a: {part_a}')
    print(f'Solution to part b: {part_b}')
