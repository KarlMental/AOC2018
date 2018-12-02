with open('input.txt', 'r') as f:
    data = f.read().split('\n')

freq = 0

for change in data:
    freq += int(change)

print(freq)