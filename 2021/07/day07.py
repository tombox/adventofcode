"""
https://adventofcode.com/2021/day/6
"""
from itertools import repeat
import math

def load_data(filename: str) -> tuple:
    " Load fish data "
    items = [int(x) for x in open(filename, "r").read().split(',')]
    return items

def part1(file: str) -> int:
    " Day 07 puzzle part 1"
    items  = load_data(file)  
    lowest_cost = None

    for pos in range(max(items)):
        cost = sum(abs(x-pos) for x in items)
        lowest_cost = cost if lowest_cost is None else lowest_cost
        lowest_cost = min(cost,lowest_cost)

    return lowest_cost

def part1_minified(file):
    items = [int(x) for x in open(file, "r").read().split(',')]
    return min([sum(abs(x-p) for x in items) for p in range(max(items))])

def part2_minified(file):
    items = [int(x) for x in open(file, "r").read().split(',')]
    return min([sum(int((abs(x-p)/2)*(abs(x-p)+1)) for x in items) for p in range(max(items))])


def part2(file: str) -> int:
    " Day 07 puzzle part 2"
    items  = load_data(file)  
    lowest_cost = None

    for pos in range(max(items)):
        cost = sum(int((abs(x-pos)/2)*(abs(x-pos)+1)) for x in items)
        lowest_cost = cost if lowest_cost is None else lowest_cost
        lowest_cost = min(cost,lowest_cost)

    return lowest_cost  

def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 37

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 357353

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 168

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 104822130

print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))


print("Part 1 min test answer = ", part1_minified("test-input.txt"))
print("Part 1 min answer = ", part1_minified("input.txt"))

print("Part 2 min test answer = ", part2_minified("test-input.txt"))
print("Part 2 min answer = ", part2_minified("input.txt"))

