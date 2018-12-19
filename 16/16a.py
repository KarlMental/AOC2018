import functions
from copy import deepcopy

def run_all_functions(registers, instruction):
    returns = {}
    for i in dir(functions):
        function = getattr(functions,i)
        if callable(function) and not i.startswith('__'):
            returns[i] = tuple(function(instruction, deepcopy(registers)))
    return returns

def get_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    return_data = []
    for i in range(0, len(data), 4):
        return_data.append([string_to_int_list(data[i+j]) for j in range(3)])
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

tests = get_input()

cnt = 0
for case in tests:
    results = run_all_functions(case[0], case[1][1:])
    if [res for res in results.values()].count(tuple(case[2])) >= 3:
        cnt += 1

print(cnt)