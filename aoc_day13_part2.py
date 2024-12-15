import math
import sys

def parse(line):
    return tuple(map(lambda x:int(x.strip("XY=,")), line.split()[-2:]))

def parse_block(block):
    button_a, button_b, price = map(parse, block.splitlines())
    # increase price coordinates by 10000000000000
    price = (price[0]+10000000000000, price[1]+10000000000000)
    return button_a, button_b, price
    
def parse_input(input):
    return [ parse_block(block) for block in input.split("\n\n")]

def cheapest_way_to_win(puzzle):
    button_A, button_B, price_location = puzzle
    price_x, price_y = price_location
    button_A_x, button_A_y = button_A
    button_B_x, button_B_y = button_B

    # solve analytically
    pressB = (price_x - ((price_y * button_A_x) / button_A_y)) / (button_B_x - ((button_B_y * button_A_x)/ button_A_y))        
    pressA = (((price_y * button_A_x) / button_A_y) - ((button_B_y * button_A_x * pressB) / button_A_y)) / button_A_x
    # check result
    pressA, pressB = round(pressA), round(pressB)
    check_position = (button_A_x * pressA + button_B_x * pressB, button_A_y * pressA + button_B_y * pressB)
    return (pressA, pressB) if check_position == price_location else None

def tokens(cheapest_way):
    pressA, pressB = cheapest_way
    return pressA*3 + pressB

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = fin.read()
    print(sum(map(lambda x: tokens(x) if x != None else 0, (cheapest_way_to_win(puzzle) for puzzle in parse_input(input)))))
