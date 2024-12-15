import sys

def parse(line):
    return tuple(map(lambda x:int(x.strip("XY=,")), line.split()[-2:]))

def parse_block(block):
    button_a, button_b, price = map(parse, block.splitlines())
    return button_a, button_b, price
    
def parse_input(input):
    return [ parse_block(block) for block in input.split("\n\n")]

def add(position, button):
    return position[0]+button[0], position[1]+button[1]

def mul(button, n):
    return button[0]*n, button[1]*n


def cheapest_way_to_win(puzzle):
    button_A, button_B, price_location = puzzle
    search_grid = []
    for row in range(101):
        search_grid.append([add(mul(button_B, row), mul(button_A, col)) for col in range(101)])
    matches_price = [(col, row) for row in range(101) for col in range(101) if search_grid[row][col] == price_location]
    return matches_price[0] if len(matches_price)>0 else None

def tokens(cheapest_way):
    pressA, pressB = cheapest_way
    return pressA*3 + pressB

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = fin.read()
    for puzzle in parse_input(input):
        result = cheapest_way_to_win(puzzle)
        print(puzzle, result) 
    print(sum(map(lambda x: tokens(x) if x != None else 0, (cheapest_way_to_win(puzzle) for puzzle in parse_input(input)))))
    