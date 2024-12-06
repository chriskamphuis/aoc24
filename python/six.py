from itertools import cycle

obstructions = set()
guard = tuple()
directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
x_min, x_max, y_min, y_max = 0, 0, 0, 0
with open('../data/6.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            match char:
                case '.':
                    continue
                case '#':
                    obstructions.add((y, x))
                case '^':
                    guard_start = guard = (y, x)
    x_max = x+1
    y_max = y+1

direction = next(directions)
visited = set()
visited.add(guard_start)

next_loc = lambda g, d: (g[0] + d[0], g[1] + d[1])
guard = guard_start
while True:
    new_loc = next_loc(guard, direction)
    if y_min > new_loc[0] or y_max < new_loc[0] or x_min > new_loc[1] or x_max < new_loc[1]:
        break
    elif new_loc in obstructions:
        direction = next(directions)
    else:
        visited.add(new_loc)
        guard = new_loc

print(len(visited))
candidates = visited
candidates.remove(guard_start)

def in_loop(_guard, _directions, _obstructions):
    _visited = set()
    dirs = _directions
    _direction = next(dirs)
    _visited.add((_guard, _direction))
    while True:
        new_loc = next_loc(_guard, _direction)
        if (new_loc, _direction) in _visited:
            return True
        elif y_min > new_loc[0] or y_max < new_loc[0] or x_min > new_loc[1] or x_max < new_loc[1]:
            return False
        elif new_loc in _obstructions:
            _direction = next(dirs)
        else:
            _visited.add((new_loc, _direction))
            _guard = new_loc

count = 0
for y, x in candidates:
    _g = guard_start
    _directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    count += int(in_loop(_g, _directions, obstructions | {(y, x)}))
print(count)
