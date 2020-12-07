
"""
https://adventofcode.com/2020/day/5
"""

def binary_part(code,char,delta, result=0):
    for c in code:
        delta = delta/2
        if c == char: result += delta

    return result

def process_seat(code):
    col = binary_part(code[:7],'B',128)
    row = binary_part(code[7:],'R',8)
    return col*8+row

lines = open("input.txt", "rb").read().splitlines()

seat_list = [process_seat(line) for line in lines]
seat_list.sort()

# Part 1
print "Highest: ",seat_list[-1]

# Part 2

for n in range(0,seat_list[-1]):
    if n not in seat_list and n-1 in seat_list and n+1 in seat_list: print "Your seat is ",n

