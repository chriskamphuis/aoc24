data = []
starts = set()
with open('../data/4.txt') as f:
    for y, line in enumerate(f):
        line_data = []
        for x, char in enumerate(line.strip()):
            line_data.append(char)
            if char == 'X':
                starts.add((x, y))
        data.append(line_data)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
values = ['M', 'A', 'S']

count = 0
for x, y in starts:
    for dx, dy in directions:
        if all([0 <= y + dy * (i+1) < len(data)
                and 0 <= x + dx * (i+1) < len(data[0])
                and data[y + dy * (i+1)][x + dx * (i+1)] == value
                for i, value in enumerate(values)]):
            count += 1
print(count)

def test_x_mas(d, _x, _y, start='M'):
    end = 'S' if start == 'M' else 'M'
    if d[_y][_x] != start or d[_y+1][_x+1] != 'A':
        return False
    if d[_y+2][_x] == start:
        return d[_y][_x+2] == end and d[_y+2][_x+2] == end
    if d[_y][_x+2] == start:
        return d[_y+2][_x] == end and d[_y+2][_x+2] == end

count = 0
for y, line in enumerate(data[:-2]):
    for x, char in enumerate(line[:-2]):
        if test_x_mas(data, x, y) or test_x_mas(data, x, y, 'S'):
            count += 1
print(count)

