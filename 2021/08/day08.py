"""
https://adventofcode.com/2021/day/7
"""

def load_data(filename: str) -> list:
    " Load data "
    data = [x.replace(' |',' ').split(' ') for x in open(filename, "r").read().splitlines()]
    return data

def str_to_bin(digit_str):
    """ Coonvert string to binary value ie:
    'a' -> 1
    'ab' -> 11
    'bc' -> 110
    'abc'- > 111
    """
    vals = [2**(ord(x)-ord('a')) for x in sorted(digit_str)]
    return sum(vals)


def part1(file: str) -> int:
    " Day 08 puzzle part 1"
    items  = load_data(file)
    total = 0
    for item in items:
        outputs = item[-4:]
        total += sum([len(output) in (2,3,4,7) for output in outputs])
    return total

def decipher_by_length(digit_str_list: list, values: list) -> list:
    " Collect the ones we know, as they are unique length "

    for digit_str in digit_str_list:
        val = str_to_bin(digit_str)
        length = len(digit_str)

        if length  == 2:
            values[1] = val
        if length  == 3:
            values[7] = val
        if length  == 4:
            values[4] = val
        if length  == 7:
            values[8] = val

    return values

def decipher_by_masks(digit_str_list: list, values: list) -> list:
    " work out the digits by comparing them "
    v = values

    # bit mask of digit 4 with digit 1 bits removed to use as an identifier for digits 2,3,5
    digit_mask = v[4] - v[1]

    for digit_str in digit_str_list:
        val = str_to_bin(digit_str)

        if len(digit_str) == 6: # 6 in lenth so its either 0,6,9
            # it's digit 9 if it masks with digit 7 and digit 4
            if val & v[7] == v[7] and val & v[4] == v[4]:
                v[9] = val

            # it's digital 6 if it masks with digit 7
            if val & v[7] != v[7]:
                v[6] = val

            # it's digit 0 if it masks with 7 but not 4
            if val & v[7] == v[7] and  val & v[4] != v[4]:
                v[0] =  val

        if len(digit_str) == 5: # 5 in lenth so its either  2 3 5
            # it's digit 2 if doesn't mask with 1 or the digit_mask
            if val & v[1] != v[1] and val & digit_mask != digit_mask:
                v[2] = val

            # it's digit 3 if it dosn't mask with the digit_mask but does mask to 1
            if val & digit_mask != digit_mask and val & v[1] == v[1]:
                v[3] = val

            # if's digit 5 if it masks with digit_mask
            if val & digit_mask == digit_mask:
                v[5] =  val

    return v


def calcline(digit_str_list: list ,output_str_list: list) -> int:
    " Decipher which digits_strs map to which digits then return corresponding output values  "

    # v array collects the binary value of each digit as we work it out
    v = [0]*10

    # work out digits by length then by comparing them to each other
    v = decipher_by_length(digit_str_list, v)
    v = decipher_by_masks(digit_str_list, v)

    result_str = ''
    # now we know all the digits, we can map them to the outputs and build final number
    for output_str in output_str_list:
        val = str_to_bin(output_str)
        result_str += str(v.index(val))

    return int(result_str)


def part2(file: str) -> int:
    " Day 08 puzzle part 1"
    items  = load_data(file)

    total = 0
    for item in items:
        digit_str_list, output_str_list = item[:10],item[-4:]
        value = calcline(digit_str_list, output_str_list)
        total += value

    return total

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
