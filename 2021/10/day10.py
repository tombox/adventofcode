"""
https://adventofcode.com/2021/day/10
"""

def load_data(filename: str) -> list:
    " Load data "
    lines = open(filename, "r").read().splitlines()
    #data = [x.replace(' |',' ').split(' ') for x in open(filename, "r").read().splitlines()]
    return lines

def check_syntax(input_line):
    syntax_eror = False

    open_chars = '[({<'
    close_chars = '])}>'
    stack = []

    for c in input_line:
        if c in open_chars:
            stack.append(c)
        else:
            popped = stack.pop()
            required = close_chars[open_chars.index(popped)]

            if c != required:
                syntax_eror = True
                return c
    return ''

def part1(file: str) -> int:
    " Day 10 puzzle part 1"
    items  = load_data(file)

    scores = {')':3,']':57,'}':1197,'>':25137}
    score = 0

    for item in items:
        invalid_char = check_syntax(item)
        if invalid_char  != '':
            score += scores[invalid_char]

    return score

def part2(file: str) -> int:
    " Day 10 puzzle part 2"
    items  = load_data(file)

    opening_chars = '[({<'
    close_chars = '])}>'
    scores = {')':1,']':2,'}':3,'>':4}
    score = 0

    # Find lines without errors
    items_correct = filter(lambda x: check_syntax(x)=='',items)  
            
    # Fix lines completions and calculate scores
    score_list = []
    for item in items_correct:
        score = 0
        stack = []
        for char in item:
            if char in opening_chars:
                closing_char = close_chars[opening_chars.index(char)]
                stack.append(closing_char)
            else:
                stack.pop()

        for char in reversed(stack):
            score = (score * 5) + scores[char]

        score_list.append(score)
        
    score_list.sort()
    return score_list[len(score_list)//2]



def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 26397

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 364389

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 288957

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 2870201088


print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))
