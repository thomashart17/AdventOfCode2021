# Advent of Code 2021 Day 13 Part 1
# Author: Thomas Hart

def fold_info(fold):
    fold = fold.split('=')
    return fold[0][-1], int(fold[1])

def count_dots(file):
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
    new_grid = []
    if folds[0][0] == 'y':
        for i in range(folds[0][1]):
            new_grid.append([0]*len(grid[0]))
        for i in range(len(new_grid)):
            for j in range(len(new_grid[i])):
                new_grid[i][j] += grid[i][j] + grid[len(grid) - i - 1][j]
    elif folds[0][0] == 'x':
        for i in range(len(grid)):
            new_grid.append([0]*folds[0][1])
        for i in range(len(new_grid)):
            for j in range(len(new_grid[i])):
                new_grid[i][j] += grid[i][j] + grid[i][len(grid[i]) - j - 1]
    grid = new_grid
    dots = 0
    for row in grid:
        for num in row:
            dots += 1 if num > 0 else 0
    return dots

if __name__ == "__main__":
    print(count_dots("input.txt"))