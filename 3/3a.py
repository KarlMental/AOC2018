import re

with open('input.txt', 'r') as f:
    data = f.read().split('\n')

def fill(fabric, x_inp, y_inp, x_count, y_count):
	for x, value in enumerate(fabric):
		for y, value in enumerate(fabric[x]):
			if x_inp <= x < x_inp + x_count and y_inp <= y < y_inp + y_count:
				fabric[x][y] += 1
	return fabric

instructions = [[int(x) for x in re.findall(r"(\d+)", row)[1:]] for row in data]

fabric = [[0 for i in range(max([row[1]+row[3]+1 for row in instructions]))] for j in range(max([row[0]+row[2]+1 for row in instructions]))]

for i, instruction in enumerate(instructions):
	fabric = fill(fabric, instruction[0], instruction[1], instruction[2], instruction[3])
	if i == 0:
		print(fabric)
	print(i)

count = 0
for x in fabric:
	for y in x:
		if y > 1:
			count += 1
print(count)