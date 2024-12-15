from operator import itemgetter
import sys


def get_plant(point, garden_map):
    r, c = point
    return garden_map[r][c]

def is_valid(point, garden_map):
    r, c = point
    max_rows = len(garden_map)
    max_cols = len(garden_map[0])
    return r>=0 and r<max_rows and c>=0 and c<max_cols

def up(r, c):
    return (r-1, c)

def down(r, c):
    return (r+1, c)

def left(r, c):
    return (r, c-1)

def right(r, c):
    return (r, c+1)

def is_contiguous(p1, p2, direction="horizontal"):
    if direction == "horizontal":
        return p1[0] ==  p2[0] and p1[1]+1 == p2[1] 
    elif direction == "vertical":
        return p1[1] ==  p2[1] and p1[0]+1 == p2[0] 
    else:
        assert(False)
    
def contiguous_side(points, direction="horizontal"):
    if len(points) == 0:
        return []
    if direction == "horizontal":
        get_key = itemgetter(1)
    elif direction == "vertical":
        get_key = itemgetter(0)
    else:
        assert(False)
    points_sorted = sorted(points, key=get_key, reverse=True)
    continuos = [points_sorted.pop()]
    while(len(points_sorted)>0):
        point = points_sorted.pop()
        if is_contiguous(continuos[-1], point, direction):
            continuos.append(point)
        else:
            yield continuos
            continuos = [point]
    yield continuos
        
        
def sides(region):
    _, points = region
    # check horizontal sides up and down
    for row in {r for r, _ in points}:
        for direction in [up, down]:            
            outer_points = [(r,c) for r, c in points if r == row and direction(r, c) not in points]
            for side in contiguous_side(list(filter(lambda x:x[0] == row, outer_points)), direction="horizontal"):
                yield side
    # check vertical sides left and right
    for column in {c for _, c in points}:
        for direction in [left, right]:            
            outer_points = [(r,c) for r, c in points if c == column and direction(r, c) not in points]
            for side in contiguous_side(list(filter(lambda x:x[1] == column, outer_points)), direction="vertical"):
                yield side

def price(region):
    return len(region[1]) * len(list(sides(region)))

def get_regions(garden_map):
    # region = a tuple of a plant type and a set of points: (plant, {(r,c), (r,c), ..})
    adjacency_graph = {(plant, frozenset([(r, c)])): list(map(lambda x: (get_plant(x, garden_map), frozenset([x])), filter(lambda x: is_valid(x, garden_map), [up(r, c), down(r, c), left(r, c), right(r, c)])))
                 for r, row in enumerate(garden_map) for c, plant in enumerate(row)}
    while True:
        found_merge = False
        for region1, adjacent_regions in adjacency_graph.items():
            for region2 in filter(lambda x: x in adjacency_graph.keys(), adjacent_regions):
                plant1, points1 = region1
                plant2, points2 = region2
                if plant1 == plant2:
                    # merge keys
                    region_merged = (plant1, points1.union(points2))
                    neighbors_merged = [region for region in adjacent_regions + adjacency_graph[region2] if region not in [region1, region2]]
                    adjacency_graph[region_merged] = neighbors_merged
                    # remove merged regions from keys
                    adjacency_graph.pop(region1)
                    adjacency_graph.pop(region2)
                    # remove merged regions from values and add new region
                    for neighbor_set in adjacency_graph.values():
                        if region1 in neighbor_set:
                            neighbor_set.remove(region1)
                            neighbor_set.append(region_merged)
                        if region2 in neighbor_set:
                            neighbor_set.remove(region2)
                            neighbor_set.append(region_merged)
                    found_merge = True
                    break
            if found_merge:
                # state of neighbors has changed. exist loop and restart
                break
        if not found_merge:
            break
    return adjacency_graph.keys()
   

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input  = fin.read().strip()
    garden_map = [list(row) for row in input.splitlines()]
    regions = get_regions(garden_map)
    print(sum(price(region) for region in regions))
    