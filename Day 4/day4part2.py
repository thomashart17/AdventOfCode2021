# Advent of Code 2021 Day 4 Part 2
# Author: Thomas Hart

from types import TracebackType
from day4part1 import check_win, sum_board

def calc_last_board(file):
    with open(file) as f:
        nums=f.readline().split(',')
        boards = []
        while(f.readline()):
            board = []
            for i in range(5):
                board.append(f.readline().split())
            boards.append(board)
    for n in nums:
        new_boards = []
        for i in range(len(boards)):
            for j in range(5):
                for k in range(5):
                    if int(boards[i][j][k]) == int(n):
                        boards[i][j][k] = False
            if len(boards) == 1 and check_win(boards[0]):
                return sum_board(boards[0])*int(n)
            if not check_win(boards[i]):
                new_boards.append(boards[i])
        boards = new_boards

if __name__ == "__main__":
    print(calc_last_board("input.txt"))