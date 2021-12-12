"""
https://adventofcode.com/2021/day/11
"""
import numpy as np
from nptyping import NDArray, Int

def load_data(file):
    return np.array([[int(c) for c in x] for x in np.loadtxt(file, dtype=str)])

def process_data(d: NDArray[Int]) -> None:
    """ Increment elemtents, also increment neighbours if element > 9, then set > 9 to 0 """
    d += 1
    while np.count_nonzero(d == 10):
        for (x, y), item in np.ndenumerate(d):
            if d[y][x] == 10:
                d[y][x] += 1
                subset = d[max(y-1,0):min(y+2,d.shape[1]),max(x-1,0):min(x+2,d.shape[0])]
                subset[subset != 10] +=1
    d[d > 9] = 0

def part1(file: str) -> int:
    " Day 11 puzzle part 1"
    d = load_data(file)
    score = step = 0
    
    while step < 100:
        process_data(d)
        score += np.count_nonzero(d == 0)
        step += 1

    return score

def part2(file: str) -> int:
    " Day 11 puzzle part 2"
    d = load_data(file)
    step = 0

    while True:
        process_data(d)
        step += 1 
        if np.sum(d) == 0:
            return step


def test():
    d  = load_data("test-input.txt")

    cx = 2
    cy = 2
    a = d[cy-1:cy+2,cx-1:cx+2]
    print(d)
    print(a)
    a[a > 1] +=1
    print(d)


def test_example_part1():
    " {}Pytest for function example data part1() "
    assert part1("test-input.txt") == 1656

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 1613

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 195

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 510


print("Part 1 test answer = ",part1("test-input.txt") )
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))

#test()