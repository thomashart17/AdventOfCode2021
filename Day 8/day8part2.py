# Advent of Code 2021 Day 8 Part 2
# Author: Thomas Hart

def sum_outputs(file):
    with open(file) as f:
        entries = f.readlines()
    nums = []
    outputs = []
    for entry in entries:
        nums.append(entry.split('|')[0])
        outputs.append(entry.split('|')[1])
    for i in range(len(nums)):
        nums[i] = nums[i].strip().split(' ')
        outputs[i] = outputs[i].strip().split(' ')
        total = 0
    for i in range(len(nums)):
        current_vals = {}
        for j in range(10):
            if len(nums[i][j]) == 2:
                current_vals.update({1:list(nums[i][j])})
                current_vals[1].sort()
                del(nums[i][j])
                break
        for j in range(9):
            if len(nums[i][j]) == 3:
                current_vals.update({7:list(nums[i][j])})
                current_vals[7].sort()
                del(nums[i][j])
                break
        for j in range(8):
            if len(nums[i][j]) == 4:
                current_vals.update({4:list(nums[i][j])})
                current_vals[4].sort()
                del(nums[i][j])
                break
        for j in range(7):
            if len(nums[i][j]) == 7:
                current_vals.update({8:list(nums[i][j])})
                current_vals[8].sort()
                del(nums[i][j])
                break
        for j in range(6):
            if len(nums[i][j]) == 5:
                status = True
                for n in current_vals[1]:
                    if n not in nums[i][j]:
                        status = False
                        break
                if status:
                    current_vals.update({3:list(nums[i][j])})
                    current_vals[3].sort()
                    del(nums[i][j])
                    break
        for j in range(5):
            if len(nums[i][j]) == 6:
                status = True
                for n in current_vals[3]:
                    if n not in nums[i][j]:
                        status = False
                        break
                if status:
                    current_vals.update({9:list(nums[i][j])})
                    current_vals[9].sort()
                    del(nums[i][j])
                    break
        for j in range(4):
            if len(nums[i][j]) == 6:
                status = True
                for n in current_vals[1]:
                    if n not in nums[i][j]:
                        status = False
                        break
                if status:
                    current_vals.update({0:list(nums[i][j])})
                    current_vals[0].sort()
                    del(nums[i][j])
                    break
        for j in range(3):
            if len(nums[i][j]) == 6:
                current_vals.update({6:list(nums[i][j])})
                current_vals[6].sort()
                del(nums[i][j])
                break
        for j in range(2):
            count = 0
            status = True
            for n in current_vals[6]:
                if n not in nums[i][j]:
                    count += 1
                if count > 1:
                    status = False
                    break
            if status:
                current_vals.update({5:list(nums[i][j])})
                current_vals[5].sort()
                del(nums[i][j])
                break
        current_vals.update({2:list(nums[i][0])})
        current_vals[2].sort()
        value = 0
        power = 1000
        for output in outputs[i]:
            current = list(output)
            current.sort()
            for key in current_vals:
                if current == current_vals[key]:
                    value += power*key
                    power //= 10
                    break
        total += value
        print(current_vals)
    return total

if __name__ == "__main__":
    print(sum_outputs("input.txt"))