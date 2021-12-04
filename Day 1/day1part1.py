# Advent of Code 2021 Day 1 Part 1
# Author: Thomas Hart

def count_increasing(file):
    with open(file) as f:
        vals = f.readlines()
    count = 0
    for i in range(1, len(vals)):
        if int(vals[i]) > int(vals[i - 1]):
            count += 1
    return count

if __name__ == "__main__":
    print(count_increasing("input.txt"))