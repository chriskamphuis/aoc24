from collections import Counter
left, right = zip(*([[int(x) for x in e.split('   ')] for e in open('input.txt').read().splitlines()]))
right = Counter(right)
print(sum([right[l]*l for l in left]))
