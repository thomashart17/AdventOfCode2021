# Advent of Code 2021 Day 10 Part 2
# Author: Thomas Hart

def incomplete(line):
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    opening = []
    for c in line:
        if c in ('(', '[', '{', '<'):
            opening.append(c)
        else:
            if len(opening) == 0:
                return False
            elif pairs[opening[-1]] == c:
                del(opening[-1])
            else:
                return False
    if len(opening) == 0:
        return False
    closing_needed = []
    for i in range(len(opening) - 1, -1, -1):
        closing_needed.append(pairs[opening[i]])
    return closing_needed

def calc_points(file):
    with open(file) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in lines:
        score = 0
        val = incomplete(line)
        if val != False:
            for c in val:
                score *= 5
                score += points[c]
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

if __name__ == "__main__":
    print(calc_points("input.txt"))