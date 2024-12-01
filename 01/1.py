left, right = zip(*([[int(x) for x in e.split('   ')] for e in open('input.txt').read().splitlines()]))
left, right = sorted(left), sorted(right)
print(sum([abs(l-r) for l,r in zip(left, right)]))