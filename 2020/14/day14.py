"""
https://adventofcode.com/2020/day/14
"""
from itertools import combinations

lines = open("input.txt", "rb").read().splitlines()

def convert_mask1(mask):
    mask1 = mask.replace('X','0')
    mask2 = mask.replace('1','X')
    mask2 = mask2.replace('0','1')
    mask2 = mask2.replace('X','0')
    return int(mask1,2), int(mask2,2)

mask1 = mask2 = 0
slots = {}
for line in lines:
    
    if 'mask' in line:
        mask = line[-36:]
        mask1,mask2 = convert_mask1(mask)
    elif 'mem' in line:
        parts = line.split()
        address = int(parts[0][4:-1])
        value = int(parts[2])
        slots[address] = mask1 | (value & ~(mask2 & value))

print "Part 1 answer:", sum(slots)

def convert_mask2(mask):
    mask_add = mask.replace('X','0')
    mask_float = mask.replace('1','0')
    mask_float = mask_float.replace('X','1')
    return int(mask_add,2), int(mask_float,2)

mask_add = mask_float = 0
slots = {}
vals = []
for line in lines:
    if 'mask' in line:
        vals = []
        mask = line[-36:]
        mask_add,mask_float = convert_mask2(mask)
        for n in range(len(mask)): 
            v = pow(2,n)
            if v & mask_float: vals.append(v)

    elif 'mem' in line:
        parts = line.split()
        address = int(parts[0][4:-1])
        value = int(parts[2])
        masked_address = address | mask_add

        for comb_count in range(pow(2,len(vals))):
            new_address = masked_address & (~mask_float)

            for vals_index in range(len(vals)):
                if pow(2,vals_index) & comb_count: 
                    new_address += vals[vals_index]
                    
            slots[new_address] = value

print "Part 2 answer:",sum(slots)
    
    