# Advent of Code 2021 Day 9 Part 2
# Author: Thomas Hart

def calc_basin(rows, i, j):
    if rows[i][j] == None:
        return 0
    else:
        if rows[i][j] == 9:
            rows[i][j] = None
            return 0
        else:
            total = 1
            rows[i][j] = None
            if i > 0:
                total += calc_basin(rows, i - 1, j)
            if i < len(rows) - 1:
                total += calc_basin(rows, i + 1, j)
            if j > 0:
                total += calc_basin(rows, i, j - 1)
            if j < len(rows[i]) - 1:
                total += calc_basin(rows, i, j + 1)
            return total

def risk_level(file):
    with open(file) as f:
        rows = f.readlines()
    for i in range(len(rows)):
        rows[i] = list(rows[i].strip())
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j] = int(rows[i][j])
    basins = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            basin = calc_basin(rows, i, j)
            if basin > 0:
                basins.append(basin)
    basins.sort()
    return basins[-1]*basins[-2]*basins[-3]

if __name__ == "__main__":
    print(risk_level("input.txt"))