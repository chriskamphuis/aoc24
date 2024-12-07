totals = []
rules = []
with open('../data/7.txt') as f:
    for line in f.readlines():
        total, parts = line.strip().split(':')
        parts = parts.strip().split()
        totals.append(int(total))
        rules.append([int(p) for p in parts])

def is_possible(total, rules, subscore=0):
    if total == subscore and len(rules) == 0:
        return True
    if subscore > total or len(rules) == 0:
        return False
    else:
        r = rules[0]
        return is_possible(total, rules[1:], subscore+r) or is_possible(total, rules[1:], subscore*r) or is_possible(total, rules[1:], int(str(subscore) + str(r)))

count = 0
for total, rule in zip(totals, rules):
    if is_possible(total, rule):
        count += total
print(count)