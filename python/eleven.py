stones = [int(e) for e in open('../data/11.txt').read().strip().split()]
store = dict()
def blink(stone, depth):
    if (stone, depth) in store:
        return store[(stone, depth)]
    if depth == 0:
        return 1
    if stone == 0:
        store[(stone, depth)] = blink(1, depth - 1)
    elif (l := len(str(stone))) % 2 == 0:
        sep = 10 ** (l // 2)
        store[(stone, depth)] = blink(stone//sep, depth - 1) + blink(stone%sep, depth - 1)
    else:
        store[(stone, depth)] = blink(stone * 2024, depth - 1)
    return store[(stone, depth)]

print(sum([blink(s, 25) for s in stones]))
print(sum([blink(s, 75) for s in stones]))
