with open('../data/9.txt') as f:
    data = f.read().strip()
blocks = []
groups = []
for i, char in enumerate(data):
    if i % 2 == 0:
        groups.append((int(char), len(blocks)))
    for n in range(int(char)):
        if i % 2 == 0:
            blocks.append(i//2)
        else:
            blocks.append(None)

# part 1
total = 0
runner = 0
back_runner = len(blocks) - 1
while runner <= back_runner:
    if blocks[runner] is not None:
        total += blocks[runner] * runner
        runner += 1
    else:
        while blocks[back_runner] is None:
            back_runner -= 1
        total += blocks[back_runner] * runner
        runner += 1
        back_runner -= 1
print(total)

# part 2
for amount, offset in groups[::-1]:
    for i in range(offset):
        if all([b is None for b in blocks[i:i+amount]]):
            blocks[i:i+amount] = blocks[offset:offset+amount]
            blocks[offset:offset+amount] = [None for _ in range(amount)]
            break
total = 0
for i, block in enumerate(blocks):
    if block is not None:
        total += block * i
print(total)