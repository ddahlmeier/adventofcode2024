# advents of code day 1

import sys

list1 = []
list2 = []


with open (sys.argv[1]) as fin:
    input = fin.readlines()
    
    for line in input:
        left, right = map(int, line.split())
        list1.append(left)
        list2.append(right)
        
list1.sort()
list2.sort()

distance = 0

for left, right in zip(list1, list2):
    distance += abs(left-right)

print(distance)

