import math
import sys

def parse(input):
    return [list(map(lambda x: list(map(int, x[2:].split(","))), line.split())) for line in input]


def robots_per_quadrant(robots_state, x_tiles, y_tiles):
    for x_min, x_max in [(0, x_tiles//2), ((x_tiles//2)+1, x_tiles)]:
        for y_min, y_max in [(0, y_tiles//2), ((y_tiles//2)+1, y_tiles)]:
            quadrant = [[x, y] for x in range(x_min, x_max) for y in range(y_min, y_max)]
            yield count_robots(robots_state, quadrant)


def count_robots(robots_state, positions):
    return len(list(filter(lambda pos: pos[0] in positions, robots_state)))


def move(state, x_tiles, y_tiles):
    pos, speed = state
    return [[(pos[0]+speed[0]) % x_tiles, (pos[1]+speed[1]) % y_tiles], speed]


def simulate(robots_state, x_tiles, y_tiles, steps=1):
    move_robot = lambda state: move(state, x_tiles, y_tiles)
    state = robots_state
    for _ in range(steps):
        state = list(map(move_robot, state))
        yield state


def print_map(robots_state, x_tiles, y_tiles):
    for y in range(y_tiles):
        for x in range(x_tiles):
            num_robots = count_robots(robots_state, [[x, y]])
            print(num_robots if num_robots>0 else '.', end="")
        print("")
    
    
        
if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        robots_state = parse(fin.read().splitlines())
    x_tiles = int(sys.argv[2])
    y_tiles = int(sys.argv[3])
    
    for n, state in enumerate(simulate(robots_state, x_tiles, y_tiles, steps=100)):
        pass
    result = math.prod([count for count in robots_per_quadrant(state, x_tiles, y_tiles)])
    print(result)