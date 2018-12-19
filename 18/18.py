from itertools import product
import copy

def get_input():
    with open('input.txt', 'r') as f:
        return [[a for a in row] for row in f.read().split('\n')]

def return_neighbors(matrix, x, y):
    temp_list = []
    for c in product(*(range(n-1, n+2) for n in (y, x))):
        if c != (y, x) and all(0 <= n < len(matrix) for n in c):
            temp_list.append(c)
    return temp_list

def morph(matrix, neighbors):
    return_matrix = copy.deepcopy(matrix)
    for y, row in enumerate(matrix):
        for x, cell in enumerate(matrix[y]):
            neighbor_list = []
            for neighbor in neighbors[(x,y)]:
                neighbor_list.append(matrix[neighbor[0]][neighbor[1]])
            if cell == '.':
                if neighbor_list.count('|') >= 3:
                    return_matrix[y][x] = '|'
            elif cell == '|':
                if neighbor_list.count('#') >= 3:
                    return_matrix[y][x] = '#'
            elif cell == '#':
                if neighbor_list.count('#') >= 1 and neighbor_list.count('|') >= 1:
                    return_matrix[y][x] = '#'
                else:
                    return_matrix[y][x] = '.'
    return return_matrix

def print_field(matrix):
    print('\n'.join([''.join([cell for cell in row]) for row in matrix]))

def main(minutes):
    field = get_input()
    neighbors = {}
    for y, row in enumerate(field):
        for x, cell in enumerate(field[y]):
            neighbors[(x,y)] = return_neighbors(field, x, y)
    for i in range(1, minutes+1):
        #print_field(field)
        field = morph(field, neighbors)
        field_flat = [cell for row in field for cell in row]
        trees = field_flat.count('|')
        lumberyards = field_flat.count('#')
        #print(trees, lumberyards)
        print(i, trees*lumberyards)

main(int(10e9))