#!/usr/bin/python3

# checks board for available spaces
def check_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O' or board[i][j] == 'X':
                continue
            else:
                available.append(board[i][j])
    return available
