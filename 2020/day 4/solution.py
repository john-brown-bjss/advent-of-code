import os
import re


def get_field_value(field, passport):
        start_index = passport.index(field)
        contains_space = passport[start_index:].__contains__(" ")
        if not contains_space:
            return passport[start_index:].replace(f'{field}:', '')
        else:
            end_index = passport.index(' ', start_index)
            return passport[start_index:end_index].replace(f'{field}:', '')
        

def validate_required_fields(passport):
    def validate_byr():
        field = get_field_value('byr', passport)
        if(len(field) != 4):
            return False

        field = int(field)
        if field >= 1920 and field <= 2002:
            return True
        return False

    def validate_iyr():
        field = get_field_value('iyr', passport)
        if(len(field) != 4):
            return False

        field = int(field)
        if field >= 2010 and field <= 2020:
            return True
        return False
    
    def validate_eyr():
        field = get_field_value('eyr', passport)
        if(len(field) != 4):
            return False

        field = int(field)
        if field >= 2020 and field <= 2030:
            return True
        return False

    def validate_hgt():
        field = get_field_value('hgt', passport)
        meaurement_type = field[-2:]
        if meaurement_type == 'cm':
            amount = int(field[:-2])
            if amount >= 150 and amount <= 193:
                return True
            return False
        elif meaurement_type == 'in':
            amount = int(field[:-2])
            if amount >= 59 and amount <= 76:
                return True
            return False
        else:
            return False
    
    def validate_hcl():
        field = get_field_value('hcl', passport)
        if field[0] != '#':
            return False
        
        field = field.replace('#', '')
        if len(field) != 6:
            return False

        is_valid = re.match('.*[0-9a-f].*', field)
        if is_valid:
            return True
        return False
    
    def validate_ecl():
        valid_eye_colors = [
            'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
        ]
        field = get_field_value('ecl', passport)
        if field not in valid_eye_colors:
            return False
        return True
    
    def validate_pid():
        field = get_field_value('pid', passport)
        is_valid = re.match('^\d{9}$', field)
        if is_valid:
            return True
        return False

    rule_engine = [
        validate_byr, validate_iyr, validate_eyr, validate_hgt,
        validate_hcl, validate_ecl, validate_pid
    ]

    try:
        for validation_rule in rule_engine:
            if not validation_rule():
                raise Exception('Not a valid passport')
    except:
        return False
    return True
    

def does_passport_contain_required_fields(passport):
    passport_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    result = list(filter(lambda x:  x in passport, passport_fields))
    return len(passport_fields) == len(result)

def sanitise_input(input):
    return input.replace('\n', ' ')

def validate_passport(input_file='inputs.txt'):
    path = os.path.join(os.path.dirname(__file__), input_file)
    valid_passports = []
    invalid_passports = []
    with open(path, 'r') as file_handle:
        passports = file_handle.read().split('\n\n')
        for passport in passports:
            passport = sanitise_input(passport)
            if does_passport_contain_required_fields(passport) and validate_required_fields(passport):
                valid_passports.append(passport)
            else:
                invalid_passports.append(passport)
    return valid_passports, invalid_passports


if __name__ == "__main__":
    valid_passports, invalid_passports = validate_passport()
    print(f'Part A solution: {len(valid_passports)} valid passports')