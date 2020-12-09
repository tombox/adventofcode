"""
https://adventofcode.com/2020/day/9
"""
lines = [int(x) for x in open("input.txt", "rb").read().splitlines()]

def part1(input, preamble):
    n = p = 0
    for line in input:
        if n< len(lines)-preamble:
            s = lines[n:n+preamble+1]
            if not filter(lambda (a,b): a+b==s[-1],[(x,y) for x in s[0:len(s)] for y in s[0:len(s)] if x is not y]): break
        n += 1
    return input[n+preamble]

result = part1(lines,25) 
print "Part 1 answer: ",result

def part2(input, target):
    size = len(input)
    for pos in range(0,size):
        length = sum = 0
        while sum < target and length < size-length:
            sum += input[pos+length]
            length += 1
        if sum == target:
            section = input[pos:pos+length]
            section.sort()
            return  section[0]+section[-1]
    return 0

print "Part 2 answer: ", part2(lines, result)

