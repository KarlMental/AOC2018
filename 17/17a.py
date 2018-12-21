import re

def get_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    return [[int(a) if a not in 'xy' else a for a in re.findall(r'^\w{1}|\d+', row) ] for row in data]

def draw(instruction, cave, min_x):
    if instruction[0] == 'y':
        for x in range(instruction[2]-min_x, instruction[3]-min_x+1):
            cave[instruction[1]][x] = '#'
    else:
        for y in range(instruction[2], instruction[3]+1):
            cave[y][instruction[1]-min_x] = '#'
    return cave

def print_cave(cave):
    cave_string = '\n'.join([''.join(row) for row in cave])
    print(cave_string)

def get_extreme(variable, instructions):
    max_value = 0
    min_value = 100000
    for instruction in instructions:
        if instruction[0] == variable and instruction[1] > max_value:
            max_value = instruction[1]
        elif instruction[0] == variable and instruction[1] < min_value:
            min_value = instruction[1]
        elif instruction[0] != variable and instruction[3] > max_value:
            max_value = instruction[3]
        elif instruction[0] != variable and instruction[2] < min_value:
            min_value = instruction[3]
    return max_value, min_value

draw_instructions = get_input()
max_x, min_x = get_extreme('x', draw_instructions)
max_y, min_y = get_extreme('y', draw_instructions)
print(min_x, max_x, min_y, max_y)
cave = [['.' for i in range(min_x, max_x+1)] for j in range(max_y+1)]
cave[0][500-min_x] = '+'
for instruction in draw_instructions:
    cave = draw(instruction, cave, min_x)
print_cave(cave)
