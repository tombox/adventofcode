"""
https://adventofcode.com/2020/day/6
"""
import re
import itertools as it

# Part 1
total = 0
for is_not_empty, lines in it.groupby(open("input.txt"), lambda line: bool(line.strip())):
    if is_not_empty: total += len(''.join(set(c for line in lines for c in line.strip()))) 

print total

# Part 2

total = 0
for is_not_empty, lines in it.groupby(open("input.txt"), lambda line: bool(line.strip())):
    if is_not_empty:
        total += len(reduce(lambda x,y: re.sub('[^%s]' % y,'',x) ,(item for item in list(line.strip()for line in lines))))
print total
