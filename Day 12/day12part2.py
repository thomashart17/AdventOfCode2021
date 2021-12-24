# Advent of Code 2021 Day 12 Part 2
# Author: Thomas Hart

def paths(start, moves, used, used_twice):
    count = 0
    for move in moves[start]:
        twice = used_twice
        used_copy = used.copy()
        if move == "end":
            count += 1
        elif move != "start":
            if move.upper() == move:
                count += paths(move, moves, used_copy, twice)
            elif move not in used:
                used_copy.append(move)
                count += paths(move, moves, used_copy, twice)
            elif (move in used) and (not twice):
                twice = True
                used_copy.append(move)
                count += paths(move, moves, used_copy, twice)
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
    return paths("start", moves, [], False)

if __name__ == "__main__":
    print(count_paths("input.txt"))