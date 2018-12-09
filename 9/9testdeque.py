from collections import deque
import sys

def lets(elf_count, rounds):
    d = deque([0])
    elves = [0 for i in range(elf_count)]
    for i in range(1, rounds+1):
        d, elves = play(i, d, elves)
    print(max(elves))

def play(turn, d, elves):
    if turn%23 !=0:
        d.rotate(-1)
        d.append(turn)
    else:
        d.rotate(7)
        elves[(turn-1)%len(elves)] += turn + d.pop()
        d.rotate(-1)
    return d, elves

lets(int(sys.argv[1]), int(sys.argv[2]))
