import numpy as np

def neighbor(grid, y_pos, x_pos, size):
	return_sum = 0
	for y in range(size):
		return_sum += grid[y_pos+y, x_pos+size-1]
	for x in range(size-1):
		return_sum += grid[y_pos+size-1, x_pos+x]
	return return_sum

def largest_coordinate(grid):
	largest = [0, 0, -90000, 0]
	for y in range(300):
			for x in range(300):
				value = 0
				for size in range(1,301-max(x,y)-1):
					value += neighbor(grid, y, x, size)
					if value > largest[2]:
						largest = [x+1, y+1, value, size]
	return largest

grid = np.array([[((((x+11)*(y+1)+2866)*(x+11)//100)%10)-5 for x in range(300)] for y in range(300)])

print(largest_coordinate(grid))
