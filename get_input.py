#!/usr/bin/python3
from random import randrange
# randrange to generate pc values


# generate pc values. Value must be 1-9 and within available spaces
def pc_random():
    while True:
        value = randrange(1, 10)
        if value in available:
            break
    return value


# prompts user to enter value. Value must be 1-9 and within available spaces
def user_random():
    while True:
        value = int(input('Enter a number 1-9: '))
        if 0 < value < 10 and value in available:
            break
    return value
