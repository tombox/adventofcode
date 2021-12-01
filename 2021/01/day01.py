"""
https://adventofcode.com/2021/day/1
"""

def load_data(file: str) -> list:
    " Given txt file consisting of ints, each on a new line, returns as list of ints "
    return [int(x) for x in open(file, "rb").read().splitlines()]

def part1(file: str) -> int:
    " Day 01 puzzle part 1"

    lines = load_data(file)
    # Sum number of times the next item in list is greater than previous
    return sum(map(lambda x,y: x < y, lines, lines[1:]))


def part2(file: str) -> int:
    " Day 01 puzzle part 2"

    lines = load_data(file)
    # Build list of sum of next 3 items (ints) in list
    window_sums = list(map(lambda x,y,z: x+y+z, lines, lines[1:], lines[2:]))
    # Sum number of times the next item in list is greater than previous
    return sum(map(lambda x,y: x < y, window_sums, window_sums[1:]))

def test_part1():
    " Pytest for function part1() "
    assert part1("test-input.txt") == 7

def test_part2():
    " Pytest for function part2() "
    assert part2("test-input.txt") == 5


print("Part 1 answer = ", part1("input.txt"))
print("Part 2 answer = ", part2("input.txt"))
