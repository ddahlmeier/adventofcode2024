from collections import defaultdict
import sys

def parse_rules(input):
    rules_before = defaultdict(list)
    for rule in [list(map(int, row.split("|"))) for row in input.splitlines() if len(row.strip())>0]:
        rules_before[rule[0]].append(rule[1])
    return rules_before


def passes_rules(rules, update):
    return not any(page in rules[following_page] for i, page in enumerate(update) for following_page in update[i+1:])

if __name__ == "__main__":
    with open (sys.argv[1]) as fin:
        ordering_rules, updates = fin.read().split("\n\n")
    rules = parse_rules(ordering_rules)
    updates = [list(map(int, line.split(','))) for line in updates.splitlines()]
    correct_ordered = filter(lambda x: passes_rules(rules, x), updates)
    middles_pages = [update[len(update)//2] for update in correct_ordered]
    print(sum(middles_pages))
            
