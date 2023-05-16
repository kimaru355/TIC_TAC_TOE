#!/usr/bin/python3

# checks if games is solved
def check_solved(board):
    state = check_solved_horizontal(board)
    if state == 'O':
        return 'user'
    elif state == 'X':
        return 'pc'
    state = check_solved_vertically(board)
    if state == 'O':
        return 'user'
    elif state == 'X':
        return 'pc'
    state = check_solved_diagonal(board)
    if state == 'O':
        return 'user'
    elif state == 'X':
        return 'pc'
    return None


# checks if game is solved vertically
def check_solved_vertically(board):
    user = 'O'
    pc = 'X'
    for i in range(3):
        count = 0
        counts = 0
        for j in range(3):
            if board[j][i] == user:
                count += 1
                if count == 3:
                    return user
            elif board[j][i] == pc:
                counts += 1
                if counts == 3:
                    return pc
    return None


# check if game is solved horizontally
def check_solved_horizontal(board):
    user = 'O'
    pc = 'X'
    for i in range(3):
        count = 0
        counts = 0
        for j in range(3):
            if board[i][j] == user:
                count += 1
                if count == 3:
                    return user
            elif board[i][j] == pc:
                counts += 1
                if counts == 3:
                    return pc
    return None


# checks if solved diagonally
def check_solved_diagonal(board):
    right = []
    left = []
    for i in range(3):
        right.append(board[i][i])
    left.append(board[0][2])
    left.append(board[1][1])
    left.append(board[2][0])
    if right[0] == right[1] == right[2]:
        return right[0]
    if left[0] == left[1] == left[2]:
        return left[0]
    return None
