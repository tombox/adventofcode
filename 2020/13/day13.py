"""
https://adventofcode.com/2020/day/13
"""
import math
rad = math.radians

lines = open("input.txt", "rb").read().splitlines()
start_time = int(lines[0])
bus_times = []
for y in lines[1].split(','):
    try:
        time = int(y)
        bus_times.append(time)
    except:
        continue

def get_earliest(time,target):
    t = 0
    while t<= target:
        t += time
    return t

def part1():
    earliest_delta = 0
    earliest_bus = 0
    for bus in bus_times:
        time = get_earliest(bus,start_time)
        delta = time-start_time
        if earliest_bus == 0 or delta < earliest_delta:
            earliest_bus = bus
            earliest_delta = delta
    return earliest_bus*earliest_delta

print "Part 1 answer:",part1()

bus_times = []
n = 0
for y in lines[1].split(','):
    if y != 'x':
        bus_times.append((int(y),n))
    n +=1

def buses_align(vals,x):
    return sum(map(lambda v: (v[1]+x) % v[0],vals)) == 0

def part2():
    n = 1
    size = 2
    start = 0
    step = bus_times[0][0]
    while True:
        x = start+ step*n
        if buses_align(bus_times[:size],x):
            if size == len(bus_times):
                break
            size +=1
            n=0
            start= x
            step *= bus_times[size-2][0]
        n+=1
    return x

print "Part 2 answer:",part2()
