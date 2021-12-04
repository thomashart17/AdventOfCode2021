# Advent of Code 2021 Day 4 Part 1
# Author: Thomas Hart

def check_win(board):
    for i in range(5):
        if board[i] == [False, False, False, False, False]:
            return True
        if (board[0][i] == False) and (board[1][i] == False) and (board[2][i] == False) and (board[3][i] == False) and (board[4][i] == False):
            return True
    return False

def sum_board(board):
    sum = 0
    for row in board:
        for n in row:
            if n:
                sum += int(n)
    return sum

def calc_winner(file):
    with open(file) as f:
        nums=f.readline().split(',')
        boards = []
        while(f.readline()):
            board = []
            for i in range(5):
                board.append(f.readline().split())
            boards.append(board)
    for n in nums:
        for i in range(len(boards)):
            for j in range(5):
                for k in range(5):
                    if int(boards[i][j][k]) == int(n):
                        boards[i][j][k] = False
            if (check_win(boards[i])):
                return sum_board(boards[i])*int(n)

print(calc_winner("input.txt"))