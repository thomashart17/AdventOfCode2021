# Advent of Code 2021 Day 11 Part 2
# Author: Thomas Hart

def flash(grid, i, j):
    flashes = 1
    grid[i][j] = False
    for k in range(-1, 2):
        for l in range(-1, 2):
            if (i + k >= 0) and (i + k < len(grid)) and (j + l >= 0) and (j + l < len(grid[i])):
                if grid[i + k][j + l] != False:
                    grid[i + k][j + l] += 1
                if grid[i + k][j + l] > 9:
                    flashes += flash(grid, i + k, j + l)
    return flashes

def calc_flashes(file):
    with open(file) as f:
        grid = f.readlines()
    for i in range(len(grid)):
        grid[i] = grid[i].strip()
        grid[i] = [c for c in grid[i]]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = int(grid[i][j])
    n = 1
    while (True):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] != False) and (grid[i][j] > 9):
                    if flash(grid, i, j) == 100:
                        return n
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == False:
                    grid[i][j] = 0
        n += 1

if __name__ == "__main__":
    print(calc_flashes("input.txt"))