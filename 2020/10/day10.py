"""
https://adventofcode.com/2020/day/10
"""
from itertools import groupby
import time
lines = [int(x) for x in open("input.txt", "rb").read().splitlines()]
lines.sort()
lines.append(lines[-1]+3)
lines.insert(0,0)

diffs = [lines[n+1]-lines[n] for n in range(0,len(lines)-1)]
print "Part 1 answer: ",diffs.count(1)*diffs.count(3)
start_time = time.time()
diffs_rle = [len(list(g)) for k, g in groupby(diffs) if k ==1]
print "Part 2 answer: ",pow(7,diffs_rle.count(4)) * pow(4,diffs_rle.count(3)) *  pow(2,diffs_rle.count(2))
print("--- %.5f seconds ---" % (time.time() - start_time))