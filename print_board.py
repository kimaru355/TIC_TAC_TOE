#!/usr/bin/python3

# prints the board. Accepts board as argument to reflect changes
def print_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
