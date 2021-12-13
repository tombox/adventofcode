"""
https://adventofcode.com/2021/day/13
"""
import numpy as np

def load_data(filename: str) -> list:
    " Load data "
    lines = open(filename, "r").read().splitlines()
    coords = []
    folds = []
    for line in lines:
        if ',' in line:
            x,y = line.split(',')
            coords.append([int(x),int(y)])
        else:
            if 'fold along' in line:
                parts  = line.split(' ')
                axis,val = parts[2].split('=')
                folds.append([axis,int(val)])

    mx = my = 0
    for x,y in coords:
        mx = max(x,mx)
        my = max(y,my)
    mx+=1
    my+=1
    if my % 2 == 0:
        my +=1 
    m = np.zeros(mx*my,dtype=int)
    m.resize(my,mx)

    for x,y in coords:
        m[y][x] = 1

    return m,folds


def part1(file: str) -> int:
    " Day 13 puzzle part 1"
    m,folds = load_data(file)
    axis,val = folds[0]

    print('---',axis,val)

    if axis == 'x':
        m = m | np.fliplr(m)
        m = m[::,0:val-0]
    if axis == 'y':
        m = m | np.flipud(m)
        m = m[0:val,::]

    return np.sum(m)

def part2(file: str) -> int:
    " Day 13 puzzle part 1"
    m,folds = load_data(file)
    fold =0
    
    for axis,val in folds:
        if axis == 'x':
            m = m | np.fliplr(m)
            m = m[::,0:val-0]
        if axis == 'y':
            m = m | np.flipud(m)
            m = m[0:val,::]

        dots = np.sum(m)
        fold+=1

    height,width = m.shape
    for y in range(height):
        s = ''
        for x in range(width):
            s += '█' if m[y][x] > 0 else '.'
        print(s)


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
