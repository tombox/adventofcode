"""
https://adventofcode.com/2021/day/16
"""
import numpy as np


def load_data(filename: str) -> list:
    " Load data "
    lines = open(filename, "r").read().splitlines()
    return lines

def convert_string(input):
    t = ''
    for c in input:
        bin = "{0:b}".format(int(c,16))
        bin = '0'*(3-len(bin)+1) + bin
        t += bin
    return t

def process_type(typeid,sub_stack):
    if typeid == 0:
        return sum(sub_stack)

    if typeid == 1:
        return np.prod(sub_stack)

    if typeid == 2:
        return min(sub_stack)

    if typeid == 3:
        return max(sub_stack)

    if typeid == 5:
        return int(sub_stack[0] > sub_stack[1])

    if typeid == 6:
        return int(sub_stack[0] < sub_stack[1])

    if typeid == 7:
        return int(sub_stack[0] == sub_stack[1])
        
    return None

def process_bin(input, stack = None, sum_versions=False):
    version = int(input[0:3],2)
    if sum_versions:
        stack[0] += version
    typeid = int(input[3:6], 2)
    plength = 6

    if typeid == 4:
        ended = False
        lv = ''
        p = 0
        while ended == False:
            part = input[6+p*5:11+p*5]
            if part[0] == '0':
                ended = True
            lv += part[1:]
            plength += len(part)
            p+=1

        lv = int(lv, 2)
        if stack != None:
            stack.append(lv)
            
        return plength
    else:
        if sum_versions:
            sub_stack = stack
        else:
            sub_stack = []
        lengthTypeID = input[6:7]
        plength += 1
        if lengthTypeID  == '0':
            v = int(input[plength:plength+15], 2)
            plength+=15
            end = plength+v
            while plength < end:
                plength += process_bin(input[plength:],sub_stack,sum_versions)
        else:
            subpackets_count = int(input[plength:plength+11], 2)
            plength+=11
            n = 0
            while subpackets_count > 0:
                plength += process_bin(input[plength:],sub_stack,sum_versions)
                subpackets_count-=1

        if stack != None and not sum_versions:
            val = process_type(typeid,sub_stack)
            if not None:
                stack.append(val)

        return plength 


def part1(file: str) -> int:
    " Day 16 puzzle part 1"
    items  = load_data(file)
    stack = [0]
    bin_str = convert_string(items[0])
    process_bin(bin_str,stack,sum_versions=True)
    return stack[0]

def part2(file: str) -> int:
    " Day 16 puzzle part 2"
    items  = load_data(file)
    stack = []
    bin_str = convert_string(items[0])
    process_bin(bin_str,stack)
    return stack[0]


def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 31

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 945

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 54

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 10637009915279

print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))
