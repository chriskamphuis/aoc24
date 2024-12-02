data = [[int(x) for x in line.split(' ')] for line in open('../data/2.txt').read().splitlines()]
step_up = lambda l: all([0 < l[i+1] - l[i] < 4 for i in range(len(l)-1)])
print(len([d for d in data if step_up(d) or step_up(d[::-1])]))
count = 0
for d in data:
    for x in [d, d[::-1]]:
        for i in range(len(x)-1):
            if 0 < x[i+1] - x[i] < 4:
                continue
            elif step_up(x[i-1:i] + x[i+1:]) or step_up([x[i]] + x[i+2:]):
                count += 1
                break
            else:
                break
        else:
            count += 1
            break
print(count)