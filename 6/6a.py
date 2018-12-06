def get_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    data = [row.split(', ') for row in data]
    data = tuple([tuple([int(a) for a in pair]) for pair in data])
    return data

pairs = get_input()
maximum = max([max(pair) for pair in pairs])
grid = [[None for i in range(maximum+1)] for j in range(maximum+1)]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        best_pair = [[], maximum]
        for ix, pair in enumerate(pairs):
            distance = abs(pair[0]-x)+abs(pair[1]-y)
            if distance < best_pair[1]:
                best_pair[0] = [ix]
                best_pair[1] = distance
            elif distance == best_pair[1]:
                best_pair[0].append(ix)
        grid[y][x] = best_pair

pairs_stats = [[0, False] for i in range(len(pairs))]


for y in range(len(grid)):
    for x in range(len(grid[y])):
        if len(grid[y][x][0]) == 1:
            pairs_stats[grid[y][x][0][0]][0] += 1
        if y in (0, maximum-1) or x in (0, maximum-1):
            pairs_stats[grid[y][x][0][0]][1] = True

largest_area = 0
for pair in pairs_stats:
    if pair[1] is False and pair[0] > largest_area:
        largest_area = pair[0]

print(largest_area)
