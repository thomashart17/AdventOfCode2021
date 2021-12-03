# Advent of Code 2021 Day 3 Part 2
# Author: Thomas Hart

def calc_oxygen_co2(file):
    with open(file) as f:
        vals = f.readlines()
    oxygen = vals
    co2 = vals
    for i in range(len(vals[0]) - 1):
        bit_count = 0
        for val in oxygen:
            bit_count += int(val[i])
        status = bit_count >= len(oxygen)/2
        new_oxygen = []
        for val in oxygen:
            if int(val[i]) == status:
                new_oxygen.append(val)
        oxygen = new_oxygen
        if len(oxygen) == 1:
            break
    for i in range(len(vals[0]) - 1):
        bit_count = 0
        for val in co2:
            bit_count += int(val[i])
        status = bit_count >= len(co2)/2
        new_co2 = []
        for val in co2:
            if int(val[i]) != status:
                new_co2.append(val)
        co2 = new_co2
        if len(co2) == 1:
            break
    return int(oxygen[0], 2), int(co2[0], 2)

oxygen, co2 = calc_oxygen_co2("input.txt")
print(oxygen*co2)