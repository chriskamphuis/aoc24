from functools import lru_cache
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

@lru_cache
def heads(y, x):
    if grid[(y, x)] == 9:
        return {(y, x)}
    else:
        splits = set()
        for neighbour in neighbours(y, x):
            if grid[neighbour] == grid[(y, x)] + 1:
                splits |= heads(*neighbour)
        return splits

count = 0
for y2, x2, in starts:
    count += len(heads(y2, x2))
print(count)

@lru_cache
def roads(y, x):
    if grid[(y, x)] == 9:
        return 1
    else:
        splits = []
        for neighbour in neighbours(y, x):
            if grid[neighbour] == grid[(y, x)] + 1:
                splits.append(roads(*neighbour))
        return sum(splits)

count = 0
for y2, x2, in starts:
    count += roads(y2, x2)
print(count)
