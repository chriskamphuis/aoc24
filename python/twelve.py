from collections import defaultdict

store = dict()
clusters = dict()
sizes = defaultdict(int)

with open('../data/12.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            store[(y, x)] = c
            clusters[(y, x)] = -1

neighbours = lambda _y, _x : [(_y + 1, _x), (_y - 1, _x), (_y, _x + 1), (_y, _x - 1)]

# Build clusters, and part 1
def search(_location, _cluster_id):
    clusters[_location] = _cluster_id
    sizes[_cluster_id] += 1
    for _neighbour in neighbours(*_location):
        if _neighbour not in clusters:
            continue
        elif store[_neighbour] == store[_location] and clusters[_neighbour] == -1:
            search(_neighbour, _cluster_id)

cluster_ids = (i for i in range(len(store)))
for location, cluster_id in clusters.items():
    if cluster_id != -1:
        continue
    cluster_id = next(cluster_ids)
    search(location, cluster_id)

# Part 2
sides = defaultdict(int)
processed = set()
difference = lambda x, y, x2, y2 : (x - x2, y - y2)
orthogonal = lambda x, y: {(y, x), (-y, x), (-y, -x), (y, -x)}
step = lambda x, y, dx, dy, s: (x + dx * s, y + dy * s)

for location, cluster_id in clusters.items():
    for neighbour in neighbours(*location):
        if (location, neighbour) in processed or neighbour in clusters and clusters[neighbour] == cluster_id:
            continue
        for direction in orthogonal(*difference(*location, *neighbour)):
            i = 0
            while True:
                new_loc = step(*location, *direction, i)
                new_neighbour = step(*neighbour, *direction, i)
                if new_loc in clusters and new_neighbour in clusters and clusters[location] == clusters[new_loc] and clusters[location] != clusters[new_neighbour]:
                    processed.add((new_loc, new_neighbour))
                elif new_loc in clusters and new_neighbour not in clusters and clusters[location] == clusters[new_loc]:
                    processed.add((new_loc, new_neighbour))
                else:
                    break
                i += 1
        sides[cluster_id] += 1

costs_a = costs_b = 0
for location, cluster_id in clusters.items():
    costs_b += sides[cluster_id]
    for neighbour in neighbours(*location):
        if neighbour in clusters and clusters[neighbour] == cluster_id:
            continue
        costs_a += sizes[cluster_id]

print(costs_a)
print(costs_b)