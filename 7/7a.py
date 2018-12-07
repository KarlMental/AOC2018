with open('input.txt', 'r') as f:
    data = f.read().split('\n')

alphabet = ''.join([chr(x) for x in range(65,91)])

final_order = ''
instructions = []

for row in data:
	instructions.append((row[5], row[-12]))

while True:
	for letter in alphabet:
		if letter not in [pair[1] for pair in instructions]:
			letter_to_run = letter
			break
	instructions = [instruction for instruction	in instructions	if instruction[0] != letter_to_run]
	alphabet = ''.join([a for a in alphabet	if a != letter_to_run])
	print(letter_to_run)
	final_order = final_order + ''.join(letter_to_run)
	if len(instructions) == 0:
		break
final_order = final_order + alphabet 
print(final_order)

