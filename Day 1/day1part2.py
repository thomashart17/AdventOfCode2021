# Advent of Code Day 1 Part 2
# Author: Thomas Hart

def count_increasing_windows(file):
    with open(file) as f:
        vals = f.readlines()
    count = 0
    prev = int(vals[0]) + int(vals[1]) + int(vals[2])
    for i in range(3, len(vals)):
        val = int(vals[i]) + int(vals[i - 1]) + int(vals[i - 2])
        if val > prev:
            count += 1
        prev = val
    return count

print(count_increasing_windows("input.txt"))