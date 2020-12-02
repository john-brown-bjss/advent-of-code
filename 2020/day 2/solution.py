import os
import re


def password_policy_1(password_data):
    required_letter = get_required_letter(password_data)
    min_count, max_count = get_required_count_for_letter(password_data)
    password = password_data.split(' ')[-1]
    occurances = password.count(required_letter)
    return True if occurances >= min_count and occurances <= max_count else False


def password_policy_2(password_data):
    required_letter = get_required_letter(password_data)
    position_1, position_2 = get_required_count_for_letter(password_data)
    password = password_data.split(' ')[-1]
    letter_a = int(password[position_1 - 1] == required_letter)
    letter_b = int(password[position_2 - 1] == required_letter)
    return True if letter_a + letter_b == 1 else False


def get_required_letter(password):
    split_password = password.split(' ')
    return split_password[1].replace(':', '')


def get_required_count_for_letter(password):
    split_password = password.split(' ')
    requirements = split_password[0]
    min, max = requirements.split('-')
    return [int(min), int(max)]


def get_password_counts(password_policy):
    path = os.path.join(os.path.dirname(__file__), 'inputs.txt')
    incorrect_passwords = []
    correct_passwords = []
    with open(path, 'r') as file_handle:
        data = file_handle.read().splitlines()
        for password in data:
            if password_policy(password.lower()):
                correct_passwords.append(password)
            else:
                incorrect_passwords.append(password)

    return correct_passwords, incorrect_passwords


if __name__ == "__main__":
    policies = [ 
        ['Part 1:', password_policy_1], 
        ['Part 2:', password_policy_2] 
    ]
    for prefix, password_policy in policies:
        correct_passwords, incorrect_passwords = get_password_counts(password_policy)
        print(f'Number of correct passwords for {prefix} {len(correct_passwords)}')
        print(f'Number of incorrect passwords for {prefix} {len(incorrect_passwords)}')