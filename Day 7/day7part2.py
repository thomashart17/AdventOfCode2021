# Advent of Code 2021 Day 7 Part 2
# Author: Thomas Hart

import sys

def summation(n):
    return (n + 1)*n/2

def calc_fuel(file):
    with open(file) as f:
        positions_input = f.readline().split(',')
    positions = [int(x) for x in positions_input]
    locations = [0]*(max(positions) + 1)
    for position in positions:
        locations[position] += 1
    min_fuel = sys.float_info.max
    for i in range(len(locations)):
        current = 0
        for j in range(len(locations)):
            current += int(summation(abs(j - i))*locations[j])
        min_fuel = min(min_fuel, current)
    return min_fuel

if __name__ == "__main__":
    print(calc_fuel("input.txt"))