import heapq

maze = set()
end = None
with open('../data/16e.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            match char:
                case '#':
                    pass
                case '.':
                    maze.add((x, y))
                case 'S':
                    maze.add((x, y))
                    start = (x, y)
                case 'E':
                    maze.add((x, y))
                    end = (x, y)

orthogonal = lambda _x, _y : {(-_y, _x), (_y, _x), (_y, -_x), (-_y, -_x)}
step = lambda _x, _y, _dx, _dy: (_x + _dx, _y + _dy)

shortest_paths = dict()
to_consider = []
heapq.heappush(to_consider, (0, start, (1, 0), set()))
while len(to_consider) > 0:
    cost, loc, direction, seen = heapq.heappop(to_consider)
    if (loc, direction) in shortest_paths:
        old_cost, old_seen = shortest_paths[(loc, direction)]
        if old_cost == cost:
            shortest_paths[(loc, direction)] = (cost, seen | old_seen | {(loc, direction)})
        continue
    shortest_paths[(loc, direction)] = cost, seen
    if step(*loc, *direction) in maze and (step(*loc, *direction), direction) not in shortest_paths:
        heapq.heappush(to_consider, (cost+1, step(*loc, *direction), direction, seen | {(loc, direction)}))
    for turn in orthogonal(*direction):
        if step(*loc, *turn) in maze and (step(*loc, *turn), turn) not in shortest_paths :
            heapq.heappush(to_consider, (cost+1000, loc, turn, seen))

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
minimum, locations = min([shortest_paths[(end, direction)] for direction in directions])
print(minimum)

while True:
    all_seen = [loc for loc in locations]
    for loc in all_seen:
        for l in shortest_paths[loc][1]:
            locations.add(l)
    if len(all_seen) == len(locations):
        break
seen_nodes = {e[0] for e in all_seen}
print(len(seen_nodes) + 1)

for _y in range(y+1):
    for _x in range(x+1):
        if (_x, _y) in seen_nodes:
            print('O', end='')
        elif (_x, _y) in maze:
            print('.', end='')
        else:
            print('#', end='')
    print()