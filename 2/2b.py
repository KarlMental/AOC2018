import itertools

with open('input.txt', 'r') as f:
    data = f.read().split('\n')

for a, b in itertools.combinations(data, 2):
    if a == b:
        continue
    count = 0
    new_string = ''
    for match in zip(a,b):
        if match[0] != match[1]:
            count += 1
        else:
            new_string += match[0]
        if count == 2:
            break
    if count == 1:
        print(a,b)
        print(new_string)