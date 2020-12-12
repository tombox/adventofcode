"""
https://adventofcode.com/2020/day/11
"""
from copy import deepcopy

def adjacent_count(map,ix,iy):
    count = 0
    for y in range(max(0,iy-1),min(len(map),iy+2)):
        count += map[y][max(0,ix-1):min(ix+2,len(map[0]))].count('#')
    return count

def line_of_sight_count(map,ix,iy):
    count = 0
    dirs = [(dx,dy) for dx in range(-1,2) for dy in range(-1,2) if not dx == dy == 0]
    seats = [0]*9

    for (dx,dy) in dirs:
        for r in range(1,max(len(map),len(map[0]))):
            rx = ix+dx*r
            ry = iy+dy*r   
            if rx >= 0 and rx < len(map[0]) and ry >= 0 and ry < len(map) and seats[dx+(dy+1)*3+1] == 0:
                if map[ry][rx] == '#':
                    seats[dx+(dy+1)*3+1] = 1
                    break
                if map[ry][rx] == 'L':
                    seats[dx+(dy+1)*3+1] = -1
                    break

    seats = [0 if i < 0 else i for i in seats]
    return sum([0 if x<0 else x for x in seats])

def iter1(map):
    new_map = deepcopy(map)
    
    for (x,y) in [(x,y) for x in range(0,len(map[0])) for y in range(0,len(map1))]:
            occ =  adjacent_count(map,x,y)
            if map[y][x] == 'L' and occ == 0:
                    new_map[y][x] = '#'
            if map[y][x] == "#" and occ > 4:
                    new_map[y][x] = 'L'
    return new_map

def iter2(map):
    new_map = deepcopy(map)
    for (x,y) in [(x,y) for x in range(0,len(map[0])) for y in range(0,len(map1))]:
            occ =  line_of_sight_count(map,x,y)
            if map[y][x] == 'L' and occ == 0:
                    new_map[y][x] = '#'
            if map[y][x] == "#" and occ > 4:
                    new_map[y][x] = 'L'

    return new_map

map1 = map(lambda x:[y for y in x], (x for x in open("input.txt", "rb").read().splitlines()))
map2 = []
count = 0
while map1 != map2:
    map2 = iter1(map1)
    map1 = iter1(map2)
    count += 1

print 'Part 1 answer: ',sum(x.count('#') for x in map1)

map1 = map(lambda x:[y for y in x], (x for x in open("input.txt", "rb").read().splitlines()))
map2 = []
count = 0
while  map1 != map2:
    map2 = iter2(map1)
    map1 = iter2(map2)
    count += 1

print 'Part 1 answer: ',sum(x.count('#') for x in map1)