"""
https://adventofcode.com/2021/day/2
"""

def load_data(filename: str) -> list:
    " Given txt file consisting of 'str int' pairs each on a new line, returns as list of tuples "
    with open(filename, "rb") as file:
        lines = (line.split() for line in file.read().splitlines())
    return list(map(lambda parts: (parts[0].decode('UTF-8'), int(parts[1])), lines))

def part1(file: str) -> int:
    " Day 02 puzzle part 1"

    lines = load_data(file)
    pos = depth = 0

    for code,val in lines:
        if code == 'up':
            depth -= val
        if code == 'down':
            depth += val
        if code == 'forward':
            pos += val
    return pos*depth

def part2(file: str) -> int:
    " Day 02 puzzle part 2"

    lines = load_data(file)
    pos = depth = aim = 0

    for code,val in lines:
        if code == 'up':
            aim -= val
        if code == 'down':
            aim += val
        if code == 'forward':
            pos += val
            depth += val*aim
    return pos*depth

def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 150

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 900

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 2027977

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 1903644897

print("Part 1 answer = ", part1("input.txt"))
print("Part 2 answer = ", part2("input.txt"))
