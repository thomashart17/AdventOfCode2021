# Advent of Code 2021 Day 3 Part 1
# Author: Thomas Hart

def calc_gamma_epsilon(file):
    with open(file) as f:
        vals = f.readlines()
    bit_count = []
    for i in range(len(vals[0]) - 1):
        bit_count.append(0)
    for val in vals:
        for i in range(len(val) - 1):
            bit_count[i] += int(val[i])
    gamma = ""
    epsilon = ""
    for bit in bit_count:
        if bit > len(vals)/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma, epsilon        

gamma, epsilon = calc_gamma_epsilon("input.txt")
print(gamma*epsilon)