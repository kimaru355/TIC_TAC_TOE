#!/usr/bin/python3

boards = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]
available = []

# main function
while True:
    available = check_board(boards)
    if len(available) == 0:
        print("It's a draw")
        break
    values = pc_random()
    add_board('pc', values)
    print_board(boards)
    status = check_solved(boards)
    if status == 'pc':
        print('You lost')
        break
    elif status == 'user':
        print("You won")
        break
    available.clear()
    available = check_board(boards)
    if len(available) == 0:
        print("It's a draw")
        break
    values = user_random()
    add_board('user', values)
    status = check_solved(boards)
    if status == 'pc':
        print('You lost')
        break
    elif status == 'user':
        print_board(boards)
        print("You won")
        break
    available.clear()
