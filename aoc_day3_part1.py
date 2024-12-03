import sys


# possible states: m, u, l, (, ), digit1, digit2, digit3
# transitions 
# any -> m
#   m -> u
#   u -> l
#   l -> (
#   ( -> 0-9
#   0-9 -> 0-9
#   0-9 -> ,
#   , -> 0-9
#   0-9 -> )

result = 0
first_value = ""
second_value = ""

def state_transition(state, symbol):
    global first_value
    global second_value
    global result
    
    if symbol == "m":
        return "m"
    elif state == "m" and symbol == "u":
        return "u"
    elif state == "u" and symbol == "l":
        return "l"
    elif state == "l" and symbol == "(":
        return "("
    elif state == "(" and symbol in "0123456789":
        first_value += symbol
        return "v1d1"
    elif state == "v1d1" and symbol in "0123456789":
        first_value += symbol
        return "v1d2"
    elif state == "v1d2" and symbol in "0123456789":
        first_value += symbol
        return "v1d3"
    elif state in ["v1d1", "v1d2", "v1d3"] and symbol == ",":
        second_value = ""
        return ","
    elif state == "," and symbol in "0123456789":
        second_value += symbol
        return "v2d1"
    elif state == "v2d1" and symbol in "0123456789":
        second_value += symbol
        return "v2d2"
    elif state == "v2d2" and symbol in "0123456789":
        second_value += symbol
        return "v2d3"
    elif state in ["v2d1", "v2d2", "v2d3"] and symbol == ")":
        result += int(first_value) * int(second_value)
        print("multiply", int(first_value), "and", int(second_value))
        first_value = ""
        second_value = ""
    else:
        first_value = ""
        second_value = ""
        state = "Null"

with open (sys.argv[1]) as fin:
    statement = fin.read().strip()

print(statement)
state = "Null"
for symbol in statement:
    state = state_transition(state, symbol)
print(result)