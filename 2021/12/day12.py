"""
https://adventofcode.com/2021/day/12
"""

def load_data(filename: str) -> list:
    " Load data "
    items = [x.split('-') for x in open(filename, "r").read().splitlines()]
    m = {}

    for c1,c2 in items:
        if not c1 in m: m[c1] = []
        if c2 not in m: m[c2] = []
        if c2 not in m[c1]: m[c1].append(c2)
        if c1 not in m[c2]: m[c2].append(c1)
    return m

def count_list_in_list(long_list, short_list):
    " Count the number of occurances of short_list in long_list "
    count = 0
    for n in range(len(long_list)):
        ln = 0
        while ln < len(short_list) and ln+n < len(long_list) and long_list[n+ln] == short_list[ln]:
            ln +=1
        if ln == len(short_list):
            count +=1
    return count

def find_paths(complete_paths, cave, links, path, limit = 1):
    " Find all paths according to rules and save them in complete_paths list "

    # check each exit in the given cave
    for exit in links[cave]:
        # if a small cave and we've been there before, then set limit to 1, so no more small caves are revisited
        if cave.islower() and path.count(cave) > 1:
            limit = 1

        # if exit is a big cave, or its a small cave and have been within number of times permitted
        # or if it's the end, but not the start 
        if exit.isupper() or (exit.islower() and path.count(exit) < limit and exit!='start') or exit=='end':

            # check we have been down this path with minimum number of times (check occurance of curentCave->exit pairs)
            if  count_list_in_list(path,[cave,exit]) < 2: 
                new_path = path.copy()
                new_path.append(cave)

                # found exit so save the path
                if exit == 'end':
                    if new_path not in complete_paths:
                        complete_paths.append(new_path)
                else:
                        find_paths(complete_paths, exit, links, new_path, limit)

def part1(file: str) -> int:
    " Day 12 puzzle part 1"

    m  = load_data(file)
    complete_paths = []

    for exit in m['start']:
        path = []
        find_paths(complete_paths, exit, m, path)
    return len(complete_paths)

def part2(file: str) -> int:
    " Day 12 puzzle part 2"

    m  = load_data(file)
    complete_paths = []

    for exit in m['start']:
        path = []
        find_paths(complete_paths, exit, m, path, 2)
    return len(complete_paths)


def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input3.txt") == 226

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 5874

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 36

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 153592



print("Part 1 test answer = ", part1("test-input3.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))