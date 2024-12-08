from itertools import combinations
from collections import defaultdict
import sys

def parse_map(input):
    antennas = defaultdict(list)
    for r, row in enumerate(input.splitlines()):
        for c, symbol in enumerate(row):
            if symbol != '.':
                antennas[symbol].append((r, c))
    return antennas, r+1, c+1

def diff(point1, point2):
    return (point2[0]-point1[0], point2[1]-point1[1])

def add(point, dist):
    return (point[0]+dist[0], point[1]+dist[1])

def sub(point, dist):
    return (point[0]-dist[0], point[1]-dist[1])
    
def mul(dist, factor):
    return (dist[0]*factor, dist[1]*factor)

def neg(dist):
    return (-dist[0], -dist[1])

def on_map(point, max_rows, max_cols):
    return 0 <= point[0] < max_rows and 0 <= point[1] < max_cols
    
def get_antinodes(points, num_rows, num_cols):
    for point1, point2 in combinations(points, 2):
            delta = diff(point1, point2)
            antinode = point1
            yield antinode
            while(True):
                antinode = add(antinode, delta)
                if not on_map(antinode, num_rows, num_cols):
                    break
                yield antinode
            antinode = point1
            while(True):
                antinode = sub(antinode, delta)
                if not on_map(antinode, num_rows, num_cols):
                    break
                yield antinode

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = fin.read()
    print(input)
    antennas, num_rows, num_cols = parse_map(input)
    antinodes = set()
    for freq in antennas.keys():
        antinodes.update(get_antinodes(antennas[freq], num_rows, num_cols))
    print(len(antinodes))

