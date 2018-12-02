with open('input.txt', 'r') as f:
    data = f.read().split('\n')

freq = 0
freq_list = [0]

while True:
    for change in data:
        freq += int(change)
        if freq not in freq_list:
            freq_list.append(freq)
        else:
            print(freq)
            break
    else:
        continue
    break
