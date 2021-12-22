# Advent of Code 2021 Day 14 Part 2
# Author: Thomas Hart

def calc_most_least_common(file):
    with open(file) as f:
        polymer = f.readline().strip()
        f.readline()
        insertions = f.readlines()
    pairs = {}
    keys = []
    for pair in insertions:
        formatted_pair = pair.strip().replace(' ', '').split("->")
        pairs.update({formatted_pair[0]: [formatted_pair[0][0] + formatted_pair[1], formatted_pair[1] + formatted_pair[0][1]]})
        keys.append(formatted_pair[0])
    transformation = []
    for i in range(len(pairs)):
        transformation.append([0]*len(pairs))
    for i in range(len(pairs)):
        for j in range(len(keys)):
            if keys[j] in pairs[keys[i]]:
                transformation[j][i] += 1
    for row in transformation:
        print(row)
    og_transformation = transformation.copy()
    for i in range(39):
        new_transformation = []
        for j in range(len(pairs)):
            new_transformation.append([0]*len(pairs))
        for j in range(len(transformation)):
            for k in range(len(transformation)):
                new_val = 0
                for l in range(len(transformation)):
                    new_val += transformation[j][l]*og_transformation[l][k]
                new_transformation[j][k] = new_val
        transformation = new_transformation
    start_state = [0]*len(keys)
    for i in range(len(polymer) - 1):
        start_state[keys.index(polymer[i:i + 2])] += 1
    final_state = [0]*len(start_state)
    for i in range(len(transformation)):
        for j in range(len(transformation)):
            final_state[i] += transformation[i][j]*start_state[j]
    counts = {}
    for i in range(len(final_state)):
        print(keys[i])
        if keys[i][0] in counts:
            print("test")
            print(final_state[i])
            print(counts[keys[i][0]] + final_state[i])
            counts[keys[i][0]] += final_state[i]
        else:
            counts[keys[i][0]] = final_state[i]
        print(counts)
    counts[polymer[0]] += 1
    counts[polymer[-1]] += 1
    print(counts)
    least = 0
    most = 0
    for c in counts:
        if (least == 0) and (most == 0):
            least = counts[c]
            most = counts[c]
        else:
            least = min(least, counts[c])
            most = max(most, counts[c])
    print((most - least)/2)
    print(start_state)
    print(final_state)
    return most - least

if __name__ == "__main__":
    print(calc_most_least_common("input.txt"))