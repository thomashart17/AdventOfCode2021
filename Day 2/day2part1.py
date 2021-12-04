# Advent of Code 2021 Day 2 Part 1
# Author: Thomas Hart

def calc_position(file):
    commands = []
    with open(file) as f:
        for line in f:
            commands.append(line.split())
    x, y = 0, 0
    for command in commands:
        if command[0] == "forward":
            x += int(command[1])
        elif command[0] == "down":
            y += int(command[1])
        elif command[0] == "up":
            y -= int(command[1])
    return x, y

if __name__ == "__main__":
    x, y = calc_position("input.txt")
    print(x*y)