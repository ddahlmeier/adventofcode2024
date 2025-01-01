import math
import sys

def parse(input):
    return [list(map(lambda x: list(map(int, x[2:].split(","))), line.split())) for line in input]


def count_robots(robots_state, positions):
    return len(list(filter(lambda pos: pos[0] in positions, robots_state)))


def move(state, x_tiles, y_tiles):
    pos, speed = state
    return [[(pos[0]+speed[0]) % x_tiles, (pos[1]+speed[1]) % y_tiles], speed]

def get_position(state):
    return state[0]


def get_robots_in_row(robots_state, y):
    return list(filter(lambda pos: pos[0][1] == y, robots_state))


def encode(robots_state, y_tiles):
    length_encoded = []
    for y in range(y_tiles):
        segment = []
        for position in sorted(map(get_position, get_robots_in_row(robots_state, y)), key=lambda pos:pos[0]):
            if segment == []:
                segment.append(position)
            elif segment[-1][0] == position[0]-1:
                segment.append(position)
            else:
                length_encoded.append(segment)
                segment = [position]
        length_encoded.append(segment)
    return length_encoded

    
def shows_xmastree(robots_state, y_tiles):
    x_center = None
    for y in range(y_tiles):
        robots =  get_robots_in_row(robots_state, y)
        if len(robots) == 0:
            continue
        elif x_center is None and len(robots) == 1:
            # found tip of xmas tree, remember x coordinate
            x_center = robots[0][0][0]
        elif x_center is None and len(robots) > 1:
            return False
        elif x_center is not None:
            # check if robots are symmetrical
            left_most_x = min(robots, key=lambda x: x[0][0])[0][0]
            right_most_x = max(robots, key=lambda x: x[0][0])[0][0]
            symmetrical = x_center - left_most_x == right_most_x - x_center
            if not symmetrical:
                return False
    return True
    

def simulate(robots_state, x_tiles, y_tiles, steps=1):
    move_robot = lambda state: move(state, x_tiles, y_tiles)
    state = robots_state
    yield state
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

    for n, state in enumerate(simulate(robots_state, x_tiles, y_tiles, steps=10000)):
        encoded = encode(state, y_tiles)
        if len(encoded) < 300:
            print("== After step ", n)
            print_map(state, x_tiles, y_tiles)
            break
        