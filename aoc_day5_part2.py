from collections import defaultdict
import sys

def parse_rules(input):
    rules_before = defaultdict(list)
    for rule in [list(map(int, row.split("|"))) for row in input.splitlines() if len(row.strip())>0]:
        rules_before[rule[0]].append(rule[1])
    return rules_before

def passes_rules(rules, update):
    return not any(page in rules[following_page] for i, page in enumerate(update) for following_page in update[i+1:])

def insert_page(update, pos, page):
    return update[:pos] + [page] + update[pos:]

def reorder_pages(rules, update):
    ordered = []
    for page in update:
        inserted = False
        for position in range(len(ordered)+1):
            # check if inserting page in this position violates any rule, if not insert page
            if (passes_rules(rules, insert_page(ordered, position, page))):
                ordered =insert_page(ordered, position, page)
                inserted = True
                break
        if not inserted:
            print("WARNING: failed to find a position to insert", page, "into", ordered)
            sys.exit(1)
    return ordered
            
if __name__ == "__main__":
    with open (sys.argv[1]) as fin:
        ordering_rules, updates = fin.read().split("\n\n")
    rules = parse_rules(ordering_rules)
    updates = [list(map(int, line.split(','))) for line in updates.splitlines()]
    incorrect_ordered = filter(lambda x: not passes_rules(rules, x), updates)
    reordered = map(lambda x: reorder_pages(rules, x), incorrect_ordered)
    middles_pages = (update[len(update)//2] for update in reordered)
    print(sum(middles_pages))
            
