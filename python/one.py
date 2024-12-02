from collections import Counter
left, right = zip(*([[int(x) for x in e.split('   ')] for e in open('../data/1.txt').read().splitlines()]))
left, right = sorted(left), sorted(right)
print(sum([abs(l-r) for l,r in zip(left, right)]))
right = Counter(right)
print(sum([right[l]*l for l in left]))