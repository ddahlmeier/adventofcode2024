# advents of code day 1
# part 2

from collections import Counter
import sys


list1 = []
list2 = []


with open (sys.argv[1]) as fin:
    input = fin.readlines()
    
    for line in input:
        left, right = map(int, line.split())
        list1.append(left)
        list2.append(right)
        
counts = Counter(list2)
similarity = 0

for item in list1:
    multiplier = counts[item] if item in counts.keys() else 0
    similarity += item * multiplier

print(similarity)

