from collections import Counter, defaultdict
import sys

def rules(stone):
    if stone == 0:
        return [1]
    elif len(str(stone))%2 == 0:
        stone = str(stone)
        return list(map(int, [stone[:len(stone)//2], stone[len(stone)//2:]]))
    else:
        return [stone * 2024]

def blink_ntimes(state, n):
    yield state
    for _ in range(n):
        state = blink(state)
        yield state

def blink(state):
    next_state = defaultdict(int)
    for stone, count in state.items():
        for next_stone in rules(stone):
            next_state[next_stone] += count
    return next_state

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = Counter(map(int, fin.readline().split()))
    for n, next_stones in enumerate(blink_ntimes(input, int(sys.argv[2]))):
        print(n, sum(next_stones.values()))