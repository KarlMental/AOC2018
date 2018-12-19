import functions
from copy import deepcopy

def run_all_functions(registers, instruction, func_dict):
    returns = {}
    for key, value in func_dict.items():
        returns[key] = tuple(value(instruction, deepcopy(registers)))
    return returns

def add_functions_to_dict():
    returns = {}
    for i in dir(functions):
        function = getattr(functions,i)
        if callable(function) and not i.startswith('__'):
            returns[i] = function
    return returns

def get_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    return_data = []
    for i in range(0, len(data), 4):
        return_data.append([string_to_int_list(data[i+j]) for j in range(3)])
    return return_data

def get_test_input():
    with open('input2.txt', 'r') as f:
        data = f.read().split('\n')
    return_data = [string_to_int_list(row) for row in data]
    return return_data

def string_to_int_list(string):
    return_list = []
    if '[' in string:
        for char in string:
            try:
                return_list.append(int(char))
            except:
                pass
    else:
        for char in string.split():
            return_list.append(int(char))
    return return_list

def keep_only_overlaps(dictionary):
    for key, value in dictionary.items():
        dictionary[key] = list(set.intersection(*map(set, value)))
    return dictionary

def keep_only_one(dictionary):
    while True:
        for key, value in dictionary.items():
            if len(value) == 1:
                dictionary = strip_duplicate(dictionary, value[0])
        if len(dictionary.keys()) == sum([len(value) for key, value in dictionary.items()]):
            for key, value in dictionary.items():
                dictionary[key] = value[0]
            break
    return dictionary

def strip_duplicate(dictionary, dup):
    for key, value in dictionary.items():
            if len(value) > 1:
                dictionary[key] = [a for a in value if a != dup]
    return dictionary

tests = get_input()

cnt = 0
func_dict = add_functions_to_dict()
functions_number = {}
for case in tests:
    results = run_all_functions(case[0], case[1][1:], func_dict)
    working_functions = []
    for key, value in results.items():
        if value == tuple(case[2]):
            working_functions.append(key)
    if str(case[1][0]) not in functions_number.keys():
        functions_number[str(case[1][0])] = [working_functions]
    else:
        functions_number[str(case[1][0])].append(working_functions)

functions_number = keep_only_overlaps(functions_number)
functions_number = keep_only_one(functions_number)

test = get_test_input()
registers = [0,0,0,0]
for run in test:
    registers = func_dict[functions_number[str(run[0])]](run[1:], registers)

print(registers)

