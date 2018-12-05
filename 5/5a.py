with open('input.txt', 'r') as f:
	data = f.read()
new_data = data
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
print(len(new_data))