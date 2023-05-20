#!/usr/bin/python3

# checks board for available spaces
def check_board(board):
    tmp = []
    available = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O' or board[i][j] == 'X':
                continue
            else:
                tmp.append(board[i][j])
    for i in tmp:
        available.append(int(i))
    return available
