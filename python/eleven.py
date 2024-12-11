from functools import lru_cache

stones = [int(e) for e in open('../data/11.txt').read().strip().split()]

@lru_cache(maxsize=None)
def blink(stone, depth):
    if depth == 0:
        return 1
    else:
        if stone == 0:
            return blink(1, depth - 1)
        if len(str(stone)) % 2 == 0:
            sep = 10**(len(str(stone)) // 2)
            return blink(stone//sep, depth - 1) + blink(stone%sep, depth - 1)
        else:
            return blink(stone * 2024, depth - 1)

count = 0
for s in stones:
    count += blink(s, 75)
print(count)