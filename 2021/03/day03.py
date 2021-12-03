"""
https://adventofcode.com/2021/day/2
"""

def load_data(filename: str) -> list:
    " Given txt file consisting of a string on a new line, returns as list "
    return [x.decode('UTF-8') for x in open(filename, "rb").read().splitlines()]

def check_bits(data: list,pos: int, digit: str, greater_equal: bool=True) -> bool:
    """ Find if occurance of given digit is greter-equal or less-equal
    to majoirty, for char at position pos in each line item string """

    count = sum(item[pos] == digit for item in data)

    if not greater_equal:
        return count <= len(data)/2

    return count >= len(data)/2


def part1(file: str) -> int:
    " Day 03 puzzle part 1"
    lines = load_data(file)
    epilson_str = gamma_str = ''

    for pos in range(len(lines[0])):
        valid = check_bits(lines, pos, '1')
        gamma_str += '0' if valid else '1'
        epilson_str += '1' if valid  else '0'

    return(int(gamma_str,2) * int(epilson_str,2))

def part2(file: str) -> int:
    " Day 03 puzzle part 2"

    data = lines = load_data(file)
    pos = 0
    while len(data) > 1:
        valid = check_bits(data,pos, '1')
        item_filter = lambda x: (x[pos] == '1' and valid) or (x[pos] == '0' and not valid)
        data = list(filter(item_filter,data))
        pos+=1

    oxygen = int(data[0],2)

    data = lines
    pos = 0
    while len(data) > 1:
        valid = check_bits(data,pos, '0', greater_equal=False)
        item_filter = lambda x: (x[pos] == '0' and valid) or (x[pos] == '1' and not valid)
        data = list(filter(item_filter,data))
        pos+=1

    co2= int(data[0],2)
    return oxygen * co2

def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 198

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 4147524

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 230

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 3570354

print("Part 1 answer = ", part1("input.txt"))
print("Part 2 answer = ", part2("input.txt"))
