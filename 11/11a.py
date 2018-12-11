
def populated_grid():
	grid = [[((((i+11)*(j+1)+2866)*(i+11)//100)%10)-5 for i in range(300)] for j in range(300)]
	return grid

def get_3x3_grid(grid, x_pos, y_pos):
	return [[grid[y_pos+y][x_pos+x] for x in range(3)] for y in range(3)]

def largest_3x3_coordinate(grid):
	largest = [0, 0, -25]
	for y in range(len(grid)-2):
		for x in range(len(grid[y])-2):
			sub_grid = get_3x3_grid(grid, x, y)
			sub_grid_value = sum([sum([x for x in row]) for row in sub_grid])
			if sub_grid_value > largest[2]:
				largest = [x+1, y+1, sub_grid_value]
	return largest

grid = populated_grid()
print(largest_3x3_coordinate(grid))
