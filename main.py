#!/usr/bin/python3

from print_board import print_board
from add_board import add_board
from check_available import check_board
from get_input import pc_random, user_random
from check_solved import check_solved

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]
available = []

# main function
while True:
    available = check_board(board)
    if len(available) == 0:
        print("It's a draw")
        break
    values = pc_random(available)
    board = add_board(board, 'pc', values)
    print_board(board)
    status = check_solved(board)
    if status == 'pc':
        print('You lost')
        break
    elif status == 'user':
        print("You won")
        break
    available.clear()
    available = check_board(board)
    if len(available) == 0:
        print("It's a draw")
        break
    values = user_random(available)
    board = add_board(board, 'user', values)
    status = check_solved(board)
    if status == 'pc':
        print('You lost')
        break
    elif status == 'user':
        print_board(board)
        print("You won")
        break
    available.clear()
