"""
https://adventofcode.com/2020/day/12
"""
import math
rad = math.radians

lines = map(lambda x:[x[0],int(x[1:])], (x for x in open("input.txt", "rb").read().splitlines()))

x = y = 0
angle = 90

for k,v in lines:
    if k == 'F':
        x += math.sin(rad(angle))*v
        y -= math.cos(rad(angle))*v 
    if k in 'NS': y+=v * (-1 if k=='S' else 1)
    if k in 'EW': x+=v * (-1 if k=='W' else 1)
    if k in 'LR': angle+=v * (-1 if k=='R' else 1)   

print "Part 1 answer: ",abs(x)+abs(y)

lines = map(lambda x:[x[0],int(x[1:])], (x for x in open("input.txt", "rb").read().splitlines()))

x = y = 0
wx,wy = 10,1

for k,v in lines:
    if k == 'F': x,y = (x+wx*v, y+wy*v)
    if k in 'NS': wy+=v * (-1 if k=='S' else 1)
    if k in 'EW': wx+=v * (-1 if k=='W' else 1)
    if k == 'L' or k == 'R': 
        if k == 'R': v *= -1
        
        wx, wy = wx*math.cos(rad(v)) - wy*math.sin(rad(v)), wx*math.sin(rad(v)) + wy*math.cos(rad(v))
    
print "Part 2 answer: ",abs(x)+abs(y)