from collections import deque

def get_input():
	with open('input.txt', 'r') as f:
	    data = f.read().split('\n')

	initial_state = deque([True if char == '#' else False for char in data[0].split(' ')[2]])

	new_data = [[True if char == '#' else False if char == '.' else 'lol' for char in row] for row in data[2:]]
	plant_map = {tuple(row[:5]) for row in new_data if row[-1]}
	return plant_map, initial_state

def strip_state(state, offset):
	while True:
		if state[-1] is False:
			state.pop()
		elif state[0] is False:
			state.popleft()
			offset -= 1
		else:
			break
	return state, offset

def pad_state(state, offset):
	padding = [False for i in range(5)]
	state.extend(padding)
	state.extendleft(padding)
	return state, offset + 5

def change_state(state, plant_map, offset):
	state = list(state)
	new_state = []
	for i in range(2,len(state)-2):
		if tuple(state[i-2:i+3]) in plant_map:
			new_state.append(True)
		else:
			new_state.append(False)
	return deque(new_state), offset - 2


def run_generations(number):
	plant_map, state = get_input()
	offset = 0
	original_sum = sum([i-offset if value else 0 for i, value in enumerate(state)])
	steady_state = 0
	latest_diff = 0
	for i in range(1,number+1):
		earlier_sum = sum([i-offset if value else 0 for i, value in enumerate(state)])
		earlier_diff = latest_diff
		state, offset = strip_state(state, offset)
		state, offset = pad_state(state, offset)
		state, offset = change_state(state, plant_map, offset)
		current_sum = sum([i-offset if value else 0 for i, value in enumerate(state)])
		latest_diff = current_sum - earlier_sum 
		if earlier_diff == latest_diff:
			steady_state += 1
		else:
			steady_state = 0
		if steady_state == 100:
			current_sum += (number-i)*latest_diff
			break

		print('Round: {}, Sum: {}, Diff: {}'.format(i, current_sum, latest_diff))
	return current_sum

print(run_generations(50000000000))
