from collections import defaultdict

grid = defaultdict(int)
starts = set()
with open('../data/10.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            grid[(y, x)] = int(char)
            if char == '0':
                starts.add((y, x))

neighbours = lambda y, x : [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]

def heads(y, x):
    if grid[(y, x)] == 9:
        return {(y, x)}, 1
    else:
        splits = set()
        score = 0
        for neighbour in neighbours(y, x):
            if grid[neighbour] == grid[(y, x)] + 1:
                subset, subscore = heads(*neighbour)
                splits |= subset
                score += subscore
        return splits, score

score_a = score_b = 0
for y2, x2, in starts:
    subset, score = heads(y2, x2)
    score_a += len(subset)
    score_b += score
print(score_a)
print(score_b)