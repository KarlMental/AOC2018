with open('input.txt', 'r') as f:
	data = f.read()

lowest = ['A', 50000]

for letter in range(65, 91):
	new_data = ''.join([x for x in data if ord(x) != letter and ord(x)-32 != letter])
	i = 1
	while True:
		if abs(ord(new_data[i])-ord(new_data[i-1])) != 32:
			if i == len(new_data)-1:
				break
			else:
				i += 1
		else:
			new_data = ''.join(new_data[:i-1])+''.join(new_data[i+1:])
			if i == len(new_data)-1:
				break
			elif i == 1:
				pass
			else:
				i -= 1
	i = 0
	if len(new_data) < lowest[1]:
		lowest = [chr(letter), len(new_data)]
	print(chr(letter))
print(lowest)