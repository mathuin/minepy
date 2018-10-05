#!/usr/bin/env python3

import argparse
import random


# Check the inputs.
def checkint(string, low, high):
    value = int(string)
    if value < low or value > high:
        msg = "%r is not a valid value" % string
        raise argparse.ArgumentTypeError(msg)
    return value


def typelength(string):
    checkint(string, 3, 30)


def typewidth(string):
    checkint(string, 3, 24)


def typemines(string):
    checkint(string, 5, 95)


parser = argparse.ArgumentParser(description='Minesweeper in Python.')
parser.add_argument('--length', type=typelength, default=15)
parser.add_argument('--width', type=typewidth, default=12)
parser.add_argument('--percent', type=typemines, default=10)
args = parser.parse_args()

gl = args.length
gw = args.width
gp = args.percent

# Build the grid.
grid = [[' '] * gw for i in range(gl)]
safecells = gw*gl
for i in range(gl):
    for j in range(gw):
        if random.randint(0, 100) < gp:
            grid[i][j] = 'X'
            safecells -= 1

for i in range(gl):
    for j in range(gw):
        if grid[i][j] == 'X':
            continue
        mines = 0
        for ni in range(i-1, i+2):
            for nj in range(j-1, j+2):
                if ni >= 0 and ni < gl and nj >= 0 and nj < gw:
                    if grid[ni][nj] == 'X':
                        mines += 1
        if mines > 0:
            grid[i][j] = str(mines)

# Play the game.
def recursivereveal(grid, revealed, ri, rj):
    revealed.append([ri, rj])
    if grid[ri][rj] == ' ':
        for si in range(ri-1, ri+2):
            for sj in range(rj-1, rj+2):
                if si >= 0 and si < gl and sj >= 0 and sj < gw:
                    if [si, sj] not in revealed:
                        recursivereveal(grid, revealed, si, sj)


revealed = []
while True:
    for i in range(gl):
        for j in range(gw):
            print(grid[i][j] if [i, j] in revealed else '+', end='')
        print()
    while True:
        try:
            coordinput = input("Next cell? ")
            coords = coordinput.split()
            ci = int(coords[0])
            cj = int(coords[1])
            recursivereveal(grid, revealed, ci, cj)
            break
        except Exception:
            print("Invalid input: need two integers!")
    if grid[ci][cj] == 'X':
        print("Boom!  Game over!")
        break
    if len(revealed) == safecells:
        print("Congratulations!")
        break
