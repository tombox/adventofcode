"""
https://adventofcode.com/2021/day/5
"""
import numpy as np

def load_data(filename: str) -> list:
    " Load  data "
    # convert each line from "0,1 -> 2,4" to "0,1,2,4" then to ints
    data = [[int(x) for x in x.replace(' -> ',',').split(',')]
              for x in open(filename, "r").read().splitlines()]
    return data


def part1(file: str) -> int:
    " Day 05 puzzle part 1"
    data  = load_data(file)
    max_val = np.amax(data)+1
    grid = np.zeros((max_val)**2, dtype=int)
    grid.resize(max_val,max_val)

    for item in data:
        x1,y1,x2,y2 = item
        x_step = -1 if x2 < x1 else 1
        y_step = -1 if y2 < y1 else 1

        # mark horizontal & vertical lines
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2+x_step, x_step):
                for y in range(y1, y2+y_step, y_step):
                    grid[y][x] += 1

    return np.count_nonzero(grid > 1)



def part2(file: str) -> int:
    " Day 05 puzzle part 2"
    data  = load_data(file)
    max_val = np.amax(data)+1
    grid = np.zeros((max_val)**2, dtype=int)
    grid.resize(max_val,max_val)

    for item in data:
        x1,y1,x2,y2 = item
        x_step = -1 if x2 < x1 else 1
        y_step = -1 if y2 < y1 else 1

        # mark horizontal & vertical lines
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2+x_step, x_step):
                for y in range(y1, y2+y_step, y_step):
                    grid[y][x] += 1

        # mark diagonal lines
        if abs(x2-x1) == abs(y2-y1):
            for x in range(x1, x2+x_step, x_step):
                y = y1+y_step*abs(x-x1)
                grid[y][x] += 1

    return np.count_nonzero(grid > 1)

def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 5

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 5084

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 12

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 17882

print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))
