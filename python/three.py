import re
data = open('../data/3.txt').read().strip()
found = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", data)
print(sum([int(a)*int(b) for a,b in found]))
found2 = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\)|don't\(\))", data)
do = True
count = 0
for a, b, action in found2:
    if action:
        if action == 'do()':
            do = True
        elif action == "don't()":
            do = False
        continue
    if do:
        count += int(a)*int(b)
print(count)