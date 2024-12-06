from collections import defaultdict
from functools import cmp_to_key

rules, updates = open('../data/5.txt').read().strip().split('\n\n')
before_after_map = defaultdict(set)
for before, after in [[int(a) for a in r.split('|')] for r in rules.split('\n')]:
    before_after_map[before].add(after)

valid, invalid = [], []
for update in updates.split('\n'):
    seen = set()
    up = [int(e) for e in update.split(',')]
    for e in up:
        if before_after_map[e] & seen:
            invalid.append(up)
            break
        seen.add(e)
    else:
        valid.append(up)

print(sum([v[len(v)//2] for v in valid]))
print(sum([sorted(iv, key=cmp_to_key(lambda a, b: -1 if a in before_after_map[b] else 1))[len(iv)//2] for iv in invalid]))