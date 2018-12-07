with open('input.txt', 'r') as f:
    data = f.read().split('\n')

def find_available(instructions, alphabet):
	for letter in alphabet:
		if letter not in [pair[1] for pair in instructions]:
			return letter
	else:
		return None

alphabet = ''.join([chr(x) for x in range(65,91)])

final_order = ''
instructions = []

for row in data:
	instructions.append((row[5], row[-12]))

seconds = 0
queue = [['', 0] for i in range(5)]

while True:
	for ix, worker in enumerate(queue):
		if worker[1] == 0:
			next_step = find_available(instructions, alphabet)
			if next_step:
				alphabet = ''.join([a for a in alphabet	if a != next_step])
				queue[ix] = [next_step, ord(next_step)-5]
			else:
				queue[ix][0] = ''
		else:
			queue[ix][1] -= 1
	for ix, worker in enumerate(queue):
		if worker[1] == 0:
			instructions = [instruction for instruction	in instructions	if instruction[0] != worker[0]]
	if ''.join([worker[0] for worker in queue]) == '':
		break
	print('second: {}, workers: {}, {}, {}, {}, {}'.format(seconds, queue[0], queue[1], queue[2], queue[3], queue[4]))
	seconds	+= 1 