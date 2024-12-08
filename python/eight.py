from collections import defaultdict

nodes = defaultdict(list)

x_min = y_min = 0
with open('../data/8.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            match char:
                case '.':
                    continue
                case node:
                    nodes[node].append((y, x))
x_max = x + 1
y_max = y + 1
anti_nodes_a = set()
anti_nodes_b = set()
for _, values in nodes.items():
    for y, x in values:
        for y2, x2 in values:
            if y == y2 and x == x2:
                continue
            i = 0
            while y_min <= y2 + i * (y2 - y) < y_max and x_min <= x2 + i * (x2 - x) < x_max:
                if i == 1:
                    anti_nodes_a.add((y2 + i * (y2 - y), x2 + i * (x2 - x)))
                anti_nodes_b.add((y2 + i * (y2 - y), x2 + i * (x2 - x)))
                i += 1
print(len(anti_nodes_a))
print(len(anti_nodes_b))
