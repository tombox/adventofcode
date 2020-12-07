"""
https://adventofcode.com/2020/day/7
"""

lines= map(lambda x: x.split(), open("input.txt", "rb").read().splitlines())

# Create dict for each bag rule
bag_rules = {}
for line in lines:
    bag_rules[' '.join(line[0:2])] = line[4:]

# Part 1  
found = []
def find_bags(baglist,a,b):
    for k,v in baglist.items():
        for n in range(0,len(v)-1):
            if v[n] == a and v[n+1] == b:
                if not k in found: found.append(k)
                find_bags(baglist, *k.split())

          
find_bags(bag_rules,'shiny','gold')
print len(found)

# Part 2
ibags = {}
def iter_bags(baglist,bag):
    count = 1
    for k,v in baglist.items():
        if k == bag:
            for n in range(0,len(v),4):
                num_bags = int(v[n]) if v[n].isdigit() else 0
                count += num_bags * iter_bags(baglist, ' '.join([v[n+1],v[n+2]]))

    return count


print iter_bags(bag_rules,'shiny gold')-1