# Advent of Code 2021 Day 5 Part 1
# Author: Thomas Hart

def horizontal(y1, y2):
    return y1 == y2

def vertical(x1, x2):
    return x1 == x2

def calc_points(file):
    with open(file) as f:
        vals = []
        for line in f:
            vals.append(line.split("->"))
        for i in range(len(vals)):
            vals[i] = vals[i][0].strip().split(',') + vals[i][1].strip().replace('\n', '').split(',')
    grid = []
    for i in range(1000):
        grid.append([0]*1000)
    for val in vals:
        if horizontal(val[1], val[3]):
            for i in range(min(int(val[0]), int(val[2])), max(int(val[0]), int(val[2])) + 1):
                grid[int(val[1])][i] += 1
        elif vertical(val[0], val[2]):
            for i in range(min(int(val[1]), int(val[3])), max(int(val[1]), int(val[3])) + 1):
                grid[i][int(val[0])] += 1
    count = 0
    for line in grid:
        for val in line:
            count += val >= 2
    return count


if __name__ == "__main__":
    print(calc_points("input.txt"))