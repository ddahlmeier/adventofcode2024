from itertools import product
from operator import add, mul
import sys

def concat(a, b):
    return int(str(a)+str(b))

def parse_equation(line):
    test_value, numbers = line.split(":")
    test_value = int(test_value)
    numbers = list(map(int, numbers.split()))
    return test_value, numbers

def parse_equations(input):
    return [parse_equation(line) for line in input]

def check_equation(test_value, numbers, operators):
    value = numbers[0]
    for operator, operant in zip(operators, numbers[1:]):
        value = operator(value, operant)
    return test_value == value

def check(test_value, numbers):
    return any((check_equation(test_value, numbers, operators) for operators in product([add, mul, concat], repeat=len(numbers)-1)))

if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = fin.read().splitlines()
    print(sum((test_value for test_value, numbers in parse_equations(input) if check(test_value, numbers))))

     