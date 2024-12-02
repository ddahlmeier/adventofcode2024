# advents of code day 2 part 1

import sys

def is_decreasing(pair):
    return pair[0] > pair[1]

def is_increasing(pair):
    return pair[0] < pair[1]

def within_difference(pair, min_diff=1, max_diff=3):
    return min_diff <= abs(pair[0]-pair[1]) <= max_diff

def is_safe(report):
    steps = list(zip(report, report[1:]))
    return (all(map(is_decreasing, steps)) or 
            all(map(is_increasing, steps))) and all(map(within_difference, steps))
            
    
with open (sys.argv[1]) as fin:
    reports = [list(map(int, line.split())) for line in fin.readlines()]
    count_safe = sum(map(is_safe, reports))    
    print(count_safe)