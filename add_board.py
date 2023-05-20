#!/usr/bin/python3

# add value to board. Accepts two arguments and adds O for user and X for pc
# row and column convert value to place correctly
def add_board(board, player, value):
    row = int(value / 3)
    column = int(value % 3)
    if column == 0:
        row -= 1
        column = 3
    column -= 1
    if player == 'pc':
        board[row][column] = 'X'
    elif player == 'user':
        board[row][column] = 'O'
    return board
