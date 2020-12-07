"""
https://adventofcode.com/2020/day/1
"""

lines = map(lambda x: int(x),open("input.txt", "rb").read().splitlines())

# Part 1
print reduce(lambda x,y: x*y, [(x,y) for x in lines for y in lines if x+y==2020].pop())

# Part 2
print reduce(lambda x,y: x*y, tuple([(x,y,z) for x in lines for y in lines for z in lines if x+y+z==2020].pop()))
