# Advent of Code Day 10 Part 1
# Author: Thomas Hart

def corrupted(line):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    opening = []
    for c in line:
        if c in ('(', '[', '{', '<'):
            opening.append(c)
        else:
            if len(opening) == 0:
                return c
            elif pairs[opening[-1]] == c:
                del(opening[-1])
            else:
                return c
    return False

def calc_points(file):
    with open(file) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        val = corrupted(line)
        if val != False:
            score += points[val]
    return score

if __name__ == "__main__":
    print(calc_points("input.txt"))