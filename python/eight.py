from collections import defaultdict

nodes = defaultdict(list)
antennas = set()

x_min = y_min = 0
with open('../data/8.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            match char:
                case '.':
                    continue
                case node:
                    nodes[node].append((y, x))
                    antennas.add((y, x))
x_max = x + 1
y_max = y + 1

anti_nodes = set()
for _, values in nodes.items():
    for y, x in values:
        for y2, x2 in values:
            if y == y2 and x == x2:
                continue
            if y_min <= y2 + (y2 - y) < y_max and x_min <= x2 + (x2 - x) < x_max:
                anti_nodes.add((y2 + (y2 - y), x2 + (x2 - x)))
print(len(anti_nodes))

anti_nodes = set()
for _, values in nodes.items():
    for y, x in values:
        for y2, x2 in values:
            if y == y2 and x == x2:
                continue
            y_dist = y2 - y
            x_dist = x2 - x
            i = 1
            while y_min <= y2 + i * y_dist < y_max and x_min <= x2 + i * x_dist < x_max:
                anti_nodes.add((y2 + i * y_dist, x2 + i * x_dist))
                i += 1
print(len(anti_nodes | antennas))
