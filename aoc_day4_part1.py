from collections import defaultdict
import sys
                
                
def search_xmas(puzzle, coordinate, n_rows, n_columns, path_len, direction):
    if (puzzle[coordinate[0]][coordinate[1]]) != "XMAS"[path_len]:
        return 0
    elif path_len == 3:
        return 1
    next = (coordinate[0]+direction[0], coordinate[1]+direction[1])
    if next[0]>=0 and next[0]<n_rows and next[1]>=0 and next[1]<n_columns :
        return search_xmas(puzzle, next, n_rows, n_columns, path_len+1, direction) 
    else:
        return 0    
        
def search_all_xmas(puzzle):
    n_rows = len(puzzle)
    n_columns = len(puzzle[0])
    xmas_counts = 0
    for r in range(n_rows):
        for c in range (n_columns):
            for direction in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                xmas_counts += search_xmas(puzzle, (r,c), n_rows, n_columns, 0, direction)
    return xmas_counts

if __name__ == "__main__":
    with open (sys.argv[1]) as fin:
        puzzle = fin.read().splitlines()
    print(search_all_xmas(puzzle))
