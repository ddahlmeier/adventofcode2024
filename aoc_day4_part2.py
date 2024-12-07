import sys

def get(puzzle, r, c):
    n_rows = len(puzzle)
    n_columns = len(puzzle[0])
    if r>=0 and r<n_rows and c>=0 and c<n_columns :
        return puzzle[r][c]
    else:
        return ""

def has_xmas(puzzle, r, c):
    return get(puzzle, r, c) + get(puzzle, r+1, c+1) + get(puzzle, r+2, c+2) in ["MAS", "SAM"] \
        and get(puzzle, r, c+2) + get(puzzle, r+1, c+1) + get(puzzle, r+2, c) in ["MAS", "SAM"]

def count_all_xmas(puzzle):
    n_rows = len(puzzle)
    n_columns = len(puzzle[0])
    return sum((has_xmas(puzzle, r, c) for r in range(n_rows) for c in range (n_columns)))
    

if __name__ == "__main__":
    with open (sys.argv[1]) as fin:
        puzzle = fin.read().splitlines()
    print(count_all_xmas(puzzle))
