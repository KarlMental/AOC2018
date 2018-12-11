
def populated_grid(grid):
	grid = [[((((i+11)*(j+1)+2866)*(i+11)//100)%10)-5 for i in range(300)] for j in range(300)]
	print(grid)

populated_grid()