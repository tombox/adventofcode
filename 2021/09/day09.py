"""
https://adventofcode.com/2021/day/9
"""
import numpy as np

def load_data(filename: str) -> list:
    " Load data "
    lines = open(filename, "r").read().splitlines()
    #data = [x.replace(' |',' ').split(' ') for x in open(filename, "r").read().splitlines()]
    data = []
    for line in lines:
        y = [int(x) for x in line]
        data.append(y)
    return data

def check_is_lowest(dmap, x,y):
    height,width  = dmap.shape
    s = [0]*4

    s[0] = dmap[y][x-1] if x > 0 else 9
    s[1] = dmap[y][x+1] if x < width-1 else 9
    s[2] = dmap[y-1][x] if y > 0 else 9
    s[3] = dmap[y+1][x] if y < height-1 else 9

    return dmap[y][x] <= min(s) and dmap[y][x] < 9

def part1(file: str) -> int:
    " Day 09 puzzle part 1"
    lines = load_data(file)

    dmap = np.array(lines)
    height,width  = dmap.shape
    dmap.resize(height,width)

    n = 0
    for y in range(height):
        for x in range(width):
            if check_is_lowest(dmap, x,y):
                n += dmap[y][x]+1

    return n


def check_is_lowest_recursive(dmap, x,y):
    height,width  = dmap.shape

    if check_is_lowest(dmap, x,y):
        v = dmap[y][x]
        dmap[y][x] = 10
        if x-1 >= 0 and dmap[y][x-1] >= v and dmap[y][x-1] < 9:
            if check_is_lowest_recursive(dmap, x-1,y):
                dmap[y][x-1] = 10

        if x+1 < width and dmap[y][x+1] >= v and dmap[y][x+1] < 9:
            if check_is_lowest_recursive(dmap, x+1,y):
                dmap[y][x+1] = 10

        if y-1 >= 0 and dmap[y-1][x] >= v and dmap[y-1][x]  < 9:
            if check_is_lowest_recursive(dmap, x,y-1):
                dmap[y-1][x] = 10

        if y+1 < height and  dmap[y+1][x] >= v and dmap[y+1][x] < 9:
            if check_is_lowest_recursive(dmap, x,y+1):
                dmap[y+1][x] = 10

        return True

    return False


def part2(file: str) -> int:
    " Day 09 puzzle part 1"
    lines = load_data(file)
    dmap = np.array(lines)
    width, height = len(lines[0]), len(lines)
    dmap.resize(height,width)

    basin_sizes = []

    for y in range(height):
        for x in range(width):
            if check_is_lowest_recursive(dmap, x,y):
                size = np.count_nonzero(dmap == 10)
                dmap[dmap == 10] = 20
                basin_sizes.append(size)

    basin_sizes.sort()

    return np.prod(basin_sizes[-3:])



def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 26

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 514

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 61229

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 1012272

print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))
