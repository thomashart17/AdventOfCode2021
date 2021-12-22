# Advent of Code 2021 Day 13 Part 2
# Author: Thomas Hart

from day13part1 import fold_info

def decode(file):
    with open(file) as f:
        coords = []
        while True:
            line = f.readline()
            if line != '\n':
                coords.append(line.strip().split(','))
                continue
            else:
                break
        for i in range(len(coords)):
            coords[i][0], coords[i][1] = int(coords[i][0]), int(coords[i][1])
        folds = f.readlines()
        for i in range(len(folds)):
            folds[i] = folds[i].strip()
    grid = []
    for i in range(895):
        grid.append([0]*1311)
    for coord in coords:
        grid[coord[1]][coord[0]] += 1
    for i in range(len(folds)):
        folds[i] = list(fold_info(folds[i]))
    for fold in folds:
        new_grid = []
        if fold[0] == 'y':
            for i in range(fold[1]):
                new_grid.append([0]*len(grid[0]))
            for i in range(len(new_grid)):
                for j in range(len(new_grid[i])):
                    new_grid[i][j] += (grid[i][j] == 1) or (grid[len(grid) - i - 1][j] == 1)
        elif fold[0] == 'x':
            for i in range(len(grid)):
                new_grid.append([0]*fold[1])
            for i in range(len(new_grid)):
                for j in range(len(new_grid[i])):
                    new_grid[i][j] += (grid[i][j] == 1) or (grid[i][len(grid[i]) - j - 1] == 1)
        grid = new_grid
    for row in grid:
        print(row)

if __name__ == "__main__":
    decode("input.txt")