# Advent of Code 2021 Day 6 Part 2
# Author: Thomas Hart

def count_lanternfish(file):
    with open(file) as f:
        fish_input = f.readline().split(',')
    fish_list = [int(x) for x in fish_input]
    ages = [0]*9
    for fish in fish_list:
        ages[fish] += 1
    for i in range(256):
        new_fish = ages[0]
        for j in range(8):
            ages[j] = ages[j+1]
        ages[8] = new_fish
        ages[6] += new_fish
    return sum(ages)

if __name__ == "__main__":
    print(count_lanternfish("input.txt"))