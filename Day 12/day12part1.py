# Advent of Code 2021 Day 12 Part 1
# Author: Thomas Hart

def paths(start, moves, used):
    count = 0
    for move in moves[start]:
        used_copy = used.copy()
        if move == "end":
            count += 1
        elif move != "start":
            if move.upper() == move:
                count += paths(move, moves, used_copy)
            elif move not in used:
                used_copy.append(move)
                count += paths(move, moves, used_copy)
    return count

def count_paths(file):
    with open(file) as f:
        rules = f.readlines()
    for i in range(len(rules)):
        rules[i] = rules[i].strip().split('-')
    moves = {}
    for rule in rules:
        if rule[0] in moves:
            moves[rule[0]].append(rule[1])
        else:
            moves[rule[0]] = [rule[1]]
        if rule[1] in moves:
            moves[rule[1]].append(rule[0])
        else:
            moves[rule[1]] = [rule[0]]
    return paths("start", moves, [])

if __name__ == "__main__":
    print(count_paths("input.txt"))