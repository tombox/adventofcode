"""
https://adventofcode.com/2021/day/6
"""
from itertools import repeat

def load_data(filename: str) -> tuple:
    " Load fish data "
    items = [int(x) for x in open(filename, "r").read().split(',')]
    return items

def part1(file: str) -> int:
    " Day 06 puzzle part 1"
    items  = load_data(file)  
    days=80
    for day in range(days):
        for n in range(len(items)):
            items[n] -= 1
            if items[n] == -1:
                items[n] = 6
                items.append(8)
    return len(items)

def part2(file: str) -> int:
    " Day 06 puzzle part 2"
    items  = load_data(file)  
    days = 256
    day = 0
    births = []
    births = list(repeat(0, days+9))

    for item in items: 
        births[item] += 1

    fish = len(items)
    for day in range(days):
        fish += births[day]
        births[day+9] += births[day] # set new fish to be born
        births[day+7] += births[day] # set today's parents to respawn again
        day += 1
    return fish

def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 5934

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 356190

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 26984457539

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 1617359101538

print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))
