"""
https://adventofcode.com/2020/day/2
"""

lines= map(lambda x: x.split(), open("input.txt", "rb").read().splitlines())

#Part 1
def test(line):
    a,b,c = line
    upper,lower = map(int,a.split('-'))
    return upper <= c.count(b[0]) <= lower

print len(filter(test,lines))

#Part 2

valid = 0
for line in lines:
    lower, upper = [int(i) for i in line[0].split('-')]
    char = line[1][0]
    password = line[2]
    count = password.count(char)

    if password[lower-1] == char and password[upper-1] != char or (password[lower-1] != char and password[upper-1] == char):
        valid += 1

print valid

