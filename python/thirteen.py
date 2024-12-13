import re

with open('../data/13.txt', 'r') as f:
    machines = [b.split('\n') for b in f.read().strip().split('\n\n')]

cost_a = 0
cost_b = 0
for machine in machines:
    (a, b), (c, d), (x, y) = [[int(e) for e in re.findall(r"\d+", m)] for m in machine]
    j = (-b * x + a * y) // (-b * c + d * a)
    i = (x - c * j) // a
    if  a * i + c * j == x and b * i + d * j == y:
        cost_a += 3 * i + j
    x += 10000000000000
    y += 10000000000000
    j = (-b * x + a * y) // (-b * c + d * a)
    i = (x - c * j) // a
    if  a * i + c * j == x and b * i + d * j == y:
        cost_b += 3 * i + j

print(cost_a)
print(cost_b)