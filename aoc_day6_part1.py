import sys

def parse_map(input):
    lab_map = {(row,col): None for col in list(range(len(input.splitlines()[0]))) for row in list(range(len(input.splitlines()))) }
    guard_position = None
    guard_direction = None
    for r, row in enumerate(input.splitlines()):
        for c, field in enumerate(row):
            lab_map[(r,c)] = field
            if field in "^><v":
                guard_position = (r, c)
                guard_direction = field
    return (lab_map, guard_position, guard_direction)

def next_position(guard_position, guard_direction):
    if guard_direction == "<":
        return (guard_position[0], guard_position[1]-1)
    elif guard_direction == ">":
        return (guard_position[0], guard_position[1]+1)
    elif guard_direction == "^":
        return (guard_position[0]-1, guard_position[1])
    elif guard_direction == "v":
        return (guard_position[0]+1, guard_position[1])

def turn(direction):
    turn_right90 = {"^": ">", ">": "v", "v": "<", "<": "^"}
    return turn_right90[direction]

def is_blocked(lab_map, position):
    return lab_map[position] == "#"

def is_outside_map(lab_map, position):
    return position not in lab_map.keys()


def generate_path(lab_map, guard_position, guard_direction):
    yield guard_position
    while True:
        next = next_position(guard_position, guard_direction)
        if is_outside_map(lab_map, next):
            break
        elif is_blocked(lab_map, next):
            guard_direction = turn(guard_direction)
        else:
            guard_position = next
        yield guard_position

if __name__ == "__main__":
    with (open(sys.argv[1]) as fin):
        lab_map, guard_start_position, guard_start_direction = parse_map(fin.read())
    covered_fields = set(generate_path(lab_map, guard_start_position, guard_start_direction))
    print(len(covered_fields))