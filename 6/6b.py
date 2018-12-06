def get_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    data = [row.split(', ') for row in data]
    data = tuple([tuple([int(a) for a in pair]) for pair in data])
    return data

pairs = get_input()
maximum = max([max(pair) for pair in pairs])
grid = [[0 for i in range(maximum+1)] for j in range(maximum+1)]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        distance_tot = 0
        for ix, pair in enumerate(pairs):
            distance_tot += abs(pair[0]-x)+abs(pair[1]-y)
        if distance_tot < 10000:
            if y in (0, maximum-1) or x in (0, maximum-1):
                print('gonna need bigger grid')
            grid[y][x] = 1

print(sum([sum(row) for row in grid]))