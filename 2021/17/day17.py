"""
https://adventofcode.com/2021/day/§7
"""

def load_data(filename: str) -> list:
    " Load data "
    x,y =  open(filename, "r").read().splitlines()[0][13:].split(', ')
    return [int(x) for x in x[2:].split('..')],[int(x) for x in y[2:].split('..')]

def part1(file: str) -> int:
    " Day 17 puzzle"
    t  = load_data(file)

    max_y_hit= False
    max_max_y = 0
    mx = 0
    my = 0
    tvs = []
    for ty in range(t[1][0]-1,t[1][0]*-1+1):
     for tx in range(t[0][1]+1):
        vx = tx
        vy = ty
        x = 0
        y = 0
        max_y = 0

        while True:
            x += vx
            y += vy

            if y > max_y:
                max_y = y

            if vx > 0:
                vx -= 1
            vy -=1

            if x >= t[0][0] and x <= t[0][1] and y >= t[1][0] and y <= t[1][1]:
                tvs.append([tx,ty])
                if max_y > max_max_y:
                    mx = tx
                    my = ty
                    max_max_y = max_y
                break

            if x > t[0][1]: break      
            if y < t[1][0]: break        
        
    print('Max',max_max_y)   
    print('Total velocities',len(tvs))         
    return 

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

print("Part 2 test answer = ", part1("test-input.txt"))
print("Part 2 answer = ", part1("input.txt"))
