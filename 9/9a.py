def play(turn, position, board):
    if turn%23 != 0:
        if position >= len(board)-1:
            position = position - len(board) + 2
        else:
            position = position + 2
        board = board[:position] + [turn] + board[position:]
        points = 0
    else:
        position = position - 7
        points = turn + board[position]

        if position == -1:
            board = board[:-1]
            position = 0
        elif position < 0:
            board = board[:position] + board[position+1:]
            position = len(board) + position + 1
        else:
            board = board[:position] + board[position+1:]
        
    return position, board, points

position = 0
board = [0]
elves = [0 for i in range(428)]
for turn in range(1, 72062):
    return_values = play(turn, position, board)
    position, board = return_values[0], return_values[1]
    elves[(turn-1)%(len(elves))] += return_values[2]
    if turn % 72061 == 0:
        max_elf = elves.index(max(elves))
        print('{}, max: {},  {}'.format(turn, elves.index(max(elves)), max(elves)))
