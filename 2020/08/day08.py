"""
https://adventofcode.com/2020/day/8
"""

code = map(lambda a: [a[0],int(a[1])],(x.split() for x in open("input.txt", "rb").read().splitlines()))

def exe(code, flip_pos=-1):
    acc = pos = loops = 0
    used = []
    flip_ops = ['jmp','nop']
    
    while pos < len(code) and pos not in used:
        op,num = code[pos]
        used.append(pos)
        if pos == flip_pos and op in flip_ops: 
            op = op.replace(flip_ops[flip_ops.index(op)],flip_ops[1-flip_ops.index(op)])
        acc += num if op == 'acc' else 0
        pos += 1 if (op != 'jmp') else num
    return acc, pos in used

print "Part 1 answer: ",exe(code)[0]

for n in range(0,len(code)):
    acc, looped = exe(code,n)
    if looped == False:
        print "Part 2 answer: ",acc
