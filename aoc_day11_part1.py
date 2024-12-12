import sys

def rules(stone):
    if stone == 0:
        return 1
    elif len(str(stone))%2 == 0:
        stone = str(stone)
        return list(map(int, [stone[:len(stone)//2], stone[len(stone)//2:]]))
    else:
        return stone * 2024

def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):  # If the item is a list, recurse
            flat.extend(flatten(item))
        else:  # If the item is not a list, add it directly
            flat.append(item)
    return flat

def blink(stones):
    return flatten(map(rules, stones))

def blink_ntimes(stones, n):
    for _ in range(n):
        stones = blink(stones)
        yield(stones)

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = list(map(int, fin.readline().split()))
    for n, next_stones in enumerate(blink_ntimes(input, 25)):
        print(n, len(next_stones))