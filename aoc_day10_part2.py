import sys

def up(pos):
    row, col = pos
    return (row-1, col) if row > 0 else None

def down(topo_map, pos):
    row, col = pos
    return (row+1, col) if row < len(topo_map)-1 else None

def left(pos):
    row, col = pos
    return (row, col-1) if col >0 else None

def right(topo_map, pos):
    row, col = pos
    return (row, col+1) if col < len(topo_map[0])-1 else None

def map_value(topo_map, pos):
    return topo_map[pos[0]][pos[1]]
            
def search_trails(start_pos, topo_map):
    trails = [[start_pos]]
    while len(trails)>0:
        trail =  trails.pop()
        if len(trail) == 10:
            yield trail
        pos = trail[-1]
        for next_pos in [up(pos), down(topo_map, pos), left(pos), right(topo_map, pos)]:
            if next_pos and map_value(topo_map, pos)+1 == map_value(topo_map, next_pos):
                trails.append(trail + [next_pos])

def trail_rating(trailhead, topo_map):
    return sum(1 for _ in search_trails(trailhead, topo_map))

         
if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = fin.read().splitlines()
    topo_map = [list(map(int, row)) for row in input]
    trailheads = [(r,c) for r, row in enumerate(topo_map) for c, value in enumerate(row)  if value == 0]
    print(sum(trail_rating(trailhead, topo_map) for trailhead in trailheads))

    