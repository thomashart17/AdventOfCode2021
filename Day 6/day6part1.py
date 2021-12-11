# Advent of Code 2021 Day 6 Part 1
# Author: Thomas Hart

def count_lanternfish(file):
    with open(file) as f:
        fish_input = f.readline().split(',')
    fish = [int(x) for x in fish_input]
    for i in range(80):
        new_fish = 0
        for j in range(len(fish)):
            if fish[j] == 0:
                new_fish += 1
                fish[j] = 6
            else:
                fish[j] -= 1
        for j in range(new_fish):
            fish.append(8)
    return len(fish)

if __name__ == "__main__":
    print(count_lanternfish("input.txt"))