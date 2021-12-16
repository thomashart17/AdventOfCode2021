# Advent of Code 2021 Day 9 Part 1
# Author: Thomas Hart

def risk_level(file):
    with open(file) as f:
        rows = f.readlines()
    for i in range(len(rows)):
        rows[i] = list(rows[i].strip())
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j] = int(rows[i][j])
    risk = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            status = True
            if (i - 1 >= 0):
                status = rows[i - 1][j] > rows[i][j] and status
            if (i + 1 < len(rows)):
                status = rows[i + 1][j] > rows[i][j] and status
            if (j - 1 >= 0):
                status = rows[i][j - 1] > rows[i][j] and status
            if (j + 1 < len(rows[i])):
                status = rows[i][j + 1] > rows[i][j] and status
            if status:
                risk += 1 + rows[i][j]
    return risk

if __name__ == "__main__":
    print(risk_level("input.txt"))