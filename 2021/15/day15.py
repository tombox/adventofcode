"""
https://adventofcode.com/2021/day/15
"""

import numpy as np
def load_data(filename: str) -> list:
    " Load data "
    lines = [[int(c) for c in x] for x in open(filename, "r").read().splitlines()]
    return np.array(lines)


def get_min(d,visited):

    height, width = d.shape
    vmin = 999999
    vx=vy=-1

    for x in range(width):
        for y in range(height):
            if d[y][x] < vmin and not visited[y][x]:
                vx = x
                vy = y
                vmin = d[y][x]
    return vx,vy


def find_route(d):
    height, width = d.shape

    m = d.copy()
    m.fill(999999)

    n = d.copy()
    n.fill(999999)

    x=y=0
    m[0][0]=0
    visited_count =0
    max_elements = width*height:
    
    while visited_count != max_elements:
        if x > 0:
            left =  d[y][x-1]+m[y][x]
            if m[y][x-1] > left:
                m[y][x-1] = left
                n[y][y-1] = left

        if y > 0:
            up = d[y-1][x]+m[y][x]
            if m[y-1][x] > up:
                m[y-1][x] = up
                n[y-1][x] = up

        if x < width-1:
            right = d[y][x+1]+m[y][x]
            if m[y][x+1] > right:
                m[y][x+1] = right  
                n[y][x+1] = right 

        if y <  height-1:
            down = d[y+1][x] +m[y][x]
            if m[y+1][x] > down:
                m[y+1][x] = down
                n[y+1][x] = down

        n[y][x] = 999999 

        vals= np.where(n == np.amin(n))
        listOfCordinates = list(zip(vals[0], vals[1]))
        y,x = listOfCordinates[0]

        visited_count +=1

    return m[-1][-1]


def part1(file: str) -> int:
    " Day 15 puzzle part 1"
    d  = load_data(file)
    return find_route(d)
                
def part2(file: str) -> int:
    " Day 15 puzzle part 2"
    d  = load_data(file)
    resized = 5
    height, width = d.shape
    f = np.array(width*resized *height*resized )
    f.resize(height*resized ,width*resized )

    for y in range(0,resized):
        for x in range(0,resized):
            for ay in range(height):
                for ax in range(width):
                    f[y*height+ay][x*width+ax] = ((d[ay][ax] + y+x) -1) % 9+1

    return find_route(f)


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


#print("Part 1 test answer = ", part1("test-input.txt"))

#print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))
