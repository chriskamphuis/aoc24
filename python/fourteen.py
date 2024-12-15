from functools import reduce
from re import findall

PATTERN = r'p\=(\d+),(\d+) v=(-?\d+),(-?\d+)'
WIDTH, HEIGHT = 101, 103
IT = 100
robots = []
with open('../data/14.txt') as f:
    for line in f.readlines():
        robots.append([int(e) for e in findall(PATTERN, line)[0]])

counts = [0, 0, 0, 0]
for x, y, dx, dy in robots:
    new_x, new_y = ((x + dx * IT) % WIDTH, (y + dy * IT) % HEIGHT)
    if new_x < WIDTH // 2 and new_y < HEIGHT // 2:
        counts[0] += 1
    if new_x > WIDTH // 2 and new_y < HEIGHT // 2:
        counts[1] += 1
    if new_x < WIDTH // 2 and new_y > HEIGHT // 2:
        counts[2] += 1
    if new_x > WIDTH // 2 and new_y > HEIGHT // 2:
        counts[3] += 1
print(reduce(lambda x, y: x * y, counts))

def locations(starts, iteration):
    _locations = []
    for x, y, dx, dy in starts:
        _locations.append(((x + dx * iteration) % WIDTH, (y + dy * iteration) % HEIGHT))
    return _locations

neighbours = lambda x, y: [((x+1)%WIDTH, y), (x, (y+1)%HEIGHT), ((x-1)%WIDTH, y), (x, (y-1)%HEIGHT)]

def clustered(locations):
    locs = set(locations)
    total = len(locs)
    c = 0
    for loc in locs:
        if any(n in locs for n in neighbours(*loc)):
            c+=1
    return c > total // 2

i = 0
while True:
    if clustered(locations(robots, i)):
        break
    else:
        i += 1
print(i)