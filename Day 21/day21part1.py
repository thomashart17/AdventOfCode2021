# Advent of Code 2021 Day 21 Part 1
# Author: Thomas Hart

def calc_score(file):
    with open(file) as f:
        p1 = int(f.readline().strip()[-1])
        p2 = int(f.readline().strip()[-1])
    roll = 0
    turn = True
    score1, score2 = 0, 0
    while (score1 < 1000) and (score2 < 1000):
        if turn:
            p1 += 3*roll + 1 + 2 + 3
            p1 %= 10
            score1 += p1 if p1 != 0 else 10
        else:
            p2 += 3*roll + 1 + 2 + 3
            p2 %= 10
            score2 += p2 if p2 != 0 else 10
        roll += 3
        turn = not turn
    return min(score1, score2)*roll

if __name__ == "__main__":
    print(calc_score("input.txt"))