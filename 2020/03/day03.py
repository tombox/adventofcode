"""
https://adventofcode.com/2020/day/3
"""

lines = open("input.txt", "rb").read().splitlines()

def count_trees(right,down):
    return reduce(lambda x,y: x+int(lines[y][right*y/down%31] is '#'), (y for y in range(0,len(lines),down)))

# Part 1

print count_trees(3,1)

# Part 2

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
print reduce(lambda x,y: x*y,list(count_trees(*slope) for slope in slopes))

