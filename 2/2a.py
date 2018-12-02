import collections

with open('input.txt', 'r') as f:
    data = f.read().split('\n')

counts = [0,0]

for line in data:
    stop = [False,False]
    for key, value in collections.Counter(line).items():
        if value == 2 and stop[0] == False:
            counts[0] += 1
            stop[0] = True
        if value == 3 and stop[1] == False:
            counts[1] += 1
            stop[1] = True
        if stop == [True, True]:
            break

print(counts[0]*counts[1])