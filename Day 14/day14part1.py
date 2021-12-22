# Advent of Code 2021 Day 14 Part 1
# Author: Thomas Hart

def calc_most_least_common(file):
    with open(file) as f:
        polymer = f.readline().strip()
        f.readline()
        insertions = f.readlines()
    pairs = {}
    for pair in insertions:
        formatted_pair = pair.strip().replace(' ', '').split("->")
        pairs.update({formatted_pair[0]: formatted_pair[1]})
    for i in range(10):
        new_polymer = ""
        for j in range(len(polymer) - 1):
            new_polymer += polymer[j] + pairs[polymer[j:j + 2]]
        new_polymer += polymer[-1]
        polymer = new_polymer
    counts = {}
    for c in polymer:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    least = 0
    most = 0
    for c in counts:
        if (least == 0) and (most == 0):
            least = counts[c]
            most = counts[c]
        else:
            least = min(least, counts[c])
            most = max(most, counts[c])
    return most - least

if __name__ == "__main__":
    print(calc_most_least_common("input.txt"))