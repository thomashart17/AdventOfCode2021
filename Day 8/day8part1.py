# Advent of Code 2021 Day 8 Part 1
# Author: Thomas Hart

def count_digits(file):
    with open(file) as f:
        entries = f.readlines()
    outputs = []
    for entry in entries:
        outputs.append(entry.split('|')[1])
    for i in range(len(outputs)):
        outputs[i] = outputs[i].strip().split(' ')
    count = 0
    for output in outputs:
        for val in output:
            count += len(val) in (2, 3, 4, 7)
    return count

if __name__ == "__main__":
    print(count_digits("input.txt"))